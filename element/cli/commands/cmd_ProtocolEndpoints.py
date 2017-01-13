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
from element import utils
import jsonpickle
import simplejson
from solidfire.models import *
from uuid import UUID
from element import exceptions
from solidfire import common


@click.group()
@pass_context
def cli(ctx):
    """List """

@cli.command('List', short_help="""Gets protocol endpoints in the system If protocolEndpointIDs isn't specified all protocol endpoints are returned. Else the supplied protocolEndpointIDs are. """)
@click.option('--protocol_endpoint_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def List(ctx,
           protocol_endpoint_ids = None):
    """Gets protocol endpoints in the system"""
    """If protocolEndpointIDs isn't specified all protocol endpoints"""
    """are returned. Else the supplied protocolEndpointIDs are."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    protocol_endpoint_ids = parser.parse_array(protocol_endpoint_ids)

    ctx.logger.info("""protocol_endpoint_ids = """+str(protocol_endpoint_ids)+""";"""+"")
    try:
        ListProtocolEndpointsResult = ctx.element.list_protocol_endpoints(protocol_endpoint_ids=protocol_endpoint_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListProtocolEndpointsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

