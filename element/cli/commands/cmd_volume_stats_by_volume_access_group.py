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

@cli.command('list', short_help="ListVolumeStatsByVolumeAccessGroup")
@click.option('--volume_access_groups',
              type=int,
              required=False,
              help="An array of VolumeAccessGroupIDs for which volume activity is returned. If no VolumeAccessGroupID is specified, stats for all volume access groups is returned. ")
@pass_context
def list(ctx, volume_access_groups = None):
    """ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s)."""
    ListVolumeStatsByVolumeAccessGroupResult = ctx.element.list_volume_stats_by_volume_access_group(volume_access_groups=volume_access_groups)
    cli_utils.print_result(ListVolumeStatsByVolumeAccessGroupResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

