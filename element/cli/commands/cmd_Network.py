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
    """ListFibreChannelPortInfo ListFibreChannelSessions ListISCSISessions ListNetworkInterfaces ListNodeFibreChannelPortInfo """
    ctx.sfapi = ctx.client

@cli.command('ListFibreChannelPortInfo', short_help="ListFibreChannelPortInfo")
@pass_context
def ListFibreChannelPortInfo(ctx):
    """The ListFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes."""



    ListFibreChannelPortInfoResult = ctx.element.list_fibre_channel_port_info()
    cli_utils.print_result(ListFibreChannelPortInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListFibreChannelSessions', short_help="ListFibreChannelSessions")
@pass_context
def ListFibreChannelSessions(ctx):
    """The ListFibreChannelSessions is used to return information about the active Fibre Channel sessions on a cluster."""



    ListFibreChannelSessionsResult = ctx.element.list_fibre_channel_sessions()
    cli_utils.print_result(ListFibreChannelSessionsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListISCSISessions', short_help="ListISCSISessions")
@pass_context
def ListISCSISessions(ctx):
    """ListISCSISessions is used to return iSCSI connection information for volumes in the cluster."""



    ListISCSISessionsResult = ctx.element.list_iscsisessions()
    cli_utils.print_result(ListISCSISessionsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListNetworkInterfaces', short_help="ListNetworkInterfaces")
@pass_context
def ListNetworkInterfaces(ctx):
    """The ListNetworkInterfaces API method is used to return information about each network interface on a node. The API method is intended for use on individual nodes. """



    ListNetworkInterfacesResult = ctx.element.list_network_interfaces()
    cli_utils.print_result(ListNetworkInterfacesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListNodeFibreChannelPortInfo', short_help="ListNodeFibreChannelPortInfo")
@pass_context
def ListNodeFibreChannelPortInfo(ctx):
    """The ListNodeFibreChannelPortInfo is used to return information about the Fibre Channel ports. The API method is intended for use on individual nodes; userid and password is required for access to individual Fibre Channel nodes."""



    ListNodeFibreChannelPortInfoResult = ctx.element.list_node_fibre_channel_port_info()
    cli_utils.print_result(ListNodeFibreChannelPortInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

