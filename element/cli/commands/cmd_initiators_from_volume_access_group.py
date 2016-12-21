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

@cli.command('remove', short_help="RemoveInitiatorsFromVolumeAccessGroup")
@click.argument('volume_access_group_id', type=int, required=True)
@click.argument('initiators', type=str, required=True)
@pass_context
def remove(ctx, volume_access_group_id, initiators):
    """Remove initiators from a volume access group."""
    ModifyVolumeAccessGroupResult = ctx.element.remove_initiators_from_volume_access_group(volume_access_group_id=volume_access_group_id, initiators=initiators)
    print(ModifyVolumeAccessGroupResult)

