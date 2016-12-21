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

@cli.command('modify', short_help="ModifyStorageContainer")
@click.option('--storage_container_id',
              type=UUID,
              required=True,
              help="")
@click.option('--initiator_secret',
              type=str,
              required=False,
              help="")
@click.option('--target_secret',
              type=str,
              required=False,
              help="")
@pass_context
def modify(ctx, storage_container_id, initiator_secret = None, target_secret = None):
    """Modifies an existing storage container."""
    ModifyStorageContainerResult = ctx.element.modify_storage_container(storage_container_id=storage_container_id, initiator_secret=initiator_secret, target_secret=target_secret)
    print(json.dumps(json.loads(jsonpickle.encode(ModifyStorageContainerResult)),indent=4))

