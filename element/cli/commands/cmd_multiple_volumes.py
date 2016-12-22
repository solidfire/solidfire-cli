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

@cli.command('clone', short_help="CloneMultipleVolumes")
@click.option('--volumes',
              type=CloneMultipleVolumeParams,
              required=True,
              help="Array of Unique ID for each volume to include in the clone with optional parameters. If optional parameters are not specified, the values will be inherited from the source volumes. ")
@click.option('--access',
              type=str,
              required=False,
              help="New default access method for the new volumes if not overridden by information passed in the volumes array. <br/><b>readOnly</b>: Only read operations are allowed. <br/><b>readWrite</b>: Reads and writes are allowed. <br/><b>locked</b>: No reads or writes are allowed. <br/><b>replicationTarget</b>: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. <br/><br/> If unspecified, the access settings of the clone will be the same as the source. ")
@click.option('--group_snapshot_id',
              type=int,
              required=False,
              help="ID of the group snapshot to use as a basis for the clone. ")
@click.option('--new_account_id',
              type=int,
              required=False,
              help="New account ID for the volumes if not overridden by information passed in the volumes array. ")
@pass_context
def clone(ctx, volumes, access = None, group_snapshot_id = None, new_account_id = None):
    """CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together."""
    """If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5."""
    CloneMultipleVolumesResult = ctx.element.clone_multiple_volumes(volumes=volumes, access=access, group_snapshot_id=group_snapshot_id, new_account_id=new_account_id)
    cli_utils.print_result(CloneMultipleVolumesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

