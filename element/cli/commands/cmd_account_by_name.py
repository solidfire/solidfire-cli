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

@cli.command('get', short_help="GetAccountByName")
@click.option('--username',
              type=str,
              required=True,
              help="Username for the account. ")
@pass_context
def get(ctx, username):
    """Returns details about an account, given its Username."""
    GetAccountResult = ctx.element.get_account_by_name(username=username)
    cli_utils.print_result(GetAccountResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

