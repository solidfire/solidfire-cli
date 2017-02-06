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
    """modify add list remove """

@cli.command('modify', short_help="""ModifyVirtualNetwork is used to change various attributes of a VirtualNetwork object. This method can be used to add or remove address blocks, change the netmask IP, or modify the name or description of the virtual network.  Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both. """)
@click.option('--virtualnetworkid',
              type=int,
              required=False,
              help="""Unique identifier of the virtual network to modify. This is the virtual network ID assigned by the SolidFire cluster. """)
@click.option('--virtualnetworktag',
              type=int,
              required=False,
              help="""Network Tag that identifies the virtual network to modify. """)
@click.option('--name',
              type=str,
              required=False,
              help="""New name for the virtual network. """)
@click.option('--addressblocks',
              type=str,
              required=False,
              help="""Provide in json format: New addressBlock to set for this Virtual Network object. This may contain new address blocks to add to the existing object or it may omit unused address blocks that need to be removed. Alternatively, existing address blocks may be extended or reduced in size. The size of the starting addressBlocks for a Virtual Network object can only be increased, and can never be decreased. Attributes for this parameter are: start: start of the IP address range. (String) size: numbre of IP addresses to include in the block. (Integer) """)
@click.option('--netmask',
              type=str,
              required=False,
              help="""New netmask for this virtual network. """)
@click.option('--svip',
              type=str,
              required=False,
              help="""The storage virtual IP address for this virtual network. The svip for Virtual Network cannot be changed. A new Virtual Network must be created in order to use a different svip address. """)
@click.option('--gateway',
              type=str,
              required=False,
              help=""" """)
