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

@cli.command('get', short_help="GetFeatureStatus")
@click.option('--feature',
              type=str,
              required=False,
              help="Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature. ")
@pass_context
def get(ctx, feature = None):
    """GetFeatureStatus allows you to retrieve the status of a cluster feature."""
    GetFeatureStatusResult = ctx.element.get_feature_status(feature=feature)
    cli_utils.print_result(GetFeatureStatusResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

