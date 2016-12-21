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

@cli.command('get', short_help="GetNodeHardwareInfo")
@click.option('--node_id',
              type=int,
              required=True,
              help="The ID of the node for which hardware information is being requested.  Information about a  node is returned if a   node is specified. ")
@pass_context
def get(ctx, node_id):
    """GetNodeHardwareInfo is used to return all the hardware info and status for the node specified. This generally includes manufacturers, vendors, versions, and other associated hardware identification information."""
    GetNodeHardwareInfoResult = ctx.element.get_node_hardware_info(node_id=node_id)
    print(json.dumps(json.loads(jsonpickle.encode(GetNodeHardwareInfoResult)),indent=4))

