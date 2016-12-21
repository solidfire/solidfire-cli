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

@cli.command('invoke', short_help="InvokeSFApi")
@click.argument('method', type=str, required=True)
@click.argument('parameters', type=dict, required=False)
@pass_context
def invoke(ctx, method, parameters = None):
    """This will invoke any API method supported by the SolidFire API for the version and port the connection is using."""
    """Returns a nested hashtable of key/value pairs that contain the result of the invoked method."""
    str = ctx.element.invoke_sfapi(method=method, parameters=parameters)
    print(str)

