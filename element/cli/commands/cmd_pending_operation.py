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

@cli.command('get', short_help="GetPendingOperation")
@pass_context
def get(ctx):
    """GetPendingOperation is used to detect an operation on a node that is currently in progress. This method can also be used to report back when an operation has completed.&lt;br/&gt;"""
    """&lt;br/&gt;"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    GetPendingOperationResult = ctx.element.get_pending_operation()
    cli_utils.print_result(GetPendingOperationResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

