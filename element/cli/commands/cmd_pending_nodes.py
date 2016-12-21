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

@cli.command('list', short_help="ListPendingNodes")
@pass_context
def list(ctx):
    """Gets the list of pending nodes."""
    """Pending nodes are running and configured to join the cluster, but have not been added via the AddNodes method."""
    ListPendingNodesResult = ctx.element.list_pending_nodes()
    print(ListPendingNodesResult)

