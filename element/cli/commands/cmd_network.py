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
    """listnodefibrechannelportinfo listfibrechannelsessions listfibrechannelportinfo listiscsisessions listinterfaces """

@cli.command('listnodefibrechannelportinfo', short_help="""The ListNodeFibreChannelPortInfo API method enables you to retrieve information about the Fibre Channel ports on a node. The API method is intended for use on individual nodes; userid and password authentication is required for access to individual Fibre Channel nodes. """, cls=SolidFireCommand)
@pass_context
def listnodefibrechannelportinfo(ctx):
    """The ListNodeFibreChannelPortInfo API method enables you to retrieve information about the Fibre Channel ports on a node. The API method is intended for use on individual nodes; userid and password authentication is required for access to individual Fibre Channel nodes."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListNodeFibreChannelPortInfoResult = ctx.element.list_node_fibre_channel_port_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListNodeFibreChannelPortInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListNodeFibreChannelPortInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listfibrechannelsessions', short_help="""ListFibreChannelSessions enables you to retrieve information about the active Fibre Channel sessions on a cluster.  """, cls=SolidFireCommand)
@pass_context
def listfibrechannelsessions(ctx):
    """ListFibreChannelSessions enables you to retrieve information about the active Fibre Channel sessions on a cluster. """

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListFibreChannelSessionsResult = ctx.element.list_fibre_channel_sessions()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListFibreChannelSessionsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListFibreChannelSessionsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listfibrechannelportinfo', short_help="""ListFibreChannelPortInfo enables you to retrieve information about the Fibre Channel ports on a node.  The API method is intended for use on individual nodes; userid and password authentication is required for access to individual Fibre Channel nodes. """, cls=SolidFireCommand)
@pass_context
def listfibrechannelportinfo(ctx):
    """ListFibreChannelPortInfo enables you to retrieve information about the Fibre Channel ports on a node.  The API method is intended for use on individual nodes; userid and password authentication is required for access to individual Fibre Channel nodes."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListFibreChannelPortInfoResult = ctx.element.list_fibre_channel_port_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListFibreChannelPortInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListFibreChannelPortInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listiscsisessions', short_help="""You can use ListISCSISessions to return iSCSI information for volumes in the cluster. """, cls=SolidFireCommand)
@pass_context
def listiscsisessions(ctx):
    """You can use ListISCSISessions to return iSCSI information for volumes in the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListISCSISessionsResult = ctx.element.list_iscsisessions()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListISCSISessionsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListISCSISessionsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listinterfaces', short_help="""ListNetworkInterfaces enables you to retrieve information about each network interface on a node. The API method is intended for use on individual nodes; userid and password authentication is required for access to individual nodes. """, cls=SolidFireCommand)
@pass_context
def listinterfaces(ctx):
    """ListNetworkInterfaces enables you to retrieve information about each network interface on a node. The API method is intended for use on individual nodes; userid and password authentication is required for access to individual nodes."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListNetworkInterfacesResult = ctx.element.list_network_interfaces()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListNetworkInterfacesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListNetworkInterfacesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

