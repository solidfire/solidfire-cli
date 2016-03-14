import logging
import logging.config
import os
import sys
import click

from solidfire import solidfire_element_api as api

LOG = logging.getLogger(__name__)
CONTEXT_SETTINGS = dict(auto_envvar_prefix='SOLIDFIRE')
DEBUG_LOGGING_MAP = {
    0: logging.CRITICAL,
    1: logging.WARNING,
    2: logging.INFO,
    3: logging.DEBUG
}

VALID_FORMATS = ['table', 'raw', 'json']
DEFAULT_FORMAT = 'raw'
CLI_VERSION = 'v1'

if sys.stdout.isatty():
    DEFAULT_FORMAT = 'table'


class Context(object):

    def __init__(self):
        self.verbose = False
        self.home = os.getcwd()

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
                "solidfire.cli.commands.cmd_%s" % (name))
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
@click.option('--format',
              default=DEFAULT_FORMAT,
              help="Output format",
              type=click.Choice(VALID_FORMATS))
@click.option('--conf', '-c',
              required=False,
              default=click.get_app_dir('solidfire', force_posix=True),
              help="Config file location",
              type=click.Path(resolve_path=True))
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
@click.option('--timings',
              required=False,
              is_flag=True,
              help="Time each API call and display after results")
@pass_context
def cli(ctx,
        mvip=None,
        login=None,
        password=None,
        format='table',
        conf=None,
        timings=False,
        debug=0,
        verbose=0):
    """SolidFire command line interface."""

    # NOTE(jdg): This method is actually our console entry point,
    # if/when we introduce a v2 of the shell and client, we may
    # need to define a new entry point one level up that parses
    # out what version we want to use
    ctx.debug = debug

    logging.config.fileConfig(os.path.join(os.path.dirname(__file__), "../../logging.cfg"))

    LOG = logging.getLogger("ism")
    LOG.debug('debug')
    LOG.info('info')
    LOG.warn('warn')
    LOG.error('error')
    LOG.critical('critical')

    ctx.verbose = verbose

    # Arguments take precedence regardless of env settings
    if mvip and login and password:
        cfg = {'mvip': mvip,
               'login': login,
               'password': password,
               'port': 443,
               'url': 'https://%s:%s' % (mvip, 443)}
    else:
        cfg = {'mvip': os.environ.get('mvip', None),
               'login': os.environ.get('login', None),
               'password': os.environ.get('password', None),
               'port': os.environ.get('port', None),
               'url': os.environ.get('url', None)}
    ctx.client = api.SolidFireAPI(endpoint_dict=cfg)

     # TODO(jdg): Use the client to query the cluster for the supported version
    ctx.sfapi_endpoint_version = 7

if __name__ == '__main__':
    cli.main()
