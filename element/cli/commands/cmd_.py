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

@cli.command('shutdown', short_help="Shutdown")
@click.argument('option', type=str, required=True)
@pass_context
def shutdown(ctx, option):
    """The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method, login in to the MIP for the pending node and enter the &quot;shutdown&quot; method with either the &quot;restart&quot; or &quot;halt&quot; options in the following table."""
    ShutdownResult = ctx.element.shutdown(option=option)
    print(json.dumps(json.loads(jsonpickle.encode(ShutdownResult)),indent=4))

