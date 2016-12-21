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

@cli.command('start', short_help="StartBulkVolumeWrite")
@click.argument('volume_id', type=int, required=True)
@click.argument('format', type=str, required=True)
@click.argument('script', type=str, required=False)
@click.argument('script_parameters', type=str, required=False)
@click.argument('attributes', type=dict, required=False)
@pass_context
def start(ctx, volume_id, format, script = None, script_parameters = None, attributes = None):
    """StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume."""
    """Only two bulk volume processes can run simultaneously on a volume."""
    """When the session is initialized, data can be written to a SolidFire storage volume from an external backup source."""
    """The external data is accessed by a web server running on a SolidFire node."""
    """Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system."""
    StartBulkVolumeWriteResult = ctx.element.start_bulk_volume_write(volume_id=volume_id, format=format, script=script, script_parameters=script_parameters, attributes=attributes)
    print(json.dumps(json.loads(jsonpickle.encode(StartBulkVolumeWriteResult)),indent=4))

