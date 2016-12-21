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

@cli.command('complete', short_help="CompleteVolumePairing")
@click.argument('volume_pairing_key', type=str, required=True)
@click.argument('volume_id', type=int, required=True)
@pass_context
def complete(ctx, volume_pairing_key, volume_id):
    """CompleteVolumePairing is used to complete the pairing of two volumes."""
    CompleteVolumePairingResult = ctx.element.complete_volume_pairing(volume_pairing_key=volume_pairing_key, volume_id=volume_id)
    print(CompleteVolumePairingResult)

