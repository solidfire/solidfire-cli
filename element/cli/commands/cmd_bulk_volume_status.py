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

@cli.command('update', short_help="UpdateBulkVolumeStatus")
@click.argument('key', type=str, required=True)
@click.argument('status', type=str, required=True)
@click.argument('percent_complete', type=str, required=False)
@click.argument('message', type=str, required=False)
@click.argument('attributes', type=dict, required=False)
@pass_context
def update(ctx, key, status, percent_complete = None, message = None, attributes = None):
    """You can use UpdateBulkVolumeStatus in a script to return to the SolidFire system the status of a bulk volume job that you have started with the &quot;StartBulkVolumeRead&quot; or &quot;StartBulkVolumeWrite&quot; methods."""
    UpdateBulkVolumeStatusResult = ctx.element.update_bulk_volume_status(key=key, status=status, percent_complete=percent_complete, message=message, attributes=attributes)
    print(UpdateBulkVolumeStatusResult)

