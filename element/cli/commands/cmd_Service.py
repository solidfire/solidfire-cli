#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli import parser
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import simplejson
from uuid import UUID


@click.group()
@pass_context
def cli(ctx):
    """ListServices """
    ctx.sfapi = ctx.client

@cli.command('ListServices', short_help="ListServices")
@pass_context
def ListServices(ctx):
    """List the services in the cluster."""



    ListServicesResult = ctx.element.list_services()
    cli_utils.print_result(ListServicesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

