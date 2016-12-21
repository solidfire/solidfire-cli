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

@cli.command('prepare', short_help="PrepareVirtualSnapshot")
@click.option('--virtual_volume_id',
              type=UUID,
              required=True,
              help="The ID of the Virtual Volume to clone. ")
@click.option('--name',
              type=str,
              required=False,
              help="The name for the newly-created volume. ")
@click.option('--writable_snapshot',
              type=bool,
              required=False,
              help="Will the snapshot be writable? ")
@click.option('--calling_virtual_volume_host_id',
              type=UUID,
              required=False,
              help="")
@pass_context
def prepare(ctx, virtual_volume_id, name = None, writable_snapshot = None, calling_virtual_volume_host_id = None):
    """PrepareVirtualSnapshot is used to set up VMware Virtual Volume snapshot."""
    PrepareVirtualSnapshotResult = ctx.element.prepare_virtual_snapshot(virtual_volume_id=virtual_volume_id, name=name, writable_snapshot=writable_snapshot, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    print(json.dumps(json.loads(jsonpickle.encode(PrepareVirtualSnapshotResult)),indent=4))

