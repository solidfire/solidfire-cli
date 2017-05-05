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
    """shutdown resetnode networking """

@cli.command('shutdown', short_help="""The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method, log in to the MIP for the pending node, and enter the "shutdown" method with either the "restart" or "halt" options. """, cls=SolidFireCommand)
@click.option('--nodes',
              type=str,
              required=True,
              prompt=True,
              help="""List of NodeIDs for the nodes to be shutdown. """)
@click.option('--option',
              type=str,
              required=False,
              help="""Specifies the action to take for the node shutdown. Possible values are: restart: Restarts the node. halt: Shuts down the node. """)
@pass_context
def shutdown(ctx,
           # Mandatory main parameter
           nodes,
           # Optional main parameter
           option = None):
    """The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method,"""
    """log in to the MIP for the pending node, and enter the "shutdown" method with either the "restart" or "halt" options."""

    

    cli_utils.establish_connection(ctx)
    

    nodes = parser.parse_array(nodes)
    
    

    ctx.logger.info(""": """"""nodes = """ + str(nodes)+";" + """option = """+str(option)+""";"""+"")
    try:
        _ShutdownResult = ctx.element.shutdown(nodes=nodes, option=option)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ShutdownResult), indent=4))
        return
    else:
        cli_utils.print_result(_ShutdownResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('resetnode', short_help="""The ResetNode API method enables you to reset a node to the factory settings. All data, packages (software upgrades, and so on), configurations, and log files are deleted from the node when you call this method. However, network settings for the node are preserved during this operation. Nodes that are participating in a cluster cannot be reset to the factory settings. The ResetNode API can only be used on nodes that are in an "Available" state. It cannot be used on nodes that are "Active" in a cluster, or in a "Pending" state. Caution: This method clears any data that is on the node. Exercise caution when using this method. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--build',
              type=str,
              required=True,
              prompt=True,
              help="""Specifies the URL to a remote Element software image to which the node will be reset. """)
@click.option('--force',
              type=bool,
              required=True,
              prompt=True,
              help="""Required parameter to successfully reset the node. """)
@pass_context
def resetnode(ctx,
           # Mandatory main parameter
           build,
           # Mandatory main parameter
           force):
    """The ResetNode API method enables you to reset a node to the factory settings. All data, packages (software upgrades, and so on),"""
    """configurations, and log files are deleted from the node when you call this method. However, network settings for the node are"""
    """preserved during this operation. Nodes that are participating in a cluster cannot be reset to the factory settings."""
    """The ResetNode API can only be used on nodes that are in an "Available" state. It cannot be used on nodes that are "Active" in a"""
    """cluster, or in a "Pending" state."""
    """Caution: This method clears any data that is on the node. Exercise caution when using this method."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""build = """ + str(build)+";"+"""force = """ + str(force)+""";"""+"")
    try:
        _ResetNodeResult = ctx.element.reset_node(build=build, force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ResetNodeResult), indent=4))
        return
    else:
        cli_utils.print_result(_ResetNodeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('networking', short_help="""The RestartNetworking API method enables you to restart the networking services on a node. Warning: This method restarts all networking services on a node, causing temporary loss of networking connectivity. Exercise caution when using this method. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--force',
              type=bool,
              required=True,
              prompt=True,
              help="""Required parameter to successfully reset the node. """)
@pass_context
def networking(ctx,
           # Mandatory main parameter
           force):
    """The RestartNetworking API method enables you to restart the networking services on a node."""
    """Warning: This method restarts all networking services on a node, causing temporary loss of networking connectivity."""
    """Exercise caution when using this method."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""force = """ + str(force)+""";"""+"")
    try:
        _dict = ctx.element.restart_networking(force=force)
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

