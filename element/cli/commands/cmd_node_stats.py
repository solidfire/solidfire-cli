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

@cli.command('list', short_help="ListNodeStats")
@pass_context
def list(ctx):
    """ListNodeStats is used to return the high-level activity measurements for all nodes in a cluster."""
    ListNodeStatsResult = ctx.element.list_node_stats()
    print(json.dumps(json.loads(jsonpickle.encode(ListNodeStatsResult)),indent=4))

