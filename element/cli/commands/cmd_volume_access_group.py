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

@cli.command('modify', short_help="ModifyVolumeAccessGroup")
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="The ID of the volume access group to modify. ")
@click.option('--virtual_network_id',
              type=int,
              required=False,
              help="The ID of the SolidFire Virtual Network ID to associate the volume access group with. ")
@click.option('--virtual_network_tags',
              type=int,
              required=False,
              help="The ID of the VLAN Virtual Network Tag to associate the volume access group with. ")
@click.option('--name',
              type=str,
              required=False,
              help="Name of the volume access group. It is not required to be unique, but recommended. ")
@click.option('--initiators',
              type=str,
              required=False,
              help="List of initiators to include in the volume access group. If unspecified, the access group's configured initiators will not be modified. ")
@click.option('--volumes',
              type=int,
              required=False,
              help="List of volumes to initially include in the volume access group. If unspecified, the access group's volumes will not be modified. ")
@click.option('--attributes',
              type=dict,
              required=False,
              help="List of Name/Value pairs in JSON object format. ")
@pass_context
def modify(ctx, volume_access_group_id, virtual_network_id = None, virtual_network_tags = None, name = None, initiators = None, volumes = None, attributes = None):
    """Update initiators and add or remove volumes from a volume access group."""
    """A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is."""
    """If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """Often, it is easier to use the convenience functions to modify initiators and volumes independently:"""
    """&lt;br/&gt;&lt;br/&gt;"""
    """AddInitiatorsToVolumeAccessGroup&lt;br/&gt;"""
    """RemoveInitiatorsFromVolumeAccessGroup&lt;br/&gt;"""
    """AddVolumesToVolumeAccessGroup&lt;br/&gt;"""
    """RemoveVolumesFromVolumeAccessGroup&lt;br/&gt;"""
    ModifyVolumeAccessGroupResult = ctx.element.modify_volume_access_group(volume_access_group_id=volume_access_group_id, virtual_network_id=virtual_network_id, virtual_network_tags=virtual_network_tags, name=name, initiators=initiators, volumes=volumes, attributes=attributes)
    cli_utils.print_result(ModifyVolumeAccessGroupResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

