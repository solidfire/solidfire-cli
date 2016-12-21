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

@cli.command('get', short_help="GetVirtualVolumeTaskUpdate")
@click.argument('virtual_volume_task_id', type=UUID, required=True)
@click.argument('calling_virtual_volume_host_id', type=UUID, required=False)
@pass_context
def get(ctx, virtual_volume_task_id, calling_virtual_volume_host_id = None):
    """GetVirtualVolumeTaskUpdate checks the status of a VVol Async Task."""
    VirtualVolumeTaskResult = ctx.element.get_virtual_volume_task_update(virtual_volume_task_id=virtual_volume_task_id, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    print(VirtualVolumeTaskResult)

