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

@cli.command('restart', short_help="RestartNetworking")
@click.option('--force',
              type=bool,
              required=True,
              help="The "force" parameter must be included on this method to successfully restart the networking. ")
@pass_context
def restart(ctx, force):
    """The RestartNetworking API method is used to restart the networking services on a node.WARNING! This method restarts all networking services on a node, causing temporary loss of networking connectivity. Exercise caution when using this method."""
    dict = ctx.element.restart_networking(force=force)
    cli_utils.print_result(dict, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

