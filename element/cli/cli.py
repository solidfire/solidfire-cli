import logging
import logging.config
import os
import sys
import click
import csv
from pkg_resources import Requirement, resource_filename
import struct
import base64

from solidfire.factory import ElementFactory
from solidfire import Element
from element.cli import utils as cli_utils

LOG = logging.getLogger(__name__)
CONTEXT_SETTINGS = dict(auto_envvar_prefix='SOLIDFIRE', token_normalize_func=lambda x: x.lower())
DEBUG_LOGGING_MAP = {
    0: logging.CRITICAL,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG
}
CLI_VERSION = 'v1'

class Context(object):

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
            print(import_string+" failed.")
            print(e.__str__())
            return
        return mod.cli


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
