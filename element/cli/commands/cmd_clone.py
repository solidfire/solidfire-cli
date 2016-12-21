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

@cli.command('cancel', short_help="CancelClone")
@click.option('--clone_id',
              type=int,
              required=True,
              help="")
@pass_context
def cancel(ctx, clone_id):
    """Cancels a currently running clone operation. This method does not return anything."""
    CancelCloneResult = ctx.element.cancel_clone(clone_id=clone_id)
    print(json.dumps(json.loads(jsonpickle.encode(CancelCloneResult)),indent=4))

