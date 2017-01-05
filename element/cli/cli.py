import logging
import logging.config
import os
import sys
import click
import csv
from solidfire.factory import ElementFactory

from element import solidfire_element_api as api
from element import exceptions

from solidfire.factory import ElementFactory

LOG = logging.getLogger(__name__)
CONTEXT_SETTINGS = dict(auto_envvar_prefix='SOLIDFIRE')
DEBUG_LOGGING_MAP = {
    0: logging.CRITICAL,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG
}
CLI_VERSION = 'v1'

if sys.stdout.isatty():
    DEFAULT_FORMAT = 'table'


class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()
        self.connections = dict()
        self.element = None
        self.depth = None
        self.json = None
        self.filter_tree = None
        self.table = None

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
                "element.cli.commands.cmd_%s" % (name))
            mod = __import__(import_string, None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=SolidFireCLI, context_settings=CONTEXT_SETTINGS)
@click.option('--mvip', '-m',
              default=None,
              help="SolidFire MVIP",
              required=False)
@click.option('--login', '-l',
              default=None,
              help="SolidFire Cluster login",
              required=False)
@click.option('--password', '-p',
              default=None,
              help="SolidFire cluster password",
              required=False)
@click.option('--name',
              default = None,
              help="The connection name for later reference (-n)",
              required=False)
@click.option('--connectionIndex', '-c',
              default=None,
              type=click.INT,
              help="The index of the connection you wish to use in connections.csv. You can use this if you have previously stored away a connection.",
              required=False)
@click.option('--connectionName', '-n',
              default=None,
              type=click.STRING,
              help="The name of the connection you wish to use in connections.csv. You can use this if you have previously stored away a connection.",
              required=False)
@click.option('--json', '-j',
              is_flag=True,
              required=False,
              help="To print the full output in json format, use this flag")
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
              default=None,
              help="Set the debug level",
              type=click.Choice(sorted([str(key) for key
                                        in DEBUG_LOGGING_MAP.keys()])))
@click.option('--verbose', '-v',
              help="Provide extra output info",
              type=click.IntRange(0, 3, clamp=True),
              count=True)
@pass_context
def cli(ctx,
        mvip=None,
        login=None,
        password=None,
        name=None,
        connectionindex=None,
        connectionname=None,
        json=None,
        depth=None,
        filter_tree=None,
        debug=0,
        verbose=0):
    """SolidFire command line interface."""

    # NOTE(jdg): This method is actually our console entry point,
    # if/when we introduce a v2 of the shell and client, we may
    # need to define a new entry point one level up that parses
    # out what version we want to use
    ctx.debug = debug
    logging.basicConfig(
        level=logging.WARNING,
        format=('%(levelname)s in %(filename)s@%(lineno)s: %(message)s'))
    ctx.verbose = verbose

    connections_dirty = False
    cfg = None

    connectionsCsvLocation = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "connections.csv")
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))

    # Arguments take precedence regardless of env settings
    if mvip and login and password:
        cfg = {'mvip': mvip,
               'login': login,
               'password': password,
               'name': name,
               'port': 443,
               'url': 'https://%s:%s' % (mvip, 443)}
        ctx.element = ElementFactory.create(cfg["mvip"],cfg["login"],cfg["password"],port=cfg["port"])
    # If someone accidentally passed in an argument, but didn't specify everything, throw an error.
    elif mvip or login or password:
        raise exceptions.SolidFireConnectionException("In order to manually connect, please provide mvip, login, AND password")
    else:
        if(connectionindex is not None):
            cfg = connections[connectionindex]
        elif(connectionname is not None):
            filteredCfg = [connection for connection in connections if connection["name"] == connectionname]
            if(len(filteredCfg) > 1):
                raise exceptions.SolidFireUsageException("Your connections.csv file has become corrupted. There are two connections of the same name.")
            if(len(filteredCfg) < 1):
                raise exceptions.SolidFireUsageException("Could not find a connection named "+connectionname)
            cfg = filteredCfg[0]
    if cfg is not None:
        cfg["port"] = int(cfg["port"])
        # Finaly, we need to establish our connection via elementfactory:
        ctx.element = ElementFactory.create(cfg["mvip"],cfg["login"],cfg["password"],9.0,port=cfg["port"])
        ctx.client = api.SolidFireAPI(endpoint_dict=cfg)

         # TODO(jdg): Use the client to query the cluster for the supported version
        ctx.sfapi_endpoint_version = 7
        ctx.element = ElementFactory.create(cfg["mvip"],cfg["login"],cfg["password"],port=cfg["port"])
        ctx.cfg = cfg
        ctx.json = json
        ctx.depth = depth
        ctx.filter_tree = filter_tree
        print(type(ctx))

if __name__ == '__main__':
    cli.main()
