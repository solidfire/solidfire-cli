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
    """list restart """

@cli.command('list', short_help="""You can use ListServices to return the services information for nodes, drives, current software, and other services that are running on the cluster. """, cls=SolidFireCommand)
@pass_context
def list(ctx):
    """You can use ListServices to return the services information for nodes, drives, current software, and other services that are running on the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListServicesResult = ctx.element.list_services()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListServicesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListServicesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('restart', short_help="""The RestartServices API method enables you to restart the services on a node. Caution: This method causes temporary node services interruption. Exercise caution when using this method. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--force',
              type=bool,
              required=True,
              prompt=True,
              help="""Required parameter to successfully restart services on a node. """)
@click.option('--service',
              type=str,
              required=False,
              help="""Service name to be restarted. """)
@click.option('--action',
              type=str,
              required=False,
              help="""Action to perform on the service (start, stop, restart). """)
@pass_context
def restart(ctx,
           # Mandatory main parameter
           force,
           # Optional main parameter
           service = None,
           # Optional main parameter
           action = None):
    """The RestartServices API method enables you to restart the services on a node."""
    """Caution: This method causes temporary node services interruption. Exercise caution when using this method."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    ctx.logger.info(""": """"""force = """ + str(force)+";" + """service = """+str(service)+";" + """action = """+str(action)+""";"""+"")
    try:
        _dict = ctx.element.restart_services(force=force, service=service, action=action)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_dict), indent=4))
        return
    else:
        cli_utils.print_result(_dict, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

