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

@cli.command('reset', short_help="ResetNode")
@click.option('--build',
              type=str,
              required=True,
              help="Used to specify the URL to a remote Element software image to which the node will be reset. ")
@click.option('--force',
              type=bool,
              required=True,
              help="The force parameter must be included in order to successfully reset the node. ")
@click.option('--option',
              type=str,
              required=True,
              help="Used to enter specifications for running the reset operation. ")
@pass_context
def reset(ctx, build, force, option):
    """Allows you to reset a node to the SolidFire factory settings. All data will be deleted from the node when you call this method. A node participating in a cluster cannot be reset."""
    ResetNodeResult = ctx.element.reset_node(build=build, force=force, option=option)
    print(json.dumps(json.loads(jsonpickle.encode(ResetNodeResult)),indent=4))

