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

@cli.command('set', short_help="SetLoginSessionInfo")
@click.option('--timeout',
              type=str,
              required=True,
              help="Cluster authentication expiration period. Formatted in HH:mm:ss. For example: 01:30:00, 00:90:00, and 00:00:5400 can all be used to equal a 90 minute timeout period. Default is 30 minutes. ")
@pass_context
def set(ctx, timeout):
    """SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed."""
    SetLoginSessionInfoResult = ctx.element.set_login_session_info(timeout=timeout)
    cli_utils.print_result(SetLoginSessionInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

