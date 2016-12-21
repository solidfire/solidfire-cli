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

@cli.command('set', short_help="SetConfig")
@click.argument('config', type=Config, required=True)
@pass_context
def set(ctx, config):
    """The SetConfig API method is used to set all the configuration information for the node. This includes the same information available via calls to SetClusterConfig and SetNetworkConfig in one API method."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Warning!&lt;/b&gt; Changing the 'bond-mode' on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    SetConfigResult = ctx.element.set_config(config=config)
    print(json.dumps(json.loads(jsonpickle.encode(SetConfigResult)),indent=4))

