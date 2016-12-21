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

@cli.command('rollback', short_help="RollbackToGroupSnapshot")
@click.argument('group_snapshot_id', type=int, required=True)
@click.argument('save_current_state', type=bool, required=True)
@click.argument('name', type=str, required=False)
@click.argument('attributes', type=dict, required=False)
@pass_context
def rollback(ctx, group_snapshot_id, save_current_state, name = None, attributes = None):
    """RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    CreateGroupSnapshotResult = ctx.element.rollback_to_group_snapshot(group_snapshot_id=group_snapshot_id, save_current_state=save_current_state, name=name, attributes=attributes)
    print(CreateGroupSnapshotResult)

