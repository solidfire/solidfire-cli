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

@cli.command('get', short_help="GetClusterVersionInfo")
@pass_context
def get(ctx):
    """Return information about the Element software version running on each node in the cluster."""
    """Information about the nodes that are currently in the process of upgrading software is also returned."""
    GetClusterVersionInfoResult = ctx.element.get_cluster_version_info()
    print(json.dumps(json.loads(jsonpickle.encode(GetClusterVersionInfoResult)),indent=4))

