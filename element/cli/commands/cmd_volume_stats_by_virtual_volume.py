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

@cli.command('list', short_help="ListVolumeStatsByVirtualVolume")
@click.option('--virtual_volume_ids',
              type=UUID,
              required=False,
              help="A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. ")
@pass_context
def list(ctx, virtual_volume_ids = None):
    """ListVolumeStatsByVirtualVolume enables you to list statistics for volumes, sorted by virtual volumes."""
    ListVolumeStatsByVirtualVolumeResult = ctx.element.list_volume_stats_by_virtual_volume(virtual_volume_ids=virtual_volume_ids)
    cli_utils.print_result(ListVolumeStatsByVirtualVolumeResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

