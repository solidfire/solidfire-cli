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

@cli.command('invoke', short_help="InvokeSFApi")
@click.option('--method',
              type=str,
              required=True,
              help="The name of the method to invoke. This is case sensitive. ")
@click.option('--parameters',
              type=dict,
              required=False,
              help="An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked. ")
@pass_context
def invoke(ctx, method, parameters = None):
    """This will invoke any API method supported by the SolidFire API for the version and port the connection is using."""
    """Returns a nested hashtable of key/value pairs that contain the result of the invoked method."""
    str = ctx.element.invoke_sfapi(method=method, parameters=parameters)
    cli_utils.print_result(str, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

