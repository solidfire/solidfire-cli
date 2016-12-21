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

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('list', short_help="ListVolumesForAccount")
@click.argument('account_id', type=int, required=True)
@click.argument('start_volume_id', type=int, required=False)
@click.argument('limit', type=int, required=False)
@pass_context
def list(ctx, account_id, start_volume_id = None, limit = None):
    """ListVolumesForAccount returns the list of active AND (pending) deleted volumes for an account."""
    ListVolumesForAccountResult = ctx.element.list_volumes_for_account(account_id=account_id, start_volume_id=start_volume_id, limit=limit)
    print(ListVolumesForAccountResult)

