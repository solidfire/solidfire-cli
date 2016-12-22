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

@cli.command('remove', short_help="RemoveVirtualNetwork")
@click.option('--virtual_network_id',
              type=int,
              required=False,
              help="Network ID that identifies the virtual network to remove. ")
@click.option('--virtual_network_tag',
              type=int,
              required=False,
              help="Network Tag that identifies the virtual network to remove. ")
@pass_context
def remove(ctx, virtual_network_id = None, virtual_network_tag = None):
    """RemoveVirtualNetwork is used to remove a previously added virtual network."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note:&lt;/b&gt; This method requires either the VirtualNetworkID of the VirtualNetworkTag as a parameter, but not both."""
    RemoveVirtualNetworkResult = ctx.element.remove_virtual_network(virtual_network_id=virtual_network_id, virtual_network_tag=virtual_network_tag)
    cli_utils.print_result(RemoveVirtualNetworkResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

