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

@cli.command('modify', short_help="ModifyGroupSnapshot")
@click.argument('group_snapshot_id', type=int, required=True)
@click.argument('expiration_time', type=str, required=False)
@click.argument('enable_remote_replication', type=bool, required=False)
@pass_context
def modify(ctx, group_snapshot_id, expiration_time = None, enable_remote_replication = None):
    """ModifyGroupSnapshot is used to change the attributes currently assigned to a group snapshot."""
    ModifyGroupSnapshotResult = ctx.element.modify_group_snapshot(group_snapshot_id=group_snapshot_id, expiration_time=expiration_time, enable_remote_replication=enable_remote_replication)
    print(json.dumps(json.loads(jsonpickle.encode(ModifyGroupSnapshotResult)),indent=4))

