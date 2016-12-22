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

@cli.command('list', short_help="ListVirtualVolumeTasks")
@click.option('--virtual_volume_task_ids',
              type=UUID,
              required=False,
              help="")
@pass_context
def list(ctx, virtual_volume_task_ids = None):
    """ListVirtualVolumeTasks returns a list of VVol Async Tasks."""
    ListVirtualVolumeTasksResult = ctx.element.list_virtual_volume_tasks(virtual_volume_task_ids=virtual_volume_task_ids)
    cli_utils.print_result(ListVirtualVolumeTasksResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

