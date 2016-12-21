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

@cli.command('rollback', short_help="RollbackToGroupSnapshot")
@click.option('--group_snapshot_id',
              type=int,
              required=True,
              help="Unique ID of the group snapshot. ")
@click.option('--save_current_state',
              type=bool,
              required=True,
              help="<br/><b>true</b>: The previous active volume image is kept. <br/><b>false</b>: (default) The previous active volume image is deleted. ")
@click.option('--name',
              type=str,
              required=False,
              help="Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with  "-copy" appended to the end of the name. ")
@click.option('--attributes',
              type=dict,
              required=False,
              help="List of Name/Value pairs in JSON object format ")
@pass_context
def rollback(ctx, group_snapshot_id, save_current_state, name = None, attributes = None):
    """RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    CreateGroupSnapshotResult = ctx.element.rollback_to_group_snapshot(group_snapshot_id=group_snapshot_id, save_current_state=save_current_state, name=name, attributes=attributes)
    print(json.dumps(json.loads(jsonpickle.encode(CreateGroupSnapshotResult)),indent=4))

