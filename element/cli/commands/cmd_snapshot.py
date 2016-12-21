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

@cli.command('modify', short_help="ModifySnapshot")
@click.argument('snapshot_id', type=int, required=True)
@click.argument('expiration_time', type=str, required=False)
@click.argument('enable_remote_replication', type=bool, required=False)
@pass_context
def modify(ctx, snapshot_id, expiration_time = None, enable_remote_replication = None):
    """ModifySnapshot is used to change the attributes currently assigned to a snapshot."""
    """Use this API method to enable the snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system."""
    ModifySnapshotResult = ctx.element.modify_snapshot(snapshot_id=snapshot_id, expiration_time=expiration_time, enable_remote_replication=enable_remote_replication)
    print(json.dumps(json.loads(jsonpickle.encode(ModifySnapshotResult)),indent=4))

