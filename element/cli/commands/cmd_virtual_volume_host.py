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

@cli.command('create', short_help="CreateVirtualVolumeHost")
@click.argument('virtual_volume_host_id', type=UUID, required=True)
@click.argument('cluster_id', type=UUID, required=True)
@click.argument('initiator_names', type=str, required=False)
@click.argument('visible_protocol_endpoint_ids', type=UUID, required=False)
@click.argument('host_address', type=str, required=False)
@click.argument('calling_virtual_volume_host_id', type=UUID, required=False)
@pass_context
def create(ctx, virtual_volume_host_id, cluster_id, initiator_names = None, visible_protocol_endpoint_ids = None, host_address = None, calling_virtual_volume_host_id = None):
    """CreateVirtualVolumeHost creates a new ESX host."""
    VirtualVolumeNullResult = ctx.element.create_virtual_volume_host(virtual_volume_host_id=virtual_volume_host_id, cluster_id=cluster_id, initiator_names=initiator_names, visible_protocol_endpoint_ids=visible_protocol_endpoint_ids, host_address=host_address, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    print(VirtualVolumeNullResult)

