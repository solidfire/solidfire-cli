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

@cli.command('modify', short_help="ModifyVolumes")
@click.argument('volume_ids', type=int, required=True)
@click.argument('account_id', type=int, required=False)
@click.argument('access', type=str, required=False)
@click.argument('attributes', type=dict, required=False)
@click.argument('qos', type=QoS, required=False)
@click.argument('total_size', type=int, required=False)
@pass_context
def modify(ctx, volume_ids, account_id = None, access = None, attributes = None, qos = None, total_size = None):
    """ModifyVolumes allows you to configure up to 500 existing volumes at one time. Changes take place immediately. If ModifyVolumes fails to modify any of the specified volumes, none of the specified volumes are changed.If you do not specify QoS values when you modify volumes, the QoS values for each volume remain unchanged. You can retrieve default QoS values for a newly created volume by running the GetDefaultQoS method.When you need to increase the size of volumes that are being replicated, do so in the following order to prevent replication errors:Increase the size of the &quot;Replication Target&quot; volume.Increase the size of the source or &quot;Read / Write&quot; volume. recommends that both the target and source volumes be the same size.NOTE: If you change access status to locked or replicationTarget all existing iSCSI connections are terminated."""
    ModifyVolumesResult = ctx.element.modify_volumes(volume_ids=volume_ids, account_id=account_id, access=access, attributes=attributes, qos=qos, total_size=total_size)
    print(ModifyVolumesResult)

