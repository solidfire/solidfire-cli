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

@cli.command('get', short_help="GetIpmiInfo")
@click.option('--force',
              type=bool,
              required=True,
              help="")
@pass_context
def get(ctx, force):
    """GetIpmiInfo allows you to display a detailed reporting of sensors (objects) for node fans, intake and exhaust temperatures, and power supplies  that are monitored by . """
    GetIpmiInfoResult = ctx.element.get_ipmi_info(force=force)
    cli_utils.print_result(GetIpmiInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

