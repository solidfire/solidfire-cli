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
    """getnetworkconfig getconfig listactive getactivetlsciphers resetsupplementaltlsciphers controlpower listall setsslcertificate setnetworkconfig removesslcertificate getsslcertificate getpendingoperation setsupplementaltlsciphers getorigin getbootstrapconfig listpendingactive getfipsdrivesreport liststats listpending setconfig checkproposedcluster getstats add remove getsupportedtlsciphers """

@cli.command('getnetworkconfig', short_help="""The GetNetworkConfig API method enables you to display the network configuration information for a node. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def getnetworkconfig(ctx):
    """The GetNetworkConfig API method enables you to display the network configuration information for a node."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetNetworkConfigResult = ctx.element.get_network_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetNetworkConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetNetworkConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getconfig', short_help="""The GetConfig API method enables you to retrieve all configuration information for a node. This method includes the same information available in both the GetClusterConfig and GetNetworkConfig API methods. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def getconfig(ctx):
    """The GetConfig API method enables you to retrieve all configuration information for a node. This method includes the same information available in both the GetClusterConfig and GetNetworkConfig API methods."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetConfigResult = ctx.element.get_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listactive', short_help="""ListActiveNodes returns the list of currently active nodes that are in the cluster. """, cls=SolidFireCommand)
@pass_context
def listactive(ctx):
    """ListActiveNodes returns the list of currently active nodes that are in the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListActiveNodesResult = ctx.element.list_active_nodes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListActiveNodesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListActiveNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getactivetlsciphers', short_help="""You can use the GetNodeActiveTlsCiphers method to get a list of the TLS ciphers that are currently accepted on this node. You can use this method on both management and storage nodes. """, cls=SolidFireCommand)
@pass_context
def getactivetlsciphers(ctx):
    """You can use the GetNodeActiveTlsCiphers method to get a list of the TLS ciphers that are currently accepted on this node."""
    """You can use this method on both management and storage nodes."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetNodeActiveTlsCiphersResult = ctx.element.get_node_active_tls_ciphers()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetNodeActiveTlsCiphersResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetNodeActiveTlsCiphersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('resetsupplementaltlsciphers', short_help="""You can use the ResetNodeSupplementalTlsCiphers method to restore the supplemental ciphers to their defaults. You can use this command on management nodes. """, cls=SolidFireCommand)
@pass_context
def resetsupplementaltlsciphers(ctx):
    """You can use the ResetNodeSupplementalTlsCiphers method to restore the supplemental ciphers to their defaults."""
    """You can use this command on management nodes."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ResetNodeSupplementalTlsCiphersResult = ctx.element.reset_node_supplemental_tls_ciphers()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ResetNodeSupplementalTlsCiphersResult), indent=4))
        return
    else:
        cli_utils.print_result(_ResetNodeSupplementalTlsCiphersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('controlpower', short_help="""ControlPower can be used to reboot or halt a node. """, cls=SolidFireCommand)
@click.option('--action',
              type=str,
              required=True,
              prompt=True,
              help="""The action to take (Must be either Halt or Restart). """)
@click.option('--wakeupdelay',
              type=str,
              required=False,
              help="""The delay in seconds to wait before powering on.  This is only usable when action=Halt. """)
@click.option('--force',
              type=bool,
              required=True,
              prompt=True,
              help="""Required for the command to succeed. """)
@pass_context
def controlpower(ctx,
           # Mandatory main parameter
           action,
           # Mandatory main parameter
           force,
           # Optional main parameter
           wakeupdelay = None):
    """ControlPower can be used to reboot or halt a node."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    

    ctx.logger.info(""": """"""action = """ + str(action)+";"+"""force = """ + str(force)+";" + """wakeupdelay = """+str(wakeupdelay)+""";"""+"")
    try:
        _ControlPowerResult = ctx.element.control_power(action=action, force=force, wakeup_delay=wakeupdelay)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ControlPowerResult), indent=4))
        return
    else:
        cli_utils.print_result(_ControlPowerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listall', short_help="""ListAllNodes enables you to retrieve a list of active and pending nodes in the cluster. """, cls=SolidFireCommand)
@pass_context
def listall(ctx):
    """ListAllNodes enables you to retrieve a list of active and pending nodes in the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListAllNodesResult = ctx.element.list_all_nodes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListAllNodesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListAllNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setsslcertificate', short_help="""You can use the SetNodeSSLCertificate method to set a user SSL certificate and private key for the management node. """, cls=SolidFireCommand)
@click.option('--certificate',
              type=str,
              required=True,
              prompt=True,
              help="""The PEM-encoded text version of the certificate. """)
@click.option('--privatekey',
              type=str,
              required=True,
              prompt=True,
              help="""The PEM-encoded text version of the private key. """)
@pass_context
def setsslcertificate(ctx,
           # Mandatory main parameter
           certificate,
           # Mandatory main parameter
           privatekey):
    """You can use the SetNodeSSLCertificate method to set a user SSL certificate and private key for the management node."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""certificate = """ + str(certificate)+";"+"""privatekey = """ + str(privatekey)+""";"""+"")
    try:
        _SetNodeSSLCertificateResult = ctx.element.set_node_sslcertificate(certificate=certificate, private_key=privatekey)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetNodeSSLCertificateResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetNodeSSLCertificateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


# SetNewtorkConfig has been intentionally excluded from the python cli because
# the input values would be too complex to reasonably support in a CLI.


@cli.command('removesslcertificate', short_help="""You can use the RemoveNodeSSLCertificate method to remove the user SSL certificate and private key for the management node. After the certificate and private key are removed, the management node is configured to use the default certificate and private key.. """, cls=SolidFireCommand)
@pass_context
def removesslcertificate(ctx):
    """You can use the RemoveNodeSSLCertificate method to remove the user SSL certificate and private key for the management node."""
    """After the certificate and private key are removed, the management node is configured to use the default certificate and private key.."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _RemoveNodeSSLCertificateResult = ctx.element.remove_node_sslcertificate()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveNodeSSLCertificateResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveNodeSSLCertificateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsslcertificate', short_help="""You can use the GetNodeSSLCertificate method to retrieve the SSL certificate that is currently active on the cluster. You can use this method on both management and storage nodes. """, cls=SolidFireCommand)
@pass_context
def getsslcertificate(ctx):
    """You can use the GetNodeSSLCertificate method to retrieve the SSL certificate that is currently active on the cluster."""
    """You can use this method on both management and storage nodes."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetNodeSSLCertificateResult = ctx.element.get_node_sslcertificate()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetNodeSSLCertificateResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetNodeSSLCertificateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getpendingoperation', short_help="""You can use GetPendingOperation to detect an operation on a node that is currently in progress. You can also use this method to report back when an operation has completed.  Note: method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def getpendingoperation(ctx):
    """You can use GetPendingOperation to detect an operation on a node that is currently in progress. You can also use this method to report back when an operation has completed. """
    """Note: method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetPendingOperationResult = ctx.element.get_pending_operation()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetPendingOperationResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetPendingOperationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setsupplementaltlsciphers', short_help="""You can use the SetNodeSupplementalTlsCiphers method to specify the list of supplemental TLS ciphers for this node. You can use this command on management nodes. """, cls=SolidFireCommand)
@click.option('--supplementalciphers',
              type=str,
              required=True,
              prompt=True,
              help="""The supplemental cipher suite names using the OpenSSL naming scheme. Use of cipher suite names is case-insensitive. """)
@pass_context
def setsupplementaltlsciphers(ctx,
           # Mandatory main parameter
           supplementalciphers):
    """You can use the SetNodeSupplementalTlsCiphers method to specify the list of supplemental TLS ciphers for this node."""
    """You can use this command on management nodes."""

    

    cli_utils.establish_connection(ctx)
    

    supplementalciphers = parser.parse_array(supplementalciphers)
    

    

    ctx.logger.info(""": """"""supplementalciphers = """ + str(supplementalciphers)+""";"""+"")
    try:
        _SetNodeSupplementalTlsCiphersResult = ctx.element.set_node_supplemental_tls_ciphers(supplemental_ciphers=supplementalciphers)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetNodeSupplementalTlsCiphersResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetNodeSupplementalTlsCiphersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getorigin', short_help="""GetOrigin enables you to retrieve the origination certificate for where the node was built. This method might return null if there is no origination certification. """, cls=SolidFireCommand)
@pass_context
def getorigin(ctx):
    """GetOrigin enables you to retrieve the origination certificate for where the node was built. This method might return null if there is no origination certification."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetOriginResult = ctx.element.get_origin()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetOriginResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetOriginResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getbootstrapconfig', short_help="""GetBootstrapConfig returns cluster and node information from the bootstrap configuration file. Use this API method on an individual node before it has been joined with a cluster. You can use the information this method returns in the cluster configuration interface when you create a cluster. If a cluster has already been created, this can be used to obtain the MVIP and SVIP addresses of the cluster. """, cls=SolidFireCommand)
@pass_context
def getbootstrapconfig(ctx):
    """GetBootstrapConfig returns cluster and node information from the bootstrap configuration file. Use this API method on an individual node before it has been joined with a cluster. You can use the information this method returns in the cluster configuration interface when you create a cluster."""
    """If a cluster has already been created, this can be used to obtain the MVIP and SVIP addresses of the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetBootstrapConfigResult = ctx.element.get_bootstrap_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetBootstrapConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetBootstrapConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listpendingactive', short_help="""ListPendingActiveNodes returns the list of nodes in the cluster that are currently in the PendingActive state, between the pending and active states. These are nodes that are currently being returned to the factory image. """, cls=SolidFireCommand)
@pass_context
def listpendingactive(ctx):
    """ListPendingActiveNodes returns the list of nodes in the cluster that are currently in the PendingActive state, between the pending and active states. These are nodes that are currently being returned to the factory image."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListPendingActiveNodesResult = ctx.element.list_pending_active_nodes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListPendingActiveNodesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListPendingActiveNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getfipsdrivesreport', short_help="""The GetNodeFipsDrivesReport reports the FipsDrives capability of a node. This is a per-node API. """, cls=SolidFireCommand)
@pass_context
def getfipsdrivesreport(ctx):
    """The GetNodeFipsDrivesReport reports the FipsDrives capability of a node. This is a per-node API."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetNodeFipsDrivesReportResult = ctx.element.get_node_fips_drives_report()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetNodeFipsDrivesReportResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetNodeFipsDrivesReportResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('liststats', short_help="""ListNodeStats enables you to view the high-level activity measurements for all nodes in a cluster. """, cls=SolidFireCommand)
@pass_context
def liststats(ctx):
    """ListNodeStats enables you to view the high-level activity measurements for all nodes in a cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListNodeStatsResult = ctx.element.list_node_stats()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListNodeStatsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListNodeStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listpending', short_help="""ListPendingNodes returns a list of the currently pending nodes in the system. Pending nodes are nodes that are running and configured to join the cluster, but have not yet been added via the AddNodes API method. """, cls=SolidFireCommand)
@pass_context
def listpending(ctx):
    """ListPendingNodes returns a list of the currently pending nodes in the system. Pending nodes are nodes that are running and configured to join the cluster, but have not yet been added via the AddNodes API method."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListPendingNodesResult = ctx.element.list_pending_nodes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListPendingNodesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListPendingNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


# SetConfig has been intentionally excluded from the python cli because
# the input values would be too complex to reasonably support in a CLI.


@cli.command('checkproposedcluster', short_help="""CheckProposedCluster validates that creating a cluster from a given set of nodes is likely to succeed.  Any problems with the proposed cluster are returned as errors with a human-readable description and unique error code. """, cls=SolidFireCommand)
@click.option('--nodes',
              type=str,
              required=True,
              prompt=True,
              help="""List of node IPs for the nodes in the new cluster. """)
@pass_context
def checkproposedcluster(ctx,
           # Mandatory main parameter
           nodes):
    """CheckProposedCluster validates that creating a cluster from a given set of nodes is likely to succeed.  Any problems with the proposed cluster are returned as errors with a human-readable description and unique error code."""

    

    cli_utils.establish_connection(ctx)
    

    nodes = parser.parse_array(nodes)
    

    

    ctx.logger.info(""": """"""nodes = """ + str(nodes)+""";"""+"")
    try:
        _CheckProposedResult = ctx.element.check_proposed_cluster(nodes=nodes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CheckProposedResult), indent=4))
        return
    else:
        cli_utils.print_result(_CheckProposedResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstats', short_help="""GetNodeStats enables you to retrieve the high-level activity measurements for a single node. """, cls=SolidFireCommand)
@click.option('--nodeid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the node for which statistics are gathered. """)
@pass_context
def getstats(ctx,
           # Mandatory main parameter
           nodeid):
    """GetNodeStats enables you to retrieve the high-level activity measurements for a single node."""

    
    if ctx.json is True:
        ctx.logger.error("This command does not support the -j field. If you really need it, use sfapi invoke.")
        exit(1)

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""nodeid = """ + str(nodeid)+""";"""+"")
    try:
        _GetNodeStatsResult = ctx.element.get_node_stats(node_id=nodeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetNodeStatsResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetNodeStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('add', short_help="""AddNodes enables you to add one or more new nodes to a cluster. When a node that is not configured starts up for the first time, you are prompted to configure the node. After you configure the node, it is registered as a "pending node" with the cluster.  Note: It might take several seconds after adding a new node for it to start up and register its drives as available. """, cls=SolidFireCommand)
@click.option('--pendingnodes',
              type=str,
              required=True,
              prompt=True,
              help=""" List of pending NodeIDs for the nodes to be added. You can  obtain the list of pending nodes using the ListPendingNodes method. """)
@click.option('--autoinstall',
              type=bool,
              required=False,
              help="""If true, RTFI will be performed on the nodes.  The default behavior is to perform RTFI. """)
@pass_context
def add(ctx,
           # Mandatory main parameter
           pendingnodes,
           # Optional main parameter
           autoinstall = None):
    """AddNodes enables you to add one or more new nodes to a cluster. When a node that is not configured starts up for the first time, you are prompted to configure the node. After you configure the node, it is registered as a "pending node" with the cluster. """
    """Note: It might take several seconds after adding a new node for it to start up and register its drives as available."""

    

    cli_utils.establish_connection(ctx)
    

    pendingnodes = parser.parse_array(pendingnodes)
    
    

    

    ctx.logger.info(""": """"""pendingnodes = """ + str(pendingnodes)+";" + """autoinstall = """+str(autoinstall)+""";"""+"")
    try:
        _AddNodesResult = ctx.element.add_nodes(pending_nodes=pendingnodes, auto_install=autoinstall)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AddNodesResult), indent=4))
        return
    else:
        cli_utils.print_result(_AddNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""RemoveNodes can be used to remove one or more nodes from the cluster. Before removing a node, you must remove all drives from the node using the RemoveDrives method. You cannot remove a node until the RemoveDrives process has completed and all data has been migrated off of the node's drives. After removing a node, the removed node registers itself as a pending node. You can add the pending node again or shut it down (shutting the node down removes it from the Pending Node list).  RemoveNodes can fail with xEnsembleInvalidSize if removing the nodes would violate ensemble size restrictions. RemoveNodes can fail with xEnsembleQuorumLoss if removing the nodes would cause a loss of quorum. RemoveNodes can fail with xEnsembleToleranceChange if there are enabled data protection schemes that can tolerate multiple node failures and removing the nodes would decrease the ensemble's node failure tolerance. The optional ignoreEnsembleToleranceChange parameter can be set true to disable the ensemble tolerance check. """, cls=SolidFireCommand)
