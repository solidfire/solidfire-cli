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

@cli.command('list', short_help="ListVirtualVolumes")
@click.argument('details', type=bool, required=False)
@click.argument('limit', type=int, required=False)
@click.argument('recursive', type=bool, required=False)
@click.argument('start_virtual_volume_id', type=UUID, required=False)
@click.argument('virtual_volume_ids', type=UUID, required=False)
@pass_context
def list(ctx, details = None, limit = None, recursive = None, start_virtual_volume_id = None, virtual_volume_ids = None):
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset."""
    ListVirtualVolumesResult = ctx.element.list_virtual_volumes(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=start_virtual_volume_id, virtual_volume_ids=virtual_volume_ids)
    print(ListVirtualVolumesResult)

