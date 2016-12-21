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
@click.argument('volume_access_group_id', type=int, required=True)
@click.argument('virtual_network_id', type=int, required=False)
@click.argument('virtual_network_tags', type=int, required=False)
@click.argument('name', type=str, required=False)
@click.argument('initiators', type=str, required=False)
@click.argument('volumes', type=int, required=False)
@click.argument('attributes', type=dict, required=False)
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
    print(json.dumps(json.loads(jsonpickle.encode(ModifyVolumeAccessGroupResult)),indent=4))

