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

@cli.command('list', short_help="ListVolumeAccessGroups")
@click.option('--start_volume_access_group_id',
              type=int,
              required=False,
              help="The lowest VolumeAccessGroupID to return. This can be useful for paging. If unspecified, there is no lower limit (implicitly 0). ")
@click.option('--limit',
              type=int,
              required=False,
              help="The maximum number of results to return. This can be useful for paging. ")
@pass_context
def list(ctx, start_volume_access_group_id = None, limit = None):
    """ListVolumeAccessGroups is used to return information about the volume access groups that are currently in the system."""
    ListVolumeAccessGroupsResult = ctx.element.list_volume_access_groups(start_volume_access_group_id=start_volume_access_group_id, limit=limit)
    print(json.dumps(json.loads(jsonpickle.encode(ListVolumeAccessGroupsResult)),indent=4))

