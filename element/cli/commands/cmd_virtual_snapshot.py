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

@cli.command('prepare', short_help="PrepareVirtualSnapshot")
@click.argument('virtual_volume_id', type=UUID, required=True)
@click.argument('name', type=str, required=False)
@click.argument('writable_snapshot', type=bool, required=False)
@click.argument('calling_virtual_volume_host_id', type=UUID, required=False)
@pass_context
def prepare(ctx, virtual_volume_id, name = None, writable_snapshot = None, calling_virtual_volume_host_id = None):
    """PrepareVirtualSnapshot is used to set up VMware Virtual Volume snapshot."""
    PrepareVirtualSnapshotResult = ctx.element.prepare_virtual_snapshot(virtual_volume_id=virtual_volume_id, name=name, writable_snapshot=writable_snapshot, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    print(PrepareVirtualSnapshotResult)

