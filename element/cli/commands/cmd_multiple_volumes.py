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

@cli.command('clone', short_help="CloneMultipleVolumes")
@click.argument('volumes', type=CloneMultipleVolumeParams, required=True)
@click.argument('access', type=str, required=False)
@click.argument('group_snapshot_id', type=int, required=False)
@click.argument('new_account_id', type=int, required=False)
@pass_context
def clone(ctx, volumes, access = None, group_snapshot_id = None, new_account_id = None):
    """CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together."""
    """If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5."""
    CloneMultipleVolumesResult = ctx.element.clone_multiple_volumes(volumes=volumes, access=access, group_snapshot_id=group_snapshot_id, new_account_id=new_account_id)
    print(CloneMultipleVolumesResult)

