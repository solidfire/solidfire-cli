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

@cli.command('get', short_help="GetAsyncResult")
@click.option('--async_handle',
              type=int,
              required=True,
              help="A value that was returned from the original asynchronous method call. ")
@pass_context
def get(ctx, async_handle):
    """Used to retrieve the result of asynchronous method calls."""
    """Some method calls are long running and do not complete when the initial response is sent."""
    """To obtain the result of the method call, polling with GetAsyncResult is required."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,"""
    """but the actual data returned for the operation depends on the original method call and the return data is documented with each method."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """The result for a completed asynchronous method call can only be retrieved once."""
    """Once the final result has been returned, later attempts returns an error."""
    GetAsyncResultResult = ctx.element.get_async_result(async_handle=async_handle)
    cli_utils.print_result(GetAsyncResultResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

