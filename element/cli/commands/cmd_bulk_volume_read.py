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

@cli.command('start', short_help="StartBulkVolumeRead")
@click.option('--volume_id',
              type=int,
              required=True,
              help="ID of the volume to be read. ")
@click.option('--format',
              type=str,
              required=True,
              help="The format of the volume data. Can be either: <br/><b>uncompressed</b>: every byte of the volume is returned without any compression. <br/><b>native</b>: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. ")
@click.option('--snapshot_id',
              type=int,
              required=False,
              help="ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. ")
@click.option('--script',
              type=str,
              required=False,
              help="Executable name of a script. If no script name is given then the key and URL is necessary to access SolidFire nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. ")
@click.option('--script_parameters',
              type=str,
              required=False,
              help="JSON parameters to pass to the script. ")
@click.option('--attributes',
              type=dict,
              required=False,
              help="JSON attributes for the bulk volume job. ")
@pass_context
def start(ctx, volume_id, format, snapshot_id = None, script = None, script_parameters = None, attributes = None):
    """StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume."""
    """Only two bulk volume processes can run simultaneously on a volume."""
    """When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source."""
    """The external data is accessed by a web server running on a SolidFire node."""
    """Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.&lt;br/&gt;"""
    """&lt;br/&gt;"""
    """At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed."""
    """You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter."""
    """Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.&lt;br/&gt;"""
    """&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This process creates a new snapshot if the ID of an existing snapshot is not provided."""
    """Snapshots can be created if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    StartBulkVolumeReadResult = ctx.element.start_bulk_volume_read(volume_id=volume_id, format=format, snapshot_id=snapshot_id, script=script, script_parameters=script_parameters, attributes=attributes)
    print(json.dumps(json.loads(jsonpickle.encode(StartBulkVolumeReadResult)),indent=4))

