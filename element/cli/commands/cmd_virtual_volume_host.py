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

@cli.command('create', short_help="CreateVirtualVolumeHost")
@click.option('--virtual_volume_host_id',
              type=UUID,
              required=True,
              help="The GUID of the ESX host. ")
@click.option('--cluster_id',
              type=UUID,
              required=True,
              help="The GUID of the ESX Cluster. ")
@click.option('--initiator_names',
              type=str,
              required=False,
              help="")
@click.option('--visible_protocol_endpoint_ids',
              type=UUID,
              required=False,
              help="A list of PEs the host is aware of. ")
@click.option('--host_address',
              type=str,
              required=False,
              help="IP or DNS name for the host. ")
@click.option('--calling_virtual_volume_host_id',
              type=UUID,
              required=False,
              help="")
@pass_context
def create(ctx, virtual_volume_host_id, cluster_id, initiator_names = None, visible_protocol_endpoint_ids = None, host_address = None, calling_virtual_volume_host_id = None):
    """CreateVirtualVolumeHost creates a new ESX host."""
    VirtualVolumeNullResult = ctx.element.create_virtual_volume_host(virtual_volume_host_id=virtual_volume_host_id, cluster_id=cluster_id, initiator_names=initiator_names, visible_protocol_endpoint_ids=visible_protocol_endpoint_ids, host_address=host_address, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    cli_utils.print_result(VirtualVolumeNullResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

