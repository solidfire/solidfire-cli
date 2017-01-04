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
from element import exceptions


@click.group()
@pass_context
def cli(ctx):
    """ListProtocolEndpoints """

@cli.command('ListProtocolEndpoints', short_help="ListProtocolEndpoints")
@click.option('--protocol_endpoint_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListProtocolEndpoints(ctx,
           protocol_endpoint_ids = None):
    """Gets protocol endpoints in the system"""
    """If protocolEndpointIDs isn't specified all protocol endpoints"""
    """are returned. Else the supplied protocolEndpointIDs are."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    protocol_endpoint_ids = parser.parse_array(protocol_endpoint_ids)

    ListProtocolEndpointsResult = ctx.element.list_protocol_endpoints(protocol_endpoint_ids=protocol_endpoint_ids)
    cli_utils.print_result(ListProtocolEndpointsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

