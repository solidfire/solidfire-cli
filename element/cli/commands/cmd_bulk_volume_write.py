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
@click.option('--volume_id',
              type=int,
              required=True,
              help="ID of the volume to be written to. ")
@click.option('--format',
              type=str,
              required=True,
              help="The format of the volume data. Can be either: <br/><b>uncompressed</b>: every byte of the volume is returned without any compression. <br/><b>native</b>: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write ")
@click.option('--script',
              type=str,
              required=False,
              help="Executable name of a script. If no script name is given then the key and URL are necessary to access SolidFire nodes. The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted. ")
@click.option('--script_parameters',
              type=str,
              required=False,
              help="JSON parameters to pass to the script. ")
@click.option('--attributes',
              type=dict,
              required=False,
              help="JSON attributes for the bulk volume job. ")
@pass_context
def start(ctx, volume_id, format, script = None, script_parameters = None, attributes = None):
    """StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume."""
    """Only two bulk volume processes can run simultaneously on a volume."""
    """When the session is initialized, data can be written to a SolidFire storage volume from an external backup source."""
    """The external data is accessed by a web server running on a SolidFire node."""
    """Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system."""
    StartBulkVolumeWriteResult = ctx.element.start_bulk_volume_write(volume_id=volume_id, format=format, script=script, script_parameters=script_parameters, attributes=attributes)
    print(json.dumps(json.loads(jsonpickle.encode(StartBulkVolumeWriteResult)),indent=4))

