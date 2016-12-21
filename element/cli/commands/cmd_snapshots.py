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

@cli.command('list', short_help="ListSnapshots")
@click.option('--volume_id',
              type=int,
              required=False,
              help="The volume to list snapshots for. If not provided, all snapshots for all volumes are returned. ")
@pass_context
def list(ctx, volume_id = None):
    """ListSnapshots is used to return the attributes of each snapshot taken on the volume."""
    ListSnapshotsResult = ctx.element.list_snapshots(volume_id=volume_id)
    print(json.dumps(json.loads(jsonpickle.encode(ListSnapshotsResult)),indent=4))

