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

@cli.command('get', short_help="GetClusterCapacity")
@pass_context
def get(ctx):
    """Return the high-level capacity measurements for an entire cluster."""
    """The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface."""
    GetClusterCapacityResult = ctx.element.get_cluster_capacity()
    print(json.dumps(json.loads(jsonpickle.encode(GetClusterCapacityResult)),indent=4))

