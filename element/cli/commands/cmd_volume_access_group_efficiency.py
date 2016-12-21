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

@cli.command('get', short_help="GetVolumeAccessGroupEfficiency")
@click.argument('volume_access_group_id', type=int, required=True)
@pass_context
def get(ctx, volume_access_group_id):
    """GetVolumeAccessGroupEfficiency is used to retrieve efficiency information about a volume access group. Only the volume access group provided as parameters in this API method is used to compute the capacity."""
    GetEfficiencyResult = ctx.element.get_volume_access_group_efficiency(volume_access_group_id=volume_access_group_id)
    print(json.dumps(json.loads(jsonpickle.encode(GetEfficiencyResult)),indent=4))

