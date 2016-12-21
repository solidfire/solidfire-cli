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

@cli.command('list', short_help="ListVirtualVolumes")
@click.option('--details',
              type=bool,
              required=False,
              help="Possible values:true: Include more details about each VVOL in the response.false: Include the standard level of detail about each VVOL in the response. ")
@click.option('--limit',
              type=int,
              required=False,
              help="The maximum number of virtual volumes to list. ")
@click.option('--recursive',
              type=bool,
              required=False,
              help="Possible values:true: Include information about the children of each VVOL in the response.false: Do not include information about the children of each VVOL in the response. ")
@click.option('--start_virtual_volume_id',
              type=UUID,
              required=False,
              help="The ID of the virtual volume at which to begin the list. ")
@click.option('--virtual_volume_ids',
              type=UUID,
              required=False,
              help="A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. ")
@pass_context
def list(ctx, details = None, limit = None, recursive = None, start_virtual_volume_id = None, virtual_volume_ids = None):
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset."""
    ListVirtualVolumesResult = ctx.element.list_virtual_volumes(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=start_virtual_volume_id, virtual_volume_ids=virtual_volume_ids)
    print(json.dumps(json.loads(jsonpickle.encode(ListVirtualVolumesResult)),indent=4))

