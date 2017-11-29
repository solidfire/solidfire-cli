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
    """modify add list remove """

@cli.command('modify', short_help="""You can use ModifyVirtualNetwork to change the attributes of an existing virtual network. This method enables you to add or remove address blocks, change the netmask, or modify the name or description of the virtual network. You can also use it to enable or disable namespaces, as well as add or remove a gateway if namespaces are enabled on the virtual network. Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both. Caution: Enabling or disabling the Routable Storage VLANs functionality for an existing virtual network by changing the "namespace" parameter disrupts any traffic handled by the virtual network. NetApp strongly recommends changing the "namespace" parameter only during a scheduled maintenance window. """, cls=SolidFireCommand)
@click.option('--virtualnetworkid',
              type=int,
              required=False,
              help="""The unique identifier of the virtual network to modify. This is the virtual network ID assigned by the cluster.  Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. """)
@click.option('--virtualnetworktag',
              type=int,
              required=False,
              help="""The network tag that identifies the virtual network to modify. Note: This parameter is optional but either virtualNetworkID or virtualNetworkTag must be specified with this API method. """)
@click.option('--name',
              type=str,
              required=False,
              help="""The new name for the virtual network. """)
@click.option('--addressblocks',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["start", "size", ],
              required=False,
              help="""The new addressBlock to set for this virtual network. This might contain new address blocks to add to the existing object or omit unused address blocks that need to be removed. Alternatively, you can extend or reduce the size of existing address blocks. You can only increase the size of the starting addressBlocks for a virtual network object; you can never decrease it. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer)  Has the following subparameters: --start --size """)
@click.option('--start',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Start of the IP address range. """,
              cls=SolidFireOption)
@click.option('--size',
              required=False,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Number of IP addresses to include in the block. """,
              cls=SolidFireOption)
@click.option('--netmask',
              type=str,
              required=False,
              help="""New network mask for this virtual network. """)
@click.option('--svip',
              type=str,
              required=False,
              help="""The storage virtual IP address for this virtual network. The svip for a virtual network cannot be changed. You must create a new virtual network to use a different svip address. """)
@click.option('--gateway',
              type=str,
              required=False,
              help="""The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. """)
