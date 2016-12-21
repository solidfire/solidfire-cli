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

@cli.command('modify', short_help="ModifyVolumePair")
@click.argument('volume_id', type=int, required=True)
@click.argument('paused_manual', type=bool, required=False)
@click.argument('mode', type=str, required=False)
@pass_context
def modify(ctx, volume_id, paused_manual = None, mode = None):
    """ModifyVolumePair is used to pause or restart replication between a pair of volumes."""
    ModifyVolumePairResult = ctx.element.modify_volume_pair(volume_id=volume_id, paused_manual=paused_manual, mode=mode)
    print(ModifyVolumePairResult)

