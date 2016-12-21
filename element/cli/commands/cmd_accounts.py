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
import json

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('list', short_help="ListAccounts")
@click.argument('start_account_id', type=int, required=False)
@click.argument('limit', type=int, required=False)
@pass_context
def list(ctx, start_account_id = None, limit = None):
    """Returns the entire list of accounts, with optional paging support."""
    ListAccountsResult = ctx.element.list_accounts(start_account_id=start_account_id, limit=limit)
    cli_utils.print_result_as_tree(ListAccountsResult)
    #print(json.dumps(json.loads(jsonpickle.encode(ListAccountsResult)),indent=4))

