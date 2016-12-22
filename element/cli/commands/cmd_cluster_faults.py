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
@click.option('--exceptions',
              type=bool,
              required=False,
              help="")
@click.option('--best_practices',
              type=bool,
              required=False,
              help="Include faults triggered by sub-optimal system configuration. Possible values: true, false ")
@click.option('--update',
              type=bool,
              required=False,
              help="")
@click.option('--fault_types',
              type=str,
              required=False,
              help="Determines the types of faults returned: current: List active, unresolved faults. <b>resolved</b>: List faults that were previously detected and resolved. <b>all</b>: (Default) List both current and resolved faults. You can see the fault status in the 'resolved' field of the Cluster Fault object. ")
@pass_context
def list(ctx, exceptions = None, best_practices = None, update = None, fault_types = None):
    """ListClusterFaults is used to retrieve information about any faults detected on the cluster."""
    """With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds."""
    ListClusterFaultsResult = ctx.element.list_cluster_faults(exceptions=exceptions, best_practices=best_practices, update=update, fault_types=fault_types)
    cli_utils.print_result(ListClusterFaultsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

