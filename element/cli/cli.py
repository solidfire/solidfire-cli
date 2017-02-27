import logging
import logging.config
import os
import sys
import click
import click.core
import copy
import csv
from pkg_resources import Requirement, resource_filename
import struct
import base64

from solidfire.factory import ElementFactory
from solidfire import Element
from element.cli import utils as cli_utils

logging.basicConfig()
LOG = logging.getLogger(__name__)
CONTEXT_SETTINGS = dict(auto_envvar_prefix='SOLIDFIRE', token_normalize_func=lambda x: x.lower())
DEBUG_LOGGING_MAP = {
    0: logging.CRITICAL,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG
}
CLI_VERSION = 'v1'

class Context():

    def __init__(self):
        self.logger = None
        self.verbose = False
        self.home = os.getcwd()
        self.connections = dict()
        self.element = None
        self.depth = None
        self.json = None
        self.pickle = None
        self.filter_tree = None
        self.table = None
        self.verifyssl = None

    def log(self, msg, *args):
        """Logs a message to stderr."""
        if args:
            msg %= args
        click.echo(msg, file=sys.stderr)

    def vlog(self, msg, *args):
        """Logs a message to stderr only if verbose is enabled."""
        if self.verbose:
            self.log(msg, *args)

pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'commands'))

class SolidFireCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            import_string = (
                "element.cli.commands.cmd_%s" % (name.lower()))
            mod = __import__(import_string, None, None, ['cli'])
        except ImportError as e:
            LOG.error(name.lower()+" is not a valid module. Please run 'sfcli --help' for a list of valid modules.")
            exit(1)
        return mod.cli

class SolidFireParsingState(click.parser.ParsingState):
    def __init__(self, args):
        self.subparameters = []
        click.parser.ParsingState.__init__(self, args)

class SolidFireParser(click.parser.OptionParser):
    # We overrided this guy because we needed to inject our custom parsing
    # state parameter into the native ParsingState. Other than that, the
    # logic is all the same.
    def parse_args(self, args):
        """Parses positional arguments and returns ``(values, args, order)``
        for the parsed options and arguments as well as the leftover
        arguments if there are any.  The order is a list of objects as they
        appear on the command line.  If arguments appear multiple times they
        will be memorized multiple times as well.
        """
        state = SolidFireParsingState(args)
        try:
            self._process_args_for_options(state)
            self._process_args_for_args(state)
        except click.parser.UsageError:
            if self.ctx is None or not self.ctx.resilient_parsing:
                raise
        return state.opts, state.largs, state.order

    # Basically, this is the thing we're overriding. Typically, this function will
    # consume the array of arguments that come directly from the user. What I'm
    # doing is adding in the subparameters as null whenever they are not provided
    # by the user.
    def _match_long_opt(self, opt, explicit_value, state):
        option = self._long_opt.get(opt, None)
        if option != None:
            if type(option.obj) == SolidFireOption and\
                    option.obj.is_sub_parameter and\
                    opt[2:] not in state.subparameters:
                raise click.parser.BadOptionUsage(opt+" is a subparameter and cannot be provided in this context.")

            if state.subparameters != [] and opt[2:] not in state.subparameters:
                # If we find out that there were some options we were expecting
                # that didn't show up, we account for them by setting them to
                # none here, pushing them into the state machine, and returning.
                # We'll process them in the next iteration.
                extraParams = []
                for paramName in state.subparameters:
                    extraParams.append("--"+paramName)
                    extraParams.append("")
                extraParams.append(opt)
                state.rargs = extraParams + state.rargs
                return


            # If we've gotten here, it implies that we are either handling
            # an expected subparameter (ie opt[2:] in state.subparameters)
            # or we're handling a regular parameter (ie state.subparameters=[])
            # If it is a subparameter,
            # First, remove it from the expected subparameters list because
            # we found it!
            if opt[2:] in state.subparameters:
                state.subparameters.remove(opt[2:])

        # Now, one way or another, we process it.
        # This kicks us out with an error if option=None. Hence, everything
        # following definitely has an option.
        click.OptionParser._match_long_opt(self, opt, explicit_value, state)

        # Finally, if this is a regular parameter, there is a chance it has
        # subparameters we need to expect. We add them to the state machine
        # here. These will be expected in the next iteration.
        if state.subparameters == [] and type(option.obj) == SolidFireOption:
            state.subparameters = copy.deepcopy(option.obj.subparameters)

        # This is the edge case: If we've run out of rargs
        # but we still are expecting some subparams, empty
        # them into rargs now.
        if state.rargs == [] and state.subparameters != []:
            for paramName in state.subparameters:
                state.rargs.append("--" + paramName)
                state.rargs.append("")

