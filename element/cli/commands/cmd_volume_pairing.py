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
@click.argument('volume_id', type=int, required=True)
@click.argument('mode', type=str, required=False)
@pass_context
def start(ctx, volume_id, mode = None):
    """StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume."""
    """The key that this method creates is used in the &quot;CompleteVolumePairing&quot; API method to establish a volume pairing."""
    StartVolumePairingResult = ctx.element.start_volume_pairing(volume_id=volume_id, mode=mode)
    print(json.dumps(json.loads(jsonpickle.encode(StartVolumePairingResult)),indent=4))

