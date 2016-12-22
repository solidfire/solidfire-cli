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

@cli.command('list', short_help="ListVirtualNetworks")
@click.option('--virtual_network_id',
              type=int,
              required=False,
              help="Network ID to filter the list for a single virtual network ")
@click.option('--virtual_network_tag',
              type=int,
              required=False,
              help="Network Tag to filter the list for a single virtual network ")
@click.option('--virtual_network_ids',
              type=int,
              required=False,
              help="NetworkIDs to include in the list. ")
@click.option('--virtual_network_tags',
              type=int,
              required=False,
              help="Network Tags to include in the list. ")
@pass_context
def list(ctx, virtual_network_id = None, virtual_network_tag = None, virtual_network_ids = None, virtual_network_tags = None):
    """ListVirtualNetworks is used to get a list of all the configured virtual networks for the cluster. This method can be used to verify the virtual network settings in the cluster."""
    """"""
    """This method does not require any parameters to be passed. But, one or more VirtualNetworkIDs or VirtualNetworkTags can be passed in order to filter the results."""
    ListVirtualNetworksResult = ctx.element.list_virtual_networks(virtual_network_id=virtual_network_id, virtual_network_tag=virtual_network_tag, virtual_network_ids=virtual_network_ids, virtual_network_tags=virtual_network_tags)
    cli_utils.print_result(ListVirtualNetworksResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

