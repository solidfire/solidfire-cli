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

@cli.command('list', short_help="ListClusterFaults")
@click.argument('exceptions', type=bool, required=False)
@click.argument('best_practices', type=bool, required=False)
@click.argument('update', type=bool, required=False)
@click.argument('fault_types', type=str, required=False)
@pass_context
def list(ctx, exceptions = None, best_practices = None, update = None, fault_types = None):
    """ListClusterFaults is used to retrieve information about any faults detected on the cluster."""
    """With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds."""
    ListClusterFaultsResult = ctx.element.list_cluster_faults(exceptions=exceptions, best_practices=best_practices, update=update, fault_types=fault_types)
    print(json.dumps(json.loads(jsonpickle.encode(ListClusterFaultsResult)),indent=4))

