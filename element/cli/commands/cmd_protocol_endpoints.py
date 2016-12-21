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

@cli.command('list', short_help="ListProtocolEndpoints")
@click.argument('protocol_endpoint_ids', type=UUID, required=False)
@pass_context
def list(ctx, protocol_endpoint_ids = None):
    """Gets protocol endpoints in the system"""
    """If protocolEndpointIDs isn't specified all protocol endpoints"""
    """are returned. Else the supplied protocolEndpointIDs are."""
    ListProtocolEndpointsResult = ctx.element.list_protocol_endpoints(protocol_endpoint_ids=protocol_endpoint_ids)
    print(json.dumps(json.loads(jsonpickle.encode(ListProtocolEndpointsResult)),indent=4))

