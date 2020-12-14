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

class ProtectionSchemeVisibility(data_model.DataObject):
    """ProtectionSchemeVisibility  
    The public visibility of the protection scheme.

    """
    enum_values = ("customer", "testOnly", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class RemoteClusterSnapshotStatus(data_model.DataObject):
    """RemoteClusterSnapshotStatus  
    Status of the remote snapshot on the target cluster as seen on the source cluster

    """
    enum_values = ("Present", "Not Present", "Syncing", "Deleted", "Unknown", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class ProtectionSchemeCategory(data_model.DataObject):
    """ProtectionSchemeCategory  
    The category of the protection scheme.

    """
    enum_values = ("helix", "erasureCoded", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class ProtectionScheme(data_model.DataObject):
    """ProtectionScheme  
    The method of protecting data on the cluster

    """
    enum_values = ("singleHelix", "doubleHelix", "tripleHelix", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class AuthConfigType(data_model.DataObject):
    """AuthConfigType  
    This type indicates the configuration data which will be accessed or modified by the element auth container.

    """
    enum_values = ("mNode", "element", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class DriveEncryptionCapabilityType(data_model.DataObject):
    """DriveEncryptionCapabilityType  
    This specifies a drive's encryption capability.

    """
    enum_values = ("none", "sed", "fips", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class FipsDrivesStatusType(data_model.DataObject):
    """FipsDrivesStatusType  
    This specifies a node's FIPS 140-2 compliance status.

    """
    enum_values = ("None", "Partial", "Ready", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class AuthMethod(data_model.DataObject):
    """AuthMethod  
    This type qualifies a ClusterAdmin with its authentication method.

    """
    enum_values = ("Cluster", "Ldap", "Idp", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class MaintenanceMode(data_model.DataObject):
    """MaintenanceMode  
    Which mode a node is in when it is having maintenenace peformed.

    """
    enum_values = ("Disabled", "FailedToRecover", "Unexpected", "RecoveringFromMaintenance", "PreparingForMaintenance", "ReadyForMaintenance", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class ProposedNodeErrorCode(data_model.DataObject):
    """ProposedNodeErrorCode  
    This specifies error code for a proposed node addition.

    """
    enum_values = ("nodesNoCapacity", "nodesTooLarge", "nodesConnectFailed", "nodesQueryFailed", "nodesClusterMember", "nonFipsNodeCapable", "nonFipsDrivesCapable", "nodeTypeUnsupported", "nodeTypesHeterogeneous", "nodeTypeInvalid", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class VolumeAccess(data_model.DataObject):
    """VolumeAccess  
    Describes host access for a volume.

    """
    enum_values = ("locked", "readOnly", "readWrite", "replicationTarget", "snapMirrorTarget", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

class ProtectionDomainType(data_model.DataObject):
    """ProtectionDomainType  
    A Protection Domain is a set of one or more components whose simultaneous failure is protected
    from causing data unavailability or loss. This specifies one of the types of Protection Domains
    recognized by this cluster.

    """
    enum_values = ("node", "chassis", "custom", )

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def get_value(self):
        return self._value

@click.group()
@pass_context
def cli(ctx):
    """getclusterinfo getnodeinfo enablebmccoldreset getconfig disablebmccoldreset getnvraminfo getinfo """

@cli.command('getclusterinfo', short_help="""You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI nodes and drives in the cluster. This generally includes details about manufacturers, vendors, versions, and other associated hardware identification information. """, cls=SolidFireCommand)
@click.option('--type',
              type=str,
              required=False,
              help="""Includes only a certain type of hardware information in the response. Possible values are: drives: List only drive information in the response. nodes: List only node information in the response. all: Include both drive and node information in the response. If this parameter is omitted, a type of "all" is assumed. """)
@pass_context
def getclusterinfo(ctx,
           # Optional main parameter
           type = None):
    """You can use the GetClusterHardwareInfo method to retrieve the hardware status and information for all Fibre Channel nodes, iSCSI"""
    """nodes and drives in the cluster. This generally includes details about manufacturers, vendors, versions, and other associated hardware"""
    """identification information."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""type = """+str(type)+""";"""+"")
    try:
        _GetClusterHardwareInfoResult = ctx.element.get_cluster_hardware_info(type=type)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterHardwareInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterHardwareInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getnodeinfo', short_help="""GetNodeHardwareInfo enables you to return all the hardware information and status for the node specified. This generally includes details about manufacturers, vendors, versions, and other associated hardware identification information. """, cls=SolidFireCommand)
@click.option('--nodeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the node for which hardware information is being requested. Information about a Fibre Channel node is returned if a Fibre Channel node is specified. """)
@pass_context
def getnodeinfo(ctx,
           # Mandatory main parameter
           nodeid):
    """GetNodeHardwareInfo enables you to return all the hardware information and status for the node specified. This generally includes details about"""
    """manufacturers, vendors, versions, and other associated hardware identification information."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""nodeid = """ + str(nodeid)+""";"""+"")
    try:
        _GetNodeHardwareInfoResult = ctx.element.get_node_hardware_info(node_id=nodeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetNodeHardwareInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetNodeHardwareInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enablebmccoldreset', short_help="""EnableBmcColdReset enables a background task that periodically resets the Baseboard Management Controller (BMC) for all nodes in the cluster. """, cls=SolidFireCommand)
@click.option('--timeout',
              type=int,
              required=False,
              help="""If set, the time between BMC reset operations in minutes. The default is 20160 minutes. """)
@pass_context
def enablebmccoldreset(ctx,
           # Optional main parameter
           timeout = None):
    """EnableBmcColdReset enables a background task that periodically resets the Baseboard Management Controller (BMC) for all nodes in the cluster."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""timeout = """+str(timeout)+""";"""+"")
    try:
        _EnableBmcColdResetResult = ctx.element.enable_bmc_cold_reset(timeout=timeout)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_EnableBmcColdResetResult), indent=4))
        return
    else:
        cli_utils.print_result(_EnableBmcColdResetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getconfig', short_help="""GetHardwareConfig enables you to display the hardware configuration information for a node. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def getconfig(ctx):
    """GetHardwareConfig enables you to display the hardware configuration information for a node."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetHardwareConfigResult = ctx.element.get_hardware_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetHardwareConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetHardwareConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('disablebmccoldreset', short_help="""DisableBmcColdReset disables the background task that periodically resets the Baseboard Management Controller (BMC) for all nodes in the cluster. """, cls=SolidFireCommand)
@pass_context
def disablebmccoldreset(ctx):
    """DisableBmcColdReset disables the background task that periodically resets the Baseboard Management Controller (BMC) for all nodes in the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _DisableBmcColdResetResult = ctx.element.disable_bmc_cold_reset()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DisableBmcColdResetResult), indent=4))
        return
    else:
        cli_utils.print_result(_DisableBmcColdResetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getnvraminfo', short_help="""GetNvramInfo enables you to retrieve information from each node about the NVRAM card. """, cls=SolidFireCommand)
@click.option('--force',
              type=bool,
              required=False,
              help="""Required parameter to successfully run on all nodes in the cluster. """)
@pass_context
def getnvraminfo(ctx,
           # Optional main parameter
           force = None):
    """GetNvramInfo enables you to retrieve information from each node about the NVRAM card."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""force = """+str(force)+""";"""+"")
    try:
        _GetNvramInfoResult = ctx.element.get_nvram_info(force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetNvramInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetNvramInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getinfo', short_help="""The GetHardwareInfo API method enables you to return hardware information and status for a single node. This generally includes details about manufacturers, vendors, versions, drives, and other associated hardware identification information. """, cls=SolidFireCommand)
@pass_context
def getinfo(ctx):
    """The GetHardwareInfo API method enables you to return hardware information and status for a single node. This generally includes details about manufacturers, vendors, versions, drives, and other associated hardware identification information."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetHardwareInfoResult = ctx.element.get_hardware_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetHardwareInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetHardwareInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


