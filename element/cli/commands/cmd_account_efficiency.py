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

@cli.command('get', short_help="GetAccountEfficiency")
@click.option('--account_id',
              type=int,
              required=True,
              help="Specifies the volume account for which capacity is computed. ")
@pass_context
def get(ctx, account_id):
    """GetAccountEfficiency is used to retrieve information about a volume account. Only the account given as a parameter in this API method is used to compute the capacity."""
    GetEfficiencyResult = ctx.element.get_account_efficiency(account_id=account_id)
    cli_utils.print_result(GetEfficiencyResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

