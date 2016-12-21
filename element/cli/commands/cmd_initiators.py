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

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('list', short_help="ListInitiators")
@click.argument('start_initiator_id', type=int, required=False)
@click.argument('limit', type=int, required=False)
@click.argument('initiators', type=int, required=False)
@pass_context
def list(ctx, start_initiator_id = None, limit = None, initiators = None):
    """ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs)."""
    ListInitiatorsResult = ctx.element.list_initiators(start_initiator_id=start_initiator_id, limit=limit, initiators=initiators)
    print(ListInitiatorsResult)

