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

@cli.command('update', short_help="UpdateBulkVolumeStatus")
@click.option('--key',
              type=str,
              required=True,
              help="The key assigned during initialization of a "StartBulkVolumeRead" or "StartBulkVolumeWrite" session. ")
@click.option('--status',
              type=str,
              required=True,
              help="The SolidFire system sets the status of the given bulk volume job.<br/> Possible values:<br/> <br/><b>running</b>: jobs that are still active. <br/><b>complete</b>: jobs that are done. failed - jobs that have failed. <br/><b>failed</b>: jobs that have failed. ")
@click.option('--percent_complete',
              type=str,
              required=False,
              help="The completed progress of the bulk volume job as a percentage. ")
@click.option('--message',
              type=str,
              required=False,
              help="Returns the status of the bulk volume job when the job has completed. ")
@click.option('--attributes',
              type=dict,
              required=False,
              help="JSON attributes  updates what is on the bulk volume job. ")
@pass_context
def update(ctx, key, status, percent_complete = None, message = None, attributes = None):
    """You can use UpdateBulkVolumeStatus in a script to return to the SolidFire system the status of a bulk volume job that you have started with the &quot;StartBulkVolumeRead&quot; or &quot;StartBulkVolumeWrite&quot; methods."""
    UpdateBulkVolumeStatusResult = ctx.element.update_bulk_volume_status(key=key, status=status, percent_complete=percent_complete, message=message, attributes=attributes)
    cli_utils.print_result(UpdateBulkVolumeStatusResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

