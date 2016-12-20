import click

from element.cli import utils as cli_utils
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils


@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client


@cli.command('list', short_help='List accounts.')
@pass_context
def list(ctx):
    """List Accounts."""
    accounts = ctx.sfapi.list_accounts()
    if ctx.verbose == 0:
        key_list = ['username', 'status', 'volumes', 'accountID']
    else:
        key_list = ['username', 'status', 'initiatorSecret', 'targetSecret',
                'volumes', 'attributes', 'accountID']
    cli_utils.print_list(accounts, key_list)


@cli.command('delete', short_help='Deletes an account(s).')
@click.argument('accounts',
                nargs=-1)
@pass_context
def delete(ctx, accounts, purge):
    """Delete the specified accountID(s)."""
    for acct_id in accounts:
        try:
            ctx.sfapi.remove_account(acct_id)
        except SolidFireRequestException as ex:
            ctx.log(ex.msg[1]['error']['message'])


@cli.command('show', short_help='Show details for the specified account')
@click.argument('account-id',
                type=int,
                required=True)
def show(ctx, account_id):
    account = ctx.sfapi.get_account_by_id(account_id)['account']
    cli_utils.print_dict(account)


@cli.command('add', short_help='Add new account to Cluster')
@click.argument('user-name',
                required=True)
@click.option('--intiator-secret',
              default=None,
              help='Chap Initiator Secret to assign to account.')
@click.option('--target-secret',
              default=None,
              help='Chap Target Secret to assign to account.')
@click.option('--attributes',
              default=None,
              help='Key Value pairs to set account attributes '
                   '(--attributes attrName=val1,attrName2=val2...)')
def add(ctx, user_name,
        initiator_secret=None, target_secret=None,
        attributes=None):
    """Creates <count> clones of volume specified by volume-id."""
    if attributes:
        attributes = utils.kv_string_to_dict(attributes)
    new_account_id = ctx.sfapi.add_account(user_name, initiator_secret,
                                           target_secret, attributes)
    account = ctx.sfapi.get_account_by_id(new_account_id)['account']
    cli_utils.print_dict(account)
