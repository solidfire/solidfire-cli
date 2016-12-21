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

@cli.command('cancel', short_help="CancelGroupClone")
@click.argument('group_clone_id', type=int, required=True)
@pass_context
def cancel(ctx, group_clone_id):
    """CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process for a group of clones. When you cancel a group clone operation, the system completes and removes the operation's associated asyncHandle. This method does not return anything."""
    CancelGroupCloneResult = ctx.element.cancel_group_clone(group_clone_id=group_clone_id)
    print(json.dumps(json.loads(jsonpickle.encode(CancelGroupCloneResult)),indent=4))

