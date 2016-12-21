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

@cli.command('get', short_help="GetDriveHardwareInfo")
@click.option('--drive_id',
              type=int,
              required=True,
              help="DriveID for the drive information requested. DriveIDs can be obtained via the "ListDrives" method. ")
@pass_context
def get(ctx, drive_id):
    """GetDriveHardwareInfo returns all the hardware info for the given drive. This generally includes manufacturers, vendors, versions, and other associated hardware identification information."""
    GetDriveHardwareInfoResult = ctx.element.get_drive_hardware_info(drive_id=drive_id)
    print(json.dumps(json.loads(jsonpickle.encode(GetDriveHardwareInfoResult)),indent=4))

