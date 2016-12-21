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

@cli.command('list', short_help="ListStorageContainers")
@click.option('--storage_container_ids',
              type=UUID,
              required=False,
              help="List of storage containers to get ")
@pass_context
def list(ctx, storage_container_ids = None):
    """Gets information for all storage containers currently in the system."""
    ListStorageContainersResult = ctx.element.list_storage_containers(storage_container_ids=storage_container_ids)
    print(json.dumps(json.loads(jsonpickle.encode(ListStorageContainersResult)),indent=4))

