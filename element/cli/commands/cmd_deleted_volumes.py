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

@cli.command('purge', short_help="PurgeDeletedVolumes")
@click.option('--volume_ids',
              type=int,
              required=False,
              help="A list of volumeIDs of volumes to be purged from the system. ")
@click.option('--account_ids',
              type=int,
              required=False,
              help="A list of accountIDs. All of the volumes from all of the specified accounts are purged from the system. ")
@click.option('--volume_access_group_ids',
              type=int,
              required=False,
              help="A list of volumeAccessGroupIDs. All of the volumes from all of the specified Volume Access Groups are purged from the system. ")
@pass_context
def purge(ctx, volume_ids = None, account_ids = None, volume_access_group_ids = None):
    """PurgeDeletedVolumes immediately and permanently purges volumes that have been deleted; you can use this method to purge up to 500 volumes at one time. You must delete volumes using DeleteVolumes before they can be purged. Volumes are purged by the system automatically after a period of time, so usage of this method is not typically required."""
    PurgeDeletedVolumesResult = ctx.element.purge_deleted_volumes(volume_ids=volume_ids, account_ids=account_ids, volume_access_group_ids=volume_access_group_ids)
    cli_utils.print_result(PurgeDeletedVolumesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

