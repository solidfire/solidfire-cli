#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import json as serializer

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('list', short_help="ListAccounts")
@click.option('--json', '-j',
              is_flag=True,
              required=False,
              help="To print the full output in json format, use this flag")
@click.option('--depth', '-d',
              type=int,
              required=False,
              help="To print the output as a tree and specify the depth, use this option.")
@click.option('--table', '-t',
              required=False,
              type=click.STRING,
              help="A comma separated list of the keys you wish to include in the table.")
@click.option('--start_account_id',
              type=int,
              required=False,
              help="Starting AccountID to return. If no Account exists with this AccountID, the next Account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last Account in the previous response + 1 ")
@click.option('--limit',
              type=int,
              required=False,
              help="Maximum number of AccountInfo objects to return. ")
@pass_context
def list(ctx, start_account_id = None, limit = None, json=None, depth=None, table=None):
    """Returns the entire list of accounts, with optional paging support."""
    ListAccountsResult = ctx.element.list_accounts(start_account_id=start_account_id, limit=limit)
    #print(serializer.dumps(serializer.loads(jsonpickle.encode(ListAccountsResult)),indent=4))
    #cli_utils.print_result_as_tree(ListAccountsResult, depth=10)
    keyPaths = {"accounts":{"username": True, "status": True}}
    cli_utils.print_result_as_tree(cli_utils.filter_objects(ListAccountsResult, keyPaths), depth=10)
    #print(table)