class SolidFireOption(click.core.Option):
    def __init__(self, param_decls=None, subparameters=[], is_sub_parameter=False, *args, **kwargs):
        self.subparameters = subparameters # This is simply a list of names that depend on our given param.
        self.is_sub_parameter = is_sub_parameter
        if is_sub_parameter and subparameters != []:
            raise click.BadParameter("An option cannot be both a super parameter and a subparameter.")
        click.core.Option.__init__(self, param_decls, *args, **kwargs)

    def type_cast_value(self, ctx, value):
        """Given a value this runs it properly through the type system.
        This automatically handles things like `nargs` and `multiple` as
        well as composite types.
        """
        if self.type.is_composite:
            if self.nargs <= 1:
                raise TypeError('Attempted to invoke composite type '
                                'but nargs has been set to %s.  This is '
                                'not supported; nargs needs to be set to '
                                'a fixed value > 1.' % self.nargs)
            if self.multiple:
                return tuple(self.type(x or (), self, ctx) for x in value or ())
            return self.type(value or (), self, ctx)

        def _convert(value, level):
            if level == 0:
                if value == "":
                    return None
                return self.type(value, self, ctx)
            return tuple(_convert(x, level - 1) for x in value or ())
        v = _convert(value, (self.nargs != 1) + bool(self.multiple))
        return _convert(value, (self.nargs != 1) + bool(self.multiple))


class SolidFireCommand(click.Command):
    def make_parser(self, ctx):
        """Creates the underlying option parser for this command."""
        parser = SolidFireParser(ctx)
        parser.allow_interspersed_args = ctx.allow_interspersed_args
        parser.ignore_unknown_options = ctx.ignore_unknown_options
        for param in self.get_params(ctx):
            param.add_to_parser(parser, ctx)
        return parser

@click.command(cls=SolidFireCLI, context_settings=CONTEXT_SETTINGS)
@click.option('--mvip', '-m',
              default=None,
              help="SolidFire MVIP",
              required=False)
@click.option('--username', '-u',
              default=None,
              help="SolidFire Cluster username",
              required=False)
@click.option('--password', '-p',
              default=None,
              help="SolidFire cluster password",
              required=False)
@click.option('--version', '-v',
              default="9.0",
              help='The version you would like to connect on',
              required=False)
@click.option('--port', '-q',
              default=443,
              help="The port number on which you wish to connect",
              required=False)
@click.option('--name', '-n',
              default = None,
              help="The name of the connection you wish to use in connections.csv. You can use this if you have previously stored away a connection with 'sfcli connection push'.",
              required=False)
@click.option('--connectionIndex', '-c',
              default=None,
              type=click.INT,
              help="The index of the connection you wish to use in connections.csv. You can use this if you have previously stored away a connection with 'sfcli connection push'.",
              required=False)
@click.option('--verifyssl', '-s',
              default = False,
              help="Enable this to check ssl connection for errors especially when using a hostname. It is invalid to set this to true when using an IP address in the target.",
              required=False,
              is_flag=True)
@click.option('--json', '-j',
              is_flag=True,
              required=False,
              help="To print the full output in json format, use this flag")
@click.option('--pickle', '-k',
              is_flag=True,
              required=False,
              help="To print the full output in a pickled json format, use this flag.")
@click.option('--depth', '-d',
              type=int,
              required=False,
              help="To print the output as a tree and specify the depth, use this option.")
