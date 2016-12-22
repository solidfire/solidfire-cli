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

@cli.command('modify', short_help="ModifyInitiators")
@click.option('--initiators',
              type=ModifyInitiator,
              required=True,
              help="A list of Initiator objects containing characteristics of each initiator to modify. ")
@pass_context
def modify(ctx, initiators):
    """ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators."""
    """If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible)."""
    ModifyInitiatorsResult = ctx.element.modify_initiators(initiators=initiators)
    cli_utils.print_result(ModifyInitiatorsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

