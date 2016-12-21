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

@cli.command('list', short_help="ListVolumeStatsByVolumeAccessGroup")
@click.argument('volume_access_groups', type=int, required=False)
@pass_context
def list(ctx, volume_access_groups = None):
    """ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s)."""
    ListVolumeStatsByVolumeAccessGroupResult = ctx.element.list_volume_stats_by_volume_access_group(volume_access_groups=volume_access_groups)
    print(ListVolumeStatsByVolumeAccessGroupResult)

