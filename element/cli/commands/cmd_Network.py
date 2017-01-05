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
    """ListFibreChannelPortInfo ListFibreChannelSessions ListISCSISessions ListInterfaces ListNodeFibreChannelPortInfo """

@cli.command('ListFibreChannelPortInfo', short_help="""The ListFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes. """)
@pass_context
def ListFibreChannelPortInfo(ctx):
    """The ListFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListFibreChannelPortInfoResult = ctx.element.list_fibre_channel_port_info()
    cli_utils.print_result(ListFibreChannelPortInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListFibreChannelSessions', short_help="""The ListFibreChannelSessions is used to return information about the active Fibre Channel sessions on a cluster. """)
@pass_context
def ListFibreChannelSessions(ctx):
    """The ListFibreChannelSessions is used to return information about the active Fibre Channel sessions on a cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListFibreChannelSessionsResult = ctx.element.list_fibre_channel_sessions()
    cli_utils.print_result(ListFibreChannelSessionsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListISCSISessions', short_help="""ListISCSISessions is used to return iSCSI connection information for volumes in the cluster. """)
@pass_context
def ListISCSISessions(ctx):
    """ListISCSISessions is used to return iSCSI connection information for volumes in the cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListISCSISessionsResult = ctx.element.list_iscsisessions()
    cli_utils.print_result(ListISCSISessionsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListInterfaces', short_help="""The ListNetworkInterfaces API method is used to return information about each network interface on a node. The API method is intended for use on individual nodes.  """)
@pass_context
def ListInterfaces(ctx):
    """The ListNetworkInterfaces API method is used to return information about each network interface on a node. The API method is intended for use on individual nodes. """
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListNetworkInterfacesResult = ctx.element.list_network_interfaces()
    cli_utils.print_result(ListNetworkInterfacesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListNodeFibreChannelPortInfo', short_help="""The ListNodeFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes. """)
@pass_context
def ListNodeFibreChannelPortInfo(ctx):
    """The ListNodeFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListNodeFibreChannelPortInfoResult = ctx.element.list_node_fibre_channel_port_info()
    cli_utils.print_result(ListNodeFibreChannelPortInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

