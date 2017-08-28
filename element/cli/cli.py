import logging
import logging.config
import os
import sys
import click
import click.core
import click.testing
import copy
import csv
import pkg_resources
from pkg_resources import Requirement, resource_filename
import struct
import base64

logging.basicConfig(
    level=logging.WARNING,
    format=('%(asctime)s - %(name)s: in %(filename)s at %(lineno)s - %(levelname)s: %(message)s'))
LOG = logging.getLogger(__name__)
CONTEXT_SETTINGS = dict(auto_envvar_prefix='SOLIDFIRE', token_normalize_func=lambda x: x.lower())
HELP_STRING = """Welcome to the SolidFire Command Line Interface """ + pkg_resources.require("solidfire-cli")[0].version + """.
    
    For more information about how to use this, see the readme here: https://github.com/solidfire/solidfire-cli."""

DEBUG_LOGGING_MAP = {
    0: logging.CRITICAL,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG
}
CLI_VERSION = 'v1'
click.disable_unicode_literals_warning = True


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
        self.timeout = 30
        self.nocache = None

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
        # here. These will be expected in the next iteration. Note well, by
        # the time we're handling regular parameters, state.subparameters=[].
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
                    #if self.required and self.is_sub_parameter:
                    #    raise click.BadParameter(self.name+" is a required member of its parameter group. Please provide it inline after the associated superparameter.")
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

@click.command(cls=SolidFireCLI, context_settings=CONTEXT_SETTINGS, help=HELP_STRING)
@click.option('--mvip', '-m',
              default=None,
              help="SolidFire MVIP.",
              required=False)
@click.option('--username', '-u',
              default=None,
              help="SolidFire Cluster username.",
              required=False)
@click.option('--password', '-p',
              default=None,
              help="SolidFire cluster password.",
              required=False)
@click.option('--version', '-v',
              default=None,
              help='The version you would like to connect on.',
              required=False)
@click.option('--port', '-q',
              default=443,
              help="The port number on which you wish to connect.",
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
@click.option('--timeout', '-t',
              default=30,
              help="The request timeout in seconds.",
              required=False)
@click.option('--json', '-j',
              is_flag=True,
              required=False,
              help="To print the full output in json format, use this flag.")
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
@click.option('--nocache',
              required=False,
              is_flag=True,
              help="If you do not wish to cache the connection, supply this flag.")
@pass_context
def cli(ctx,
        mvip=None,
        username=None,
        password=None,
        name=None,
        port=None,
        verifyssl=False,
        timeout=30,
        connectionindex=None,
        json=None,
        pickle=None,
        depth=None,
        filter_tree=None,
        debug=0,
        verbose=0,
        version=None,
        nocache=None):
    """Welcome to the SolidFire command line interface! For more information about how to use this, see the readme here: https://github.com/solidfire/solidfire-cli"""
    # NOTE(jdg): This method is actually our console entry point,
    # if/when we introduce a v2 of the shell and client, we may
    # need to define a new entry point one level up that parses
    # out what version we want to uses

    ctx.debug = debug
    LOG.setLevel(DEBUG_LOGGING_MAP[int(debug)])

    element_logger = logging.getLogger('solidfire.Element')
    element_logger.setLevel(DEBUG_LOGGING_MAP[int(debug)])
    for h in element_logger.handlers:
        element_logger.removeHandler(h)
    #if element_logger.hasHandlers():
    #    element_logger.handlers.clear()
    ctx.logger = LOG
    ctx.verbose = verbose
    ctx.username = username
    ctx.password = password
    ctx.name = name
    ctx.port = port
    ctx.connectionindex = connectionindex
    ctx.mvip = mvip
    ctx.json = json
    ctx.pickle = pickle
    ctx.depth = depth
    ctx.filter_tree = filter_tree
    ctx.verifyssl = verifyssl
    ctx.timeout = timeout
    ctx.version = version
    ctx.nocache = nocache

if __name__ == '__main__':
    """
    #pass_context()
    #ctx = click.globals.get_current_context()
    runner = click.testing.CliRunner()
    runner.invoke(element_cli.cli,
                  ["account", "list"])
    runner.invoke(element_cli.cli,
                  ['--mvip', "10.117.61.44", "--login", "admin", "--password", "admin", "--name", "b", "Connection",
                   "PushConnection"])"""
    cli.main()
