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
@click.argument('volume_ids', type=int, required=False)
@click.argument('account_ids', type=int, required=False)
@click.argument('volume_access_group_ids', type=int, required=False)
@pass_context
def purge(ctx, volume_ids = None, account_ids = None, volume_access_group_ids = None):
    """PurgeDeletedVolumes immediately and permanently purges volumes that have been deleted; you can use this method to purge up to 500 volumes at one time. You must delete volumes using DeleteVolumes before they can be purged. Volumes are purged by the system automatically after a period of time, so usage of this method is not typically required."""
    PurgeDeletedVolumesResult = ctx.element.purge_deleted_volumes(volume_ids=volume_ids, account_ids=account_ids, volume_access_group_ids=volume_access_group_ids)
    print(json.dumps(json.loads(jsonpickle.encode(PurgeDeletedVolumesResult)),indent=4))

