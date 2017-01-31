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


@click.group()
@pass_context
def cli(ctx):
    """shutdown resetnode networking services """

@cli.command('shutdown', short_help="""The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method, login in to the MIP for the pending node and enter the "shutdown" method with either the "restart" or "halt" options in the following table. """)
@click.option('--nodes',
              type=str,
              required=True,
              help="""List of NodeIDs for the nodes to be shutdown. """)
@click.option('--option',
              type=str,
              required=False,
              help="""Action to take for the node shutdown:restart: Restarts the node.halt: Performs full power-off of the node. """)
@pass_context
def shutdown(ctx,
           nodes,
           option = None):
    """The Shutdown API method enables you to restart or shutdown a node that has not yet been added to a cluster. To use this method, login in to the MIP for the pending node and enter the &quot;shutdown&quot; method with either the &quot;restart&quot; or &quot;halt&quot; options in the following table."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    nodes = parser.parse_array(nodes)
    

    ctx.logger.info("""nodes = """+str(nodes)+""";"""+"""option = """+str(option)+""";"""+"")
    try:
        _ShutdownResult = ctx.element.shutdown(nodes=nodes, option=option)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ShutdownResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('resetnode', short_help="""Allows you to reset a node to the SolidFire factory settings. All data will be deleted from the node when you call this method. A node participating in a cluster cannot be reset. """)
@click.option('--build',
              type=str,
              required=True,
              help="""Used to specify the URL to a remote Element software image to which the node will be reset. """)
@click.option('--force',
              type=bool,
              required=True,
              help="""The force parameter must be included in order to successfully reset the node. """)
@click.option('--option',
              type=str,
              required=True,
              help="""Used to enter specifications for running the reset operation. """)
@pass_context
def resetnode(ctx,
           build,
           force,
           option):
    """Allows you to reset a node to the SolidFire factory settings. All data will be deleted from the node when you call this method. A node participating in a cluster cannot be reset."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""build = """+str(build)+""";"""+"""force = """+str(force)+""";"""+"""option = """+str(option)+""";"""+"")
    try:
        _ResetNodeResult = ctx.element.reset_node(build=build, force=force, option=option)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ResetNodeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('networking', short_help="""The RestartNetworking API method is used to restart the networking services on a node.WARNING! This method restarts all networking services on a node, causing temporary loss of networking connectivity. Exercise caution when using this method. """)
@click.option('--force',
              type=bool,
              required=True,
              help="""The "force" parameter must be included on this method to successfully restart the networking. """)
@pass_context
def networking(ctx,
           force):
    """The RestartNetworking API method is used to restart the networking services on a node.WARNING! This method restarts all networking services on a node, causing temporary loss of networking connectivity. Exercise caution when using this method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""force = """+str(force)+""";"""+"")
    try:
        _dict = ctx.element.restart_networking(force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_dict, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('services', short_help="""The RestartServices API method is used to restart the  Element services on a node.Caution: This method causes temporary node services interruption. Exercise caution when using this method. """)
@click.option('--force',
              type=bool,
              required=True,
              help="""The "force" parameter must be included on this method to successfully restart services on a node.    """)
@click.option('--service',
              type=str,
              required=False,
              help="""Service name to be restarted. """)
@click.option('--action',
              type=str,
              required=False,
              help="""Action to perform on the service (start, stop, restart). """)
@pass_context
def services(ctx,
           force,
           service = None,
           action = None):
    """The RestartServices API method is used to restart the  Element services on a node.Caution: This method causes temporary node services interruption. Exercise caution when using this method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""force = """+str(force)+""";"""+"""service = """+str(service)+""";"""+"""action = """+str(action)+""";"""+"")
    try:
        _dict = ctx.element.restart_services(force=force, service=service, action=action)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_dict, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

