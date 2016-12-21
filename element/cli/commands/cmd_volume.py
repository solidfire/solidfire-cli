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
@click.argument('volume_id', type=int, required=True)
@click.argument('account_id', type=int, required=False)
@click.argument('access', type=str, required=False)
@click.argument('qos', type=QoS, required=False)
@click.argument('total_size', type=int, required=False)
@click.argument('attributes', type=dict, required=False)
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
    print(json.dumps(json.loads(jsonpickle.encode(ModifyVolumeResult)),indent=4))

