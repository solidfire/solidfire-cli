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
from solidfire.custom.models import *
from uuid import UUID
from element import exceptions
from solidfire import common
from element.cli.cli import SolidFireOption, SolidFireCommand

@click.group()
@pass_context
def cli(ctx):
    """list """

@cli.command('list', short_help="""Gets protocol endpoints in the system If protocolEndpointIDs isn't specified all protocol endpoints are returned. Else the supplied protocolEndpointIDs are. """, cls=SolidFireCommand)
@click.option('--protocolendpointids',
              type=str,
              required=False,
              help=""" """)
@pass_context
def list(ctx,
           # Optional main parameter
           protocolendpointids = None):
    """Gets protocol endpoints in the system"""
    """If protocolEndpointIDs isn&#x27;t specified all protocol endpoints"""
    """are returned. Else the supplied protocolEndpointIDs are."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    protocolendpointids = parser.parse_array(protocolendpointids)
    

    ctx.logger.info("""protocolendpointids = """+str(protocolendpointids)+""";"""+"")
    try:
        _ListProtocolEndpointsResult = ctx.element.list_protocol_endpoints(protocol_endpoint_ids=protocolendpointids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListProtocolEndpointsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

