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

@cli.command('remove', short_help="RemoveBackupTarget")
@click.argument('backup_target_id', type=int, required=True)
@pass_context
def remove(ctx, backup_target_id):
    """RemoveBackupTarget allows you to delete backup targets."""
    RemoveBackupTargetResult = ctx.element.remove_backup_target(backup_target_id=backup_target_id)
    print(json.dumps(json.loads(jsonpickle.encode(RemoveBackupTargetResult)),indent=4))