@click.option('--filter_tree', '-f',
              required=False,
              type=click.STRING,
              help="To filter the fields that will be displayed in a tree, use this parameter. Supply fields in a comma separated list of keypaths. For example, to filter accounts list, if I wanted only the username and status, I could supply 'accounts.username,accounts.status'.")
@click.option('--debug',
              required=False,
              default="1",
              help="Set the debug level",
              type=click.Choice(sorted([str(key) for key
                                        in DEBUG_LOGGING_MAP.keys()])))
@pass_context
def cli(ctx,
        mvip=None,
        username=None,
        password=None,
        name=None,
        port=None,
        verifyssl=False,
        connectionindex=None,
        json=None,
        pickle=None,
        depth=None,
        filter_tree=None,
        debug=0,
        verbose=0,
        version='9.0'):
    """SolidFire command line interface."""
    # NOTE(jdg): This method is actually our console entry point,
    # if/when we introduce a v2 of the shell and client, we may
    # need to define a new entry point one level up that parses
    # out what version we want to uses
    ctx.debug = debug
    logging.basicConfig(
        level=logging.WARNING,
        format=('%(levelname)s in %(filename)s@%(lineno)s: %(message)s'))
    LOG.setLevel(DEBUG_LOGGING_MAP[int(debug)])

    logging.getLogger('solidfire.Element').setLevel(logging.CRITICAL)
    ctx.logger = LOG
    ctx.verbose = verbose

    # Verify that the mvip does not contain the port number:
    if mvip and ":" in mvip:
        ctx.logger.error('Please provide the port using the port parameter.')
        exit(1)

    cfg = None
    # Arguments take precedence regardless of env settings
    if mvip and username and password:
        cfg = {'mvip': mvip,
               'username': username,
               'password': password,
               'port': port,
               'url': 'https://%s:%s' % (mvip, port),
               'version': version}
        try:
            ctx.element = ElementFactory.create(cfg["mvip"],cfg["username"],cfg["password"],port=cfg["port"],version=version,verify_ssl=verifyssl)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)

    # If someone accidentally passed in an argument, but didn't specify everything, throw an error.
    elif mvip or username or password:
        LOG.error("In order to manually connect, please provide mvip, username, AND password")

    # If someone asked for a given connection or we need to default to using the connection at index 0 if it exists:
    else:
        connections = cli_utils.get_connections()
        if(connectionindex is not None):
            cfg = connections[connectionindex]
        elif(name is not None):
            filteredCfg = [connection for connection in connections if connection["name"] == name]
            if(len(filteredCfg) > 1):
                LOG.error("Your connections.csv file has become corrupted. There are two connections of the same name.")
                exit()
            if(len(filteredCfg) < 1):
                LOG.error("Could not find a connection named "+name)
                exit()
            cfg = filteredCfg[0]
        else:
            if len(connections) > 0:
                cfg = connections[0]

        # If we managed to find the connection we were looking for, we must try to establish the connection.
        if cfg is not None:
            # Finally, we need to establish our connection via elementfactory:
            try:
                ctx.element = Element(cfg["mvip"]+":"+str(cfg["port"]), cli_utils.decrypt(cfg["username"]), cli_utils.decrypt(cfg["password"]), cfg["version"], verify_ssl=verifyssl)
            except Exception as e:
                ctx.logger.error(e.__str__())
                ctx.logger.error("The connection is corrupt. Run 'sfcli connection prune' to try and remove all broken connections or use 'sfcli connection remove -n name'")
                ctx.logger.error(cfg)

    # The only time it is none is when we're asking for help or we're trying to store a connection.
    # If that's not what we're doing, we catch it later.
    if cfg is not None:
        cfg["port"] = int(cfg["port"])
        ctx.cfg = cfg
    ctx.json = json
    ctx.pickle = pickle
    ctx.depth = depth
    ctx.filter_tree = filter_tree
    ctx.verifyssl = verifyssl

if __name__ == '__main__':
    cli.main()