@click.option('--namespace',
              type=bool,
              required=False,
              help="""When set to true, enables Routable Storage VLANs functionality by recreating the virtual network and configuring a namespace to contain it. When set to false, disables the VRF functionality for the virtual network. Changing this value disrupts traffic running through this virtual network. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""A new list of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def modify(ctx,
           # Optional main parameter
           virtualnetworkid = None,
           # Optional main parameter
           virtualnetworktag = None,
           # Optional main parameter
           name = None,
           # Optional main parameter
           addressblocks = None,
           # Optional subparameter of optional main parameter.
           start = None,
           # Optional subparameter of optional main parameter.
           size = None,
           # Optional main parameter
           netmask = None,
           # Optional main parameter
           svip = None,
           # Optional main parameter
           gateway = None,
           # Optional main parameter
           namespace = None,
           # Optional main parameter
           attributes = None):
    """You can use ModifyVirtualNetwork to change the attributes of an existing virtual network. This method enables you to add or remove"""
    """address blocks, change the netmask, or modify the name or description of the virtual network. You can also use it to enable or"""
    """disable namespaces, as well as add or remove a gateway if namespaces are enabled on the virtual network."""
    """Note: This method requires either the VirtualNetworkID or the VirtualNetworkTag as a parameter, but not both."""
    """Caution: Enabling or disabling the Routable Storage VLANs functionality for an existing virtual network by changing the"""
    """"namespace" parameter disrupts any traffic handled by the virtual network. NetApp strongly recommends changing the"""
    """"namespace" parameter only during a scheduled maintenance window."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    addressblocksArray = None
    if len(addressblocks) == 1 and start[0] is None and size[0] is None:
        addressblocksArray = []
    elif(addressblocks is not None and addressblocks != ()):
        addressblocksArray = []
        try:
            for i, _addressblocks in enumerate(addressblocks):
                addressblocksArray.append(AddressBlockParams(start=start[i], size=size[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    
    
    
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""virtualnetworkid = """+str(virtualnetworkid)+";" + """virtualnetworktag = """+str(virtualnetworktag)+";" + """name = """+str(name)+";" + """addressblocks = """+str(addressblocksArray)+";" + """netmask = """+str(netmask)+";" + """svip = """+str(svip)+";" + """gateway = """+str(gateway)+";" + """namespace = """+str(namespace)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _AddVirtualNetworkResult = ctx.element.modify_virtual_network(virtual_network_id=virtualnetworkid, virtual_network_tag=virtualnetworktag, name=name, address_blocks=addressblocksArray, netmask=netmask, svip=svip, gateway=gateway, namespace=namespace, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AddVirtualNetworkResult), indent=4))
        return
    else:
        cli_utils.print_result(_AddVirtualNetworkResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('add', short_help="""You can use the AddVirtualNetwork method to add a new virtual network to a cluster configuration. When you add a virtual network, an interface for each node is created and each interface will require a virtual network IP address. The number of IP addresses you specify as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. The system bulk provisions virtual network addresses and assigns them to individual nodes automatically. You do not need to assign virtual network addresses to nodes manually. Note: You can use AddVirtualNetwork only to create a new virtual network. If you want to make changes to an existing virtual network, use ModifyVirtualNetwork. Note: Virtual network parameters must be unique to each virtual network when setting the namespace parameter to false. """, cls=SolidFireCommand)
@click.option('--virtualnetworktag',
              type=int,
              required=True,
              prompt=True,
              help="""A unique virtual network (VLAN) tag. Supported values are 1 through 4094.The number zero (0) is not supported. """)
@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""A user-defined name for the new virtual network. """)
@click.option('--addressblocks',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["start", "size", ],
              required=True,
              help="""Unique range of IP addresses to include in the virtual network. Attributes for this parameter are: start: The start of the IP address range. (String) size: The number of IP addresses to include in the block. (Integer)  Has the following subparameters: --start --size """)
@click.option('--start',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Start of the IP address range. """,
              cls=SolidFireOption)
@click.option('--size',
              required=True,
              prompt=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Number of IP addresses to include in the block. """,
              cls=SolidFireOption)
@click.option('--netmask',
              type=str,
              required=True,
              prompt=True,
              help="""Unique network mask for the virtual network being created. """)
@click.option('--svip',
              type=str,
              required=True,
              prompt=True,
              help="""Unique storage IP address for the virtual network being created. """)
@click.option('--gateway',
              type=str,
              required=False,
              help="""The IP address of a gateway of the virtual network. This parameter is only valid if the "namespace" parameter is set to true. """)
@click.option('--namespace',
              type=bool,
              required=False,
              help="""When set to true, enables the Routable Storage VLANs functionality by creating and configuring a namespace and the virtual network contained by it. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def add(ctx,
           # Mandatory main parameter
           virtualnetworktag,
           # Mandatory main parameter
           name,
           # Mandatory main parameter
           addressblocks,
           # Mandatory main parameter
           netmask,
           # Mandatory main parameter
           svip,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           start,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           size,
           # Optional main parameter
           gateway = None,
           # Optional main parameter
           namespace = None,
           # Optional main parameter
           attributes = None):
    """You can use the AddVirtualNetwork method to add a new virtual network to a cluster configuration. When you add a virtual network,"""
    """an interface for each node is created and each interface will require a virtual network IP address. The number of IP addresses you"""
    """specify as a parameter for this API method must be equal to or greater than the number of nodes in the cluster. The system bulk"""
    """provisions virtual network addresses and assigns them to individual nodes automatically. You do not need to assign virtual"""
    """network addresses to nodes manually."""
    """Note: You can use AddVirtualNetwork only to create a new virtual network. If you want to make changes to an"""
    """existing virtual network, use ModifyVirtualNetwork."""
    """Note: Virtual network parameters must be unique to each virtual network when setting the namespace parameter to false."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    addressblocksArray = None
    if len(addressblocks) == 1 and start[0] is None and size[0] is None:
        addressblocksArray = []
    elif(addressblocks is not None and addressblocks != ()):
        addressblocksArray = []
        try:
            for i, _addressblocks in enumerate(addressblocks):
                addressblocksArray.append(AddressBlockParams(start=start[i], size=size[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    
    
    
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""virtualnetworktag = """ + str(virtualnetworktag)+";"+"""name = """ + str(name)+";"+"""addressblocks = """ + str(addressblocksArray)+";"+"""netmask = """ + str(netmask)+";"+"""svip = """ + str(svip)+";" + """gateway = """+str(gateway)+";" + """namespace = """+str(namespace)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _AddVirtualNetworkResult = ctx.element.add_virtual_network(virtual_network_tag=virtualnetworktag, name=name, address_blocks=addressblocksArray, netmask=netmask, svip=svip, gateway=gateway, namespace=namespace, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AddVirtualNetworkResult), indent=4))
        return
    else:
        cli_utils.print_result(_AddVirtualNetworkResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListVirtualNetworks enables you to list all configured virtual networks for the cluster. You can use this method to verify the virtual network settings in the cluster. There are no required parameters for this method. However, to filter the results, you can pass one or more VirtualNetworkID or VirtualNetworkTag values. """, cls=SolidFireCommand)
@click.option('--virtualnetworkid',
              type=int,
              required=False,
              help="""Network ID to filter the list for a single virtual network. """)
@click.option('--virtualnetworktag',
              type=int,
              required=False,
              help="""Network tag to filter the list for a single virtual network. """)
@click.option('--virtualnetworkids',
              type=str,
              required=False,
              help="""Network IDs to include in the list. """)
@click.option('--virtualnetworktags',
              type=str,
              required=False,
              help="""Network tag to include in the list. """)
@pass_context
def list(ctx,
           # Optional main parameter
           virtualnetworkid = None,
           # Optional main parameter
           virtualnetworktag = None,
           # Optional main parameter
           virtualnetworkids = None,
           # Optional main parameter
           virtualnetworktags = None):
    """ListVirtualNetworks enables you to list all configured virtual networks for the cluster. You can use this method to verify the virtual"""
    """network settings in the cluster."""
    """There are no required parameters for this method. However, to filter the results, you can pass one or more VirtualNetworkID or"""
    """VirtualNetworkTag values."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    virtualnetworkids = parser.parse_array(virtualnetworkids)
    

    virtualnetworktags = parser.parse_array(virtualnetworktags)
    

    ctx.logger.info(""": """"""virtualnetworkid = """+str(virtualnetworkid)+";" + """virtualnetworktag = """+str(virtualnetworktag)+";" + """virtualnetworkids = """+str(virtualnetworkids)+";" + """virtualnetworktags = """+str(virtualnetworktags)+""";"""+"")
    try:
        _ListVirtualNetworksResult = ctx.element.list_virtual_networks(virtual_network_id=virtualnetworkid, virtual_network_tag=virtualnetworktag, virtual_network_ids=virtualnetworkids, virtual_network_tags=virtualnetworktags)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListVirtualNetworksResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListVirtualNetworksResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""RemoveVirtualNetwork enables you to remove a previously added virtual network. Note: This method requires either the virtualNetworkID or the virtualNetworkTag as a parameter, but not both. """, cls=SolidFireCommand)
@click.option('--virtualnetworkid',
              type=int,
              required=False,
              help="""Network ID that identifies the virtual network to remove. """)
@click.option('--virtualnetworktag',
              type=int,
              required=False,
              help="""Network tag that identifies the virtual network to remove. """)
@pass_context
def remove(ctx,
           # Optional main parameter
           virtualnetworkid = None,
           # Optional main parameter
           virtualnetworktag = None):
    """RemoveVirtualNetwork enables you to remove a previously added virtual network."""
    """Note: This method requires either the virtualNetworkID or the virtualNetworkTag as a parameter, but not both."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""virtualnetworkid = """+str(virtualnetworkid)+";" + """virtualnetworktag = """+str(virtualnetworktag)+""";"""+"")
    try:
        _RemoveVirtualNetworkResult = ctx.element.remove_virtual_network(virtual_network_id=virtualnetworkid, virtual_network_tag=virtualnetworktag)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveVirtualNetworkResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveVirtualNetworkResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

