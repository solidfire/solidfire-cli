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
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import simplejson
from solidfire.models import *
from uuid import UUID
from element import exceptions


@click.group()
@pass_context
def cli(ctx):
    """Add GetByID GetByName GetEfficiency List Modify Remove """

@cli.command('Add', short_help="""Used to add a new account to the system. New volumes can be created under the new account. The CHAP settings specified for the account applies to all volumes owned by the account. """)
@click.option('--username',
              type=str,
              required=True,
              help="""Unique username for this account. (May be 1 to 64 characters in length). """)
@click.option('--initiator_secret',
              type=str,
              required=False,
              help="""CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable. The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret. <br/><br/> If not specified, a random secret is created. """)
@click.option('--target_secret',
              type=str,
              required=False,
              help="""CHAP secret to use for the target (mutual CHAP authentication). Should be 12-16 characters long and impenetrable. The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret. <br/><br/> If not specified, a random secret is created. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Add(ctx,
           username,
           initiator_secret = None,
           target_secret = None,
           attributes = None):
    """Used to add a new account to the system."""
    """New volumes can be created under the new account."""
    """The CHAP settings specified for the account applies to all volumes owned by the account."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    AddAccountResult = ctx.element.add_account(username=username, initiator_secret=initiator_secret, target_secret=target_secret, attributes=attributes)
    cli_utils.print_result(AddAccountResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetByID', short_help="""Returns details about an account, given its AccountID. """)
@click.option('--account_id',
              type=int,
              required=True,
              help="""Specifies the account for which details are gathered. """)
@pass_context
def GetByID(ctx,
           account_id):
    """Returns details about an account, given its AccountID."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetAccountResult = ctx.element.get_account_by_id(account_id=account_id)
    cli_utils.print_result(GetAccountResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetByName', short_help="""Returns details about an account, given its Username. """)
@click.option('--username',
              type=str,
              required=True,
              help="""Username for the account. """)
@pass_context
def GetByName(ctx,
           username):
    """Returns details about an account, given its Username."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetAccountResult = ctx.element.get_account_by_name(username=username)
    cli_utils.print_result(GetAccountResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetEfficiency', short_help="""GetAccountEfficiency is used to retrieve information about a volume account. Only the account given as a parameter in this API method is used to compute the capacity. """)
@click.option('--account_id',
              type=int,
              required=True,
              help="""Specifies the volume account for which capacity is computed. """)
@pass_context
def GetEfficiency(ctx,
           account_id):
    """GetAccountEfficiency is used to retrieve information about a volume account. Only the account given as a parameter in this API method is used to compute the capacity."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetEfficiencyResult = ctx.element.get_account_efficiency(account_id=account_id)
    cli_utils.print_result(GetEfficiencyResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""Returns the entire list of accounts, with optional paging support. """)
@click.option('--start_account_id',
              type=int,
              required=False,
              help="""Starting AccountID to return. If no Account exists with this AccountID, the next Account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last Account in the previous response + 1 """)
@click.option('--limit',
              type=int,
              required=False,
              help="""Maximum number of AccountInfo objects to return. """)
@pass_context
def List(ctx,
           start_account_id = None,
           limit = None):
    """Returns the entire list of accounts, with optional paging support."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListAccountsResult = ctx.element.list_accounts(start_account_id=start_account_id, limit=limit)
    cli_utils.print_result(ListAccountsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Modify', short_help="""Used to modify an existing account. When locking an account, any existing connections from that account are immediately terminated. When changing CHAP settings, any existing connections continue to be active, and the new CHAP values are only used on subsequent connection or reconnection. """)
@click.option('--account_id',
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
@click.option('--initiator_secret',
              type=str,
              required=False,
              help="""CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable. """)
@click.option('--target_secret',
              type=str,
              required=False,
              help="""CHAP secret to use for the target (mutual CHAP authentication). Should be 12-16 characters long and impenetrable. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Modify(ctx,
           account_id,
           username = None,
           status = None,
           initiator_secret = None,
           target_secret = None,
           attributes = None):
    """Used to modify an existing account."""
    """When locking an account, any existing connections from that account are immediately terminated."""
    """When changing CHAP settings, any existing connections continue to be active,"""
    """and the new CHAP values are only used on subsequent connection or reconnection."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ModifyAccountResult = ctx.element.modify_account(account_id=account_id, username=username, status=status, initiator_secret=initiator_secret, target_secret=target_secret, attributes=attributes)
    cli_utils.print_result(ModifyAccountResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Remove', short_help="""Used to remove an existing account. All Volumes must be deleted and purged on the account before it can be removed. If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes. """)
@click.option('--account_id',
              type=int,
              required=True,
              help="""AccountID for the account to remove. """)
@pass_context
def Remove(ctx,
           account_id):
    """Used to remove an existing account."""
    """All Volumes must be deleted and purged on the account before it can be removed."""
    """If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    RemoveAccountResult = ctx.element.remove_account(account_id=account_id)
    cli_utils.print_result(RemoveAccountResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

