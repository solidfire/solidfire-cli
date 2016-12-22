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

@cli.command('list', short_help="ListDriveHardware")
@click.option('--force',
              type=bool,
              required=True,
              help="To run this command, the force parameter must be set to true. ")
@pass_context
def list(ctx, force):
    """ListDriveHardware returns all the drives connected to a node. Use this method on the cluster to return drive hardware information for all the drives on all nodes."""
    ListDriveHardwareResult = ctx.element.list_drive_hardware(force=force)
    cli_utils.print_result(ListDriveHardwareResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

