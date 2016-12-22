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

@cli.command('list', short_help="ListActiveVolumes")
@click.option('--start_volume_id',
              type=int,
              required=False,
              help="The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. ")
@click.option('--limit',
              type=int,
              required=False,
              help="The maximum number of volumes to return from the API. ")
@pass_context
def list(ctx, start_volume_id = None, limit = None):
    """ListActiveVolumes is used to return the list of active volumes currently in the system."""
    """The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages)."""
    ListActiveVolumesResult = ctx.element.list_active_volumes(start_volume_id=start_volume_id, limit=limit)
    cli_utils.print_result(ListActiveVolumesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

