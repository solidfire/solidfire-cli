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

@cli.command('get', short_help="GetStorageContainerEfficiency")
@click.option('--storage_container_id',
              type=UUID,
              required=True,
              help="The ID of the storage container for which to retrieve efficiency information. ")
@pass_context
def get(ctx, storage_container_id):
    """GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container."""
    GetStorageContainerEfficiencyResult = ctx.element.get_storage_container_efficiency(storage_container_id=storage_container_id)
    print(json.dumps(json.loads(jsonpickle.encode(GetStorageContainerEfficiencyResult)),indent=4))