@click.option('--namespace',
              type=bool,
              required=False,
              help=""" """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: A new list of Name/Value pairs in JSON object format. """)
@pass_context
def modify(ctx,
           virtualnetworkid = None,
           virtualnetworktag = None,
           name = None,
           addressblocks = None,
           netmask = None,
           svip = None,
           gateway = None,
           namespace = None,
           attributes = None):
    """ModifyVirtualNetwork is used to change various attributes of a VirtualNetwork object. This method can be used to add or remove address blocks, change the netmask IP, or modify the name or description of the virtual network."""
    """"""
    """Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(addressblocks is not None):
        try:
            kwargsDict = simplejson.loads(addressblocks)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1) 
        addressblocks = [AddressBlock(**argsOfInterest) for argsOfInterest in kwargsDict]
    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1) 
        attributes = dict(**kwargsDict)
    

    ctx.logger.info("""virtualnetworkid = """+str(virtualnetworkid)+""";"""+"""virtualnetworktag = """+str(virtualnetworktag)+""";"""+"""name = """+str(name)+""";"""+"""addressblocks = """+str(addressblocks)+""";"""+"""netmask = """+str(netmask)+""";"""+"""svip = """+str(svip)+""";"""+"""gateway = """+str(gateway)+""";"""+"""namespace = """+str(namespace)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _AddVirtualNetworkResult = ctx.element.modify_virtual_network(virtual_network_id=virtualnetworkid, virtual_network_tag=virtualnetworktag, name=name, address_blocks=addressblocks, netmask=netmask, svip=svip, gateway=gateway, namespace=namespace, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_AddVirtualNetworkResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('add', short_help="""AddVirtualNetwork is used to add a new virtual network to a cluster configuration. When a virtual network is added, an interface for each node is created and each will require a virtual network IP address. The number of IP addresses specified as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. Virtual network addresses are bulk provisioned by SolidFire and assigned to individual nodes automatically. Virtual network addresses do not need to be assigned to nodes manually.  Note: The AddVirtualNetwork method is used only to create a new virtual network. If you want to make changes to a virtual network, please use the ModifyVirtualNetwork method. """)
@click.option('--virtualnetworktag',
              type=int,
              required=True,
              help="""A unique virtual network (VLAN) tag. Supported values are 1 to 4095 (the number zero (0) is not supported). """)
@click.option('--name',
              type=str,
              required=True,
              help="""User defined name for the new virtual network. """)
@click.option('--addressblocks',
              type=str,
              required=True,
              help="""Provide in json format: Unique Range of IP addresses to include in the virtual network. Attributes for this parameter are: start: start of the IP address range. (String) size: numbre of IP addresses to include in the block. (Integer) """)
@click.option('--netmask',
              type=str,
              required=True,
              help="""Unique netmask for the virtual network being created. """)
@click.option('--svip',
              type=str,
              required=True,
              help="""Unique storage IP address for the virtual network being created. """)
@click.option('--gateway',
              type=str,
              required=False,
              help=""" """)
@click.option('--namespace',
              type=bool,
              required=False,
              help=""" """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def add(ctx,
           virtualnetworktag,
           name,
           addressblocks,
           netmask,
           svip,
           gateway = None,
           namespace = None,
           attributes = None):
    """AddVirtualNetwork is used to add a new virtual network to a cluster configuration. When a virtual network is added, an interface for each node is created and each will require a virtual network IP address. The number of IP addresses specified as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. Virtual network addresses are bulk provisioned by SolidFire and assigned to individual nodes automatically. Virtual network addresses do not need to be assigned to nodes manually."""
    """"""
    """Note: The AddVirtualNetwork method is used only to create a new virtual network. If you want to make changes to a virtual network, please use the ModifyVirtualNetwork method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(addressblocks is not None):
        try:
            kwargsDict = simplejson.loads(addressblocks)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1) 
        addressblocks = [AddressBlock(**argsOfInterest) for argsOfInterest in kwargsDict]
    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1) 
        attributes = dict(**kwargsDict)
    

    ctx.logger.info("""virtualnetworktag = """+str(virtualnetworktag)+""";"""+"""name = """+str(name)+""";"""+"""addressblocks = """+str(addressblocks)+""";"""+"""netmask = """+str(netmask)+""";"""+"""svip = """+str(svip)+""";"""+"""gateway = """+str(gateway)+""";"""+"""namespace = """+str(namespace)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _AddVirtualNetworkResult = ctx.element.add_virtual_network(virtual_network_tag=virtualnetworktag, name=name, address_blocks=addressblocks, netmask=netmask, svip=svip, gateway=gateway, namespace=namespace, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_AddVirtualNetworkResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListVirtualNetworks is used to get a list of all the configured virtual networks for the cluster. This method can be used to verify the virtual network settings in the cluster.  This method does not require any parameters to be passed. But, one or more VirtualNetworkIDs or VirtualNetworkTags can be passed in order to filter the results. """)
@click.option('--virtualnetworkid',
              type=int,
              required=False,
              help="""Network ID to filter the list for a single virtual network """)
@click.option('--virtualnetworktag',
              type=int,
              required=False,
              help="""Network Tag to filter the list for a single virtual network """)
@click.option('--virtualnetworkids',
              type=str,
              required=False,
              help="""NetworkIDs to include in the list. """)
@click.option('--virtualnetworktags',
              type=str,
              required=False,
              help="""Network Tags to include in the list. """)
@pass_context
def list(ctx,
           virtualnetworkid = None,
           virtualnetworktag = None,
           virtualnetworkids = None,
           virtualnetworktags = None):
    """ListVirtualNetworks is used to get a list of all the configured virtual networks for the cluster. This method can be used to verify the virtual network settings in the cluster."""
    """"""
    """This method does not require any parameters to be passed. But, one or more VirtualNetworkIDs or VirtualNetworkTags can be passed in order to filter the results."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    virtualnetworkids = parser.parse_array(virtualnetworkids)

    virtualnetworktags = parser.parse_array(virtualnetworktags)
    

    ctx.logger.info("""virtualnetworkid = """+str(virtualnetworkid)+""";"""+"""virtualnetworktag = """+str(virtualnetworktag)+""";"""+"""virtualnetworkids = """+str(virtualnetworkids)+""";"""+"""virtualnetworktags = """+str(virtualnetworktags)+""";"""+"")
    try:
        _ListVirtualNetworksResult = ctx.element.list_virtual_networks(virtual_network_id=virtualnetworkid, virtual_network_tag=virtualnetworktag, virtual_network_ids=virtualnetworkids, virtual_network_tags=virtualnetworktags)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVirtualNetworksResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""RemoveVirtualNetwork is used to remove a previously added virtual network.  Note: This method requires either the VirtualNetworkID of the VirtualNetworkTag as a parameter, but not both. """)
@click.option('--virtualnetworkid',
              type=int,
              required=False,
              help="""Network ID that identifies the virtual network to remove. """)
@click.option('--virtualnetworktag',
              type=int,
              required=False,
              help="""Network Tag that identifies the virtual network to remove. """)
@pass_context
def remove(ctx,
           virtualnetworkid = None,
           virtualnetworktag = None):
    """RemoveVirtualNetwork is used to remove a previously added virtual network."""
    """"""
    """Note: This method requires either the VirtualNetworkID of the VirtualNetworkTag as a parameter, but not both."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""virtualnetworkid = """+str(virtualnetworkid)+""";"""+"""virtualnetworktag = """+str(virtualnetworktag)+""";"""+"")
    try:
        _RemoveVirtualNetworkResult = ctx.element.remove_virtual_network(virtual_network_id=virtualnetworkid, virtual_network_tag=virtualnetworktag)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_RemoveVirtualNetworkResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

