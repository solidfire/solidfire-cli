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

@cli.command('list', short_help="ListVolumeStatsByAccount")
@pass_context
def list(ctx):
    """ListVolumeStatsByAccount returns high-level activity measurements for every account."""
    """Values are summed from all the volumes owned by the account."""
    ListVolumeStatsByAccountResult = ctx.element.list_volume_stats_by_account()
    print(json.dumps(json.loads(jsonpickle.encode(ListVolumeStatsByAccountResult)),indent=4))