@click.option('--nodes',
              type=str,
              required=True,
              prompt=True,
              help="""List of NodeIDs for the nodes to be removed. """)
@click.option('--ignoreensembletolerancechange',
              type=bool,
              required=False,
              help="""Ignore changes to the ensemble's node failure tolerance when removing nodes. """)
@pass_context
def remove(ctx,
           # Mandatory main parameter
           nodes,
           # Optional main parameter
           ignoreensembletolerancechange = None):
    """RemoveNodes can be used to remove one or more nodes from the cluster. Before removing a node, you must remove all drives from the node using the RemoveDrives method. You cannot remove a node until the RemoveDrives process has completed and all data has been migrated off of the node's drives."""
    """After removing a node, the removed node registers itself as a pending node. You can add the pending node again or shut it down (shutting the node down removes it from the Pending Node list)."""
    """"""
    """RemoveNodes can fail with xEnsembleInvalidSize if removing the nodes would violate ensemble size restrictions."""
    """RemoveNodes can fail with xEnsembleQuorumLoss if removing the nodes would cause a loss of quorum."""
    """RemoveNodes can fail with xEnsembleToleranceChange if there are enabled data protection schemes that can tolerate multiple node failures and removing the nodes would decrease the ensemble's node failure tolerance. The optional ignoreEnsembleToleranceChange parameter can be set true to disable the ensemble tolerance check."""

    

    cli_utils.establish_connection(ctx)
    

    nodes = parser.parse_array(nodes)
    
    

    

    ctx.logger.info(""": """"""nodes = """ + str(nodes)+";" + """ignoreensembletolerancechange = """+str(ignoreensembletolerancechange)+""";"""+"")
    try:
        _RemoveNodesResult = ctx.element.remove_nodes(nodes=nodes, ignore_ensemble_tolerance_change=ignoreensembletolerancechange)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveNodesResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsupportedtlsciphers', short_help="""You can use the GetSupportedTlsCiphers method to get a list of the supported TLS ciphers on this node. You can use this method on both management and storage nodes. """, cls=SolidFireCommand)
@pass_context
def getsupportedtlsciphers(ctx):
    """You can use the GetSupportedTlsCiphers method to get a list of the supported TLS ciphers on this node."""
    """You can use this method on both management and storage nodes."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetNodeSupportedTlsCiphersResult = ctx.element.get_node_supported_tls_ciphers()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetNodeSupportedTlsCiphersResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetNodeSupportedTlsCiphersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


