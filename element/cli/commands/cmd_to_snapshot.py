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

@cli.command('rollback', short_help="RollbackToSnapshot")
@click.argument('volume_id', type=int, required=True)
@click.argument('snapshot_id', type=int, required=True)
@click.argument('save_current_state', type=bool, required=True)
@click.argument('name', type=str, required=False)
@click.argument('attributes', type=dict, required=False)
@pass_context
def rollback(ctx, volume_id, snapshot_id, save_current_state, name = None, attributes = None):
    """RollbackToSnapshot is used to make an existing snapshot the &quot;active&quot; volume image. This method creates a new """
    """snapshot from an existing snapshot. The new snapshot becomes &quot;active&quot; and the existing snapshot is preserved until """
    """it is manually deleted. The previously &quot;active&quot; snapshot is deleted unless the parameter saveCurrentState is set with """
    """a value of &quot;true.&quot;"""
    """&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    CreateSnapshotResult = ctx.element.rollback_to_snapshot(volume_id=volume_id, snapshot_id=snapshot_id, save_current_state=save_current_state, name=name, attributes=attributes)
    print(CreateSnapshotResult)

