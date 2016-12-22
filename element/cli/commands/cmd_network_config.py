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

@cli.command('set', short_help="SetNetworkConfig")
@click.option('--network',
              type=Network,
              required=True,
              help="Objects that will be changed for the node network settings. ")
@pass_context
def set(ctx, network):
    """The &quot;SetNetworkConfig&quot; method is used to set the network configuration for a node. To see the states in which these objects can be modified, see &quot;Network Object for 1G and 10G Interfaces&quot; on page 109 of the Element API. To display the current network settings for a node, run the &quot;GetNetworkConfig&quot; method."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;WARNING!&lt;/b&gt; Changing the &quot;bond-mode&quot; on a node can cause a temporary loss of network connectivity. Caution should be taken when using this method."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    SetNetworkConfigResult = ctx.element.set_network_config(network=network)
    cli_utils.print_result(SetNetworkConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

