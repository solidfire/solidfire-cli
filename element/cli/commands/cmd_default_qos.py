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

@cli.command('set', short_help="SetDefaultQoS")
@click.argument('min_iops', type=int, required=False)
@click.argument('max_iops', type=int, required=False)
@click.argument('burst_iops', type=int, required=False)
@pass_context
def set(ctx, min_iops = None, max_iops = None, burst_iops = None):
    """SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or IOPS) for all volumes not yet created."""
    SetDefaultQoSResult = ctx.element.set_default_qos(min_iops=min_iops, max_iops=max_iops, burst_iops=burst_iops)
    print(json.dumps(json.loads(jsonpickle.encode(SetDefaultQoSResult)),indent=4))

