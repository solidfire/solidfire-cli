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
@click.option('--group_snapshot_id',
              type=int,
              required=True,
              help="ID of the snapshot. ")
@click.option('--expiration_time',
              type=str,
              required=False,
              help="Use to set the time when the snapshot should be removed. ")
@click.option('--enable_remote_replication',
              type=bool,
              required=False,
              help="Use to enable the snapshot created to be replicated to a remote SolidFire cluster. Possible values: <br/><b>true</b>: the snapshot will be replicated to remote storage. <br/><b>false</b>: Default. No replication. ")
@pass_context
def modify(ctx, group_snapshot_id, expiration_time = None, enable_remote_replication = None):
    """ModifyGroupSnapshot is used to change the attributes currently assigned to a group snapshot."""
    ModifyGroupSnapshotResult = ctx.element.modify_group_snapshot(group_snapshot_id=group_snapshot_id, expiration_time=expiration_time, enable_remote_replication=enable_remote_replication)
    cli_utils.print_result(ModifyGroupSnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

