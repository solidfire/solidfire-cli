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

@cli.command('start', short_help="StartVolumePairing")
@click.option('--volume_id',
              type=int,
              required=True,
              help="The ID of the volume on which to start the pairing process. ")
@click.option('--mode',
              type=str,
              required=False,
              help="The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.<br/> Possible values:<br/> <b>Async</b>: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.<br/> <b>Sync</b>: Source acknowledges write when the data is stored locally and on the remote cluster.<br/> <b>SnapshotsOnly</b>: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.<br/> ")
@pass_context
def start(ctx, volume_id, mode = None):
    """StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume."""
    """The key that this method creates is used in the &quot;CompleteVolumePairing&quot; API method to establish a volume pairing."""
    StartVolumePairingResult = ctx.element.start_volume_pairing(volume_id=volume_id, mode=mode)
    cli_utils.print_result(StartVolumePairingResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

