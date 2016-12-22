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

@cli.command('modify', short_help="ModifyVolume")
@click.option('--volume_id',
              type=int,
              required=True,
              help="VolumeID for the volume to be modified. ")
@click.option('--account_id',
              type=int,
              required=False,
              help="AccountID to which the volume is reassigned. If none is specified, the previous account name is used. ")
@click.option('--access',
              type=str,
              required=False,
              help="Access allowed for the volume. <br/><b>readOnly</b>: Only read operations are allowed. <br/><b>readWrite</b>: Reads and writes are allowed. <br/><b>locked</b>: No reads or writes are allowed. <br/><b>replicationTarget</b>: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. <br/><br/> If unspecified, the access settings of the clone will be the same as the source. ")
@click.option('--qos',
              type=QoS,
              required=False,
              help="New quality of service settings for this volume. ")
@click.option('--total_size',
              type=int,
              required=False,
              help="New size of the volume in bytes. Size is rounded up to the nearest 1MiB size. This parameter can only be used to *increase* the size of a volume. ")
@click.option('--attributes',
              type=dict,
              required=False,
              help="List of Name/Value pairs in JSON object format. ")
@pass_context
def modify(ctx, volume_id, account_id = None, access = None, qos = None, total_size = None, attributes = None):
    """ModifyVolume is used to modify settings on an existing volume."""
    """Modifications can be made to one volume at a time and changes take place immediately."""
    """If an optional parameter is left unspecified, the value will not be changed."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """Extending the size of a volume that is being replicated should be done in an order."""
    """The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized."""
    """It is recommended that both the target and the source volumes be the same size."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: If you change access status to locked or target all existing iSCSI connections are terminated."""
    ModifyVolumeResult = ctx.element.modify_volume(volume_id=volume_id, account_id=account_id, access=access, qos=qos, total_size=total_size, attributes=attributes)
    cli_utils.print_result(ModifyVolumeResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

