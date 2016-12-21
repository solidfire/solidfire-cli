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

@cli.command('get', short_help="GetClusterStats")
@pass_context
def get(ctx):
    """GetClusterStats is used to return high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster."""
    GetClusterStatsResult = ctx.element.get_cluster_stats()
    print(json.dumps(json.loads(jsonpickle.encode(GetClusterStatsResult)),indent=4))

