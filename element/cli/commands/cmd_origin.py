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

@cli.command('get', short_help="GetOrigin")
@click.option('--force',
              type=bool,
              required=True,
              help="")
@pass_context
def get(ctx, force):
    """GetOrigin enables you to retrieve the origination certificate for where the node was built.NOTE: The GetOrigin method may return &quot;null&quot; if there is no origination certification."""
    GetOriginResult = ctx.element.get_origin(force=force)
    print(json.dumps(json.loads(jsonpickle.encode(GetOriginResult)),indent=4))

