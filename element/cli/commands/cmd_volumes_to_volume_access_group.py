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

@cli.command('add', short_help="AddVolumesToVolumeAccessGroup")
@click.argument('volume_access_group_id', type=int, required=True)
@click.argument('volumes', type=int, required=True)
@pass_context
def add(ctx, volume_access_group_id, volumes):
    """Add volumes to a volume access group."""
    ModifyVolumeAccessGroupResult = ctx.element.add_volumes_to_volume_access_group(volume_access_group_id=volume_access_group_id, volumes=volumes)
    print(json.dumps(json.loads(jsonpickle.encode(ModifyVolumeAccessGroupResult)),indent=4))

