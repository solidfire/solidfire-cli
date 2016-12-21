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

@cli.command('modify', short_help="ModifyVolumes")
@click.option('--volume_ids',
              type=int,
              required=True,
              help="A list of volumeIDs for the volumes to be modified. ")
@click.option('--account_id',
              type=int,
              required=False,
              help="AccountID to which the volume is reassigned. If none is specified, the previous account name is used. ")
@click.option('--access',
              type=str,
              required=False,
              help="Access allowed for the volume. Possible values:readOnly: Only read operations are allowed.readWrite: Reads and writes are allowed.locked: No reads or writes are allowed.If not specified, the access value does not change.replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.If a value is not specified, the access value does not change.  ")
@click.option('--qos',
              type=QoS,
              required=False,
              help="New quality of service settings for this volume.If not specified, the QoS settings are not changed. ")
@click.option('--total_size',
              type=int,
              required=False,
              help="New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB in size. This parameter can only be used to increase the size of a volume. ")
@click.option('--attributes',
              type=dict,
              required=False,
              help="")
@pass_context
def modify(ctx, volume_ids, account_id = None, access = None, qos = None, total_size = None, attributes = None):
    """ModifyVolumes allows you to configure up to 500 existing volumes at one time. Changes take place immediately. If ModifyVolumes fails to modify any of the specified volumes, none of the specified volumes are changed.If you do not specify QoS values when you modify volumes, the QoS values for each volume remain unchanged. You can retrieve default QoS values for a newly created volume by running the GetDefaultQoS method.When you need to increase the size of volumes that are being replicated, do so in the following order to prevent replication errors:Increase the size of the &quot;Replication Target&quot; volume.Increase the size of the source or &quot;Read / Write&quot; volume. recommends that both the target and source volumes be the same size.NOTE: If you change access status to locked or replicationTarget all existing iSCSI connections are terminated."""
    ModifyVolumesResult = ctx.element.modify_volumes(volume_ids=volume_ids, account_id=account_id, access=access, qos=qos, total_size=total_size, attributes=attributes)
    print(json.dumps(json.loads(jsonpickle.encode(ModifyVolumesResult)),indent=4))

