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

@cli.command('list', short_help="ListActivePairedVolumes")
@pass_context
def list(ctx):
    """ListActivePairedVolumes is used to list all of the active volumes paired with a volume."""
    """Volumes listed in the return for this method include volumes with active and pending pairings."""
    ListActivePairedVolumesResult = ctx.element.list_active_paired_volumes()
    print(ListActivePairedVolumesResult)

