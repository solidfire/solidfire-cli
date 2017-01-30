#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli import parser
from element.cli.cli import pass_context
from element import utils
import jsonpickle
import simplejson
from solidfire.models import *
from solidfire.custom.models import *
from uuid import UUID
from element import exceptions
from solidfire import common


@click.group()
@pass_context
def cli(ctx):
    """getefficiency list getbyid getbyname remove modify add """

@cli.command('getefficiency', short_help="""GetAccountEfficiency is used to retrieve information about a volume account. Only the account given as a parameter in this API method is used to compute the capacity. """)
@click.option('--accountid',
              type=int,
              required=True,
              help="""Specifies the volume account for which capacity is computed. """)
@pass_context
def getefficiency(ctx,
           accountid):
    """GetAccountEfficiency is used to retrieve information about a volume account. Only the account given as a parameter in this API method is used to compute the capacity."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""accountid = """+str(accountid)+""";"""+"")
    try:
        _GetEfficiencyResult = ctx.element.get_account_efficiency(account_id=accountid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""Returns the entire list of accounts, with optional paging support. """)
@click.option('--startaccountid',
              type=int,
              required=False,
              help="""Starting AccountID to return. If no Account exists with this AccountID, the next Account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last Account in the previous response + 1 """)
@click.option('--limit',
              type=int,
              required=False,
              help="""Maximum number of AccountInfo objects to return. """)
@pass_context
def list(ctx,
           startaccountid = None,
           limit = None):
    """Returns the entire list of accounts, with optional paging support."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""startaccountid = """+str(startaccountid)+""";"""+"""limit = """+str(limit)+""";"""+"")
    try:
        _ListAccountsResult = ctx.element.list_accounts(start_account_id=startaccountid, limit=limit)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListAccountsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getbyid', short_help="""Returns details about an account, given its AccountID. """)
@click.option('--accountid',
              type=int,
              required=True,
              help="""Specifies the account for which details are gathered. """)
@pass_context
def getbyid(ctx,
           accountid):
    """Returns details about an account, given its AccountID."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""accountid = """+str(accountid)+""";"""+"")
    try:
        _GetAccountResult = ctx.element.get_account_by_id(account_id=accountid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getbyname', short_help="""Returns details about an account, given its Username. """)
@click.option('--username',
              type=str,
              required=True,
              help="""Username for the account. """)
@pass_context
def getbyname(ctx,
           username):
    """Returns details about an account, given its Username."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""username = """+str(username)+""";"""+"")
    try:
        _GetAccountResult = ctx.element.get_account_by_name(username=username)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""Used to remove an existing account. All Volumes must be deleted and purged on the account before it can be removed. If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes. """)
@click.option('--accountid',
              type=int,
              required=True,
              help="""AccountID for the account to remove. """)
@pass_context
def remove(ctx,
           accountid):
    """Used to remove an existing account."""
    """All Volumes must be deleted and purged on the account before it can be removed."""
    """If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""accountid = """+str(accountid)+""";"""+"")
    try:
        _RemoveAccountResult = ctx.element.remove_account(account_id=accountid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_RemoveAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""Used to modify an existing account. When locking an account, any existing connections from that account are immediately terminated. When changing CHAP settings, any existing connections continue to be active, and the new CHAP values are only used on subsequent connection or reconnection. """)
@click.option('--accountid',
              type=int,
              required=True,
              help="""AccountID for the account to modify. """)
@click.option('--username',
              type=str,
              required=False,
              help="""Change the username of the account to this value. """)
@click.option('--status',
              type=str,
              required=False,
              help="""Status of the account. """)
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable. """)
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""CHAP secret to use for the target (mutual CHAP authentication). Should be 12-16 characters long and impenetrable. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def modify(ctx,
           accountid,
           username = None,
           status = None,
           initiatorsecret = None,
           targetsecret = None,
           attributes = None):
    """Used to modify an existing account."""
    """When locking an account, any existing connections from that account are immediately terminated."""
    """When changing CHAP settings, any existing connections continue to be active,"""
    """and the new CHAP values are only used on subsequent connection or reconnection."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""accountid = """+str(accountid)+""";"""+"""username = """+str(username)+""";"""+"""status = """+str(status)+""";"""+"""initiatorsecret = """+str(initiatorsecret)+""";"""+"""targetsecret = """+str(targetsecret)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _ModifyAccountResult = ctx.element.modify_account(account_id=accountid, username=username, status=status, initiator_secret=initiatorsecret, target_secret=targetsecret, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('add', short_help="""Used to add a new account to the system. New volumes can be created under the new account. The CHAP settings specified for the account applies to all volumes owned by the account. """)
@click.option('--username',
              type=str,
              required=True,
              help="""Unique username for this account. (May be 1 to 64 characters in length). """)
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable. The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.  If not specified, a random secret is created. """)
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""CHAP secret to use for the target (mutual CHAP authentication). Should be 12-16 characters long and impenetrable. The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.  If not specified, a random secret is created. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def add(ctx,
           username,
           initiatorsecret = None,
           targetsecret = None,
           attributes = None):
    """Used to add a new account to the system."""
    """New volumes can be created under the new account."""
    """The CHAP settings specified for the account applies to all volumes owned by the account."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""username = """+str(username)+""";"""+"""initiatorsecret = """+str(initiatorsecret)+""";"""+"""targetsecret = """+str(targetsecret)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _AddAccountResult = ctx.element.add_account(username=username, initiator_secret=initiatorsecret, target_secret=targetsecret, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_AddAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

