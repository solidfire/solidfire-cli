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

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('clear', short_help="ClearClusterFaults")
@click.argument('fault_types', type=str, required=False)
@pass_context
def clear(ctx, fault_types = None):
    """ClearClusterFaults is used to clear information about both current faults that are resolved as well as faults that were previously detected and resolved can be cleared."""
    ClearClusterFaultsResult = ctx.element.clear_cluster_faults(fault_types=fault_types)
    print(ClearClusterFaultsResult)

