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
    """GetClusterInfo GetConfig GetNodeInfo GetNvramInfo """

@cli.command('GetClusterInfo', short_help="""You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI nodes and drives in the cluster. This generally includes manufacturers, vendors, versions, and other associated hardware identification information. """)
@click.option('--type',
              type=str,
              required=False,
              help="""Include only a certain type of hardware information in the response. Can be one of the following:drives: List only drive information in the response.nodes: List only node information in the response.all: Include both drive and node information in the response.If this parameter is omitted, a type of "all" is assumed. """)
@pass_context
def GetClusterInfo(ctx,
           type = None):
    """You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI nodes and drives in the cluster. This generally includes manufacturers, vendors, versions, and other associated hardware identification information."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetClusterHardwareInfoResult = ctx.element.get_cluster_hardware_info(type=type)
    cli_utils.print_result(GetClusterHardwareInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetConfig', short_help="""GetHardwareConfig enables you to display the hardware configuration information for a node. NOTE: This method is available only through the per-node API endpoint 5.0 or later. """)
@pass_context
def GetConfig(ctx):
    """GetHardwareConfig enables you to display the hardware configuration information for a node. NOTE: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetHardwareConfigResult = ctx.element.get_hardware_config()
    cli_utils.print_result(GetHardwareConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetNodeInfo', short_help="""GetNodeHardwareInfo is used to return all the hardware info and status for the node specified. This generally includes manufacturers, vendors, versions, and other associated hardware identification information. """)
@click.option('--node_id',
              type=int,
              required=True,
              help="""The ID of the node for which hardware information is being requested.  Information about a  node is returned if a   node is specified. """)
@pass_context
def GetNodeInfo(ctx,
           node_id):
    """GetNodeHardwareInfo is used to return all the hardware info and status for the node specified. This generally includes manufacturers, vendors, versions, and other associated hardware identification information."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetNodeHardwareInfoResult = ctx.element.get_node_hardware_info(node_id=node_id)
    cli_utils.print_result(GetNodeHardwareInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetNvramInfo', short_help="""GetNvramInfo allows you to retrieve information from each node about the NVRAM card.   """)
@pass_context
def GetNvramInfo(ctx):
    """GetNvramInfo allows you to retrieve information from each node about the NVRAM card.  """
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetNvramInfoResult = ctx.element.get_nvram_info()
    cli_utils.print_result(GetNvramInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

