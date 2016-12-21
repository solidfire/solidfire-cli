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

@cli.command('remove', short_help="RemoveVolumePair")
@click.option('--volume_id',
              type=int,
              required=True,
              help="ID of the volume on which to stop the replication process. ")
@pass_context
def remove(ctx, volume_id):
    """RemoveVolumePair is used to remove the remote pairing between two volumes."""
    """When the volume pairing information is removed, data is no longer replicated to or from the volume."""
    """This method should be run on both the source and target volumes that are paired together."""
    RemoveVolumePairResult = ctx.element.remove_volume_pair(volume_id=volume_id)
    print(json.dumps(json.loads(jsonpickle.encode(RemoveVolumePairResult)),indent=4))

