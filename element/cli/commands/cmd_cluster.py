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
    """deleteinterfacepreference setsupplementaltlsciphers enableencryptionatrest disablemaintenancemode getlicensekey disableencryptionatrest getprotectiondomainlayout setntpinfo getmasternodeid getbinassignmentproperties getsslcertificate getstats getconfig removesslcertificate getntpinfo listinterfacepreferences getstructure getcapacity resetsupplementaltlsciphers getsystemstatus getlimits setprotectiondomainlayout getsupportedtlsciphers enablemaintenancemode createinterfacepreference listfaults listsyncjobs setsslcertificate setconfig listprotectiondomainlevels setstructure getstate deleteallsupportbundles getapi modifyinterfacepreference getinterfacepreference testaddressavailability getfullthreshold clearfaults modifyfullthreshold create getcompletestats checkproposednodeadditions getrawstats getversioninfo listevents getactivetlsciphers setlicensekey getinfo createsupportbundle """

@cli.command('deleteinterfacepreference', short_help="""Deletes an existing cluster interface preference. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""Name of the cluster interface preference. """)
@pass_context
def deleteinterfacepreference(ctx,
           # Mandatory main parameter
           name):
    """Deletes an existing cluster interface preference."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""name = """ + str(name)+""";"""+"")
    try:
        _DeleteClusterInterfacePreferenceResult = ctx.element.delete_cluster_interface_preference(name=name)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteClusterInterfacePreferenceResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteClusterInterfacePreferenceResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setsupplementaltlsciphers', short_help="""You can use the SetSupplementalTlsCiphers method to specify the list of supplemental TLS ciphers. """, cls=SolidFireCommand)
@click.option('--supplementalciphers',
              type=str,
              required=True,
              prompt=True,
              help="""The supplemental cipher suite names using the OpenSSL naming scheme. Use of cipher suite names is case-insensitive. """)
@pass_context
def setsupplementaltlsciphers(ctx,
           # Mandatory main parameter
           supplementalciphers):
    """You can use the SetSupplementalTlsCiphers method to specify the list of supplemental TLS ciphers."""

    

    cli_utils.establish_connection(ctx)
    

    supplementalciphers = parser.parse_array(supplementalciphers)
    

    

    ctx.logger.info(""": """"""supplementalciphers = """ + str(supplementalciphers)+""";"""+"")
    try:
        _SetSupplementalTlsCiphersResult = ctx.element.set_supplemental_tls_ciphers(supplemental_ciphers=supplementalciphers)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetSupplementalTlsCiphersResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetSupplementalTlsCiphersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enableencryptionatrest', short_help="""Initiate the process of setting a password on self-encrypting drives (SEDs) within the cluster.  This feature is not enabled by default but can be toggled on and off as needed. If a password is set on a SED which is removed from the cluster, the password will remain set and the drive is not secure erased.  Data can be secure erased using the SecureEraseDrives API method. Note: This does not affect performance or efficiency. If no parameters are specified, the password will be generated internally and at random (the only option for endpoints prior to 12.0).  This generated password will be distributed across the nodes using Shamir's Secret Sharing Algorithm such that at least two nodes are required to reconstruct the password.  The complete password to unlock the drives is not stored on any single node and is never sent across the network in its entirety.  This protects against the theft of any number of drives or a single node. If a keyProviderID is specified then the password will be generated/retrieved as appropriate per the type of provider.  Commonly this would be via a KMIP (Key Management Interoperability Protocol) Key Server in the case of a KMIP Key Provider (see CreateKeyProviderKmip).  After this operation the specified provider will be considered 'active' and will not be able to be deleted until DisableEncryptionAtRest is called. """, cls=SolidFireCommand)
@click.option('--keyproviderid',
              type=int,
              required=False,
              help="""The ID of a Key Provider to use.  This is a unique value returned as part of one of the CreateKeyProvider* methods. """)
@pass_context
def enableencryptionatrest(ctx,
           # Optional main parameter
           keyproviderid = None):
    """Initiate the process of setting a password on self-encrypting drives (SEDs) within the cluster.  This feature is not enabled by default but can be toggled on and off as needed."""
    """If a password is set on a SED which is removed from the cluster, the password will remain set and the drive is not secure erased.  Data can be secure erased using the SecureEraseDrives API method."""
    """Note: This does not affect performance or efficiency."""
    """If no parameters are specified, the password will be generated internally and at random (the only option for endpoints prior to 12.0).  This generated password will be distributed across the nodes using Shamir's Secret Sharing Algorithm such that at least two nodes are required to reconstruct the password.  The complete password to unlock the drives is not stored on any single node and is never sent across the network in its entirety.  This protects against the theft of any number of drives or a single node."""
    """If a keyProviderID is specified then the password will be generated/retrieved as appropriate per the type of provider.  Commonly this would be via a KMIP (Key Management Interoperability Protocol) Key Server in the case of a KMIP Key Provider (see CreateKeyProviderKmip).  After this operation the specified provider will be considered 'active' and will not be able to be deleted until DisableEncryptionAtRest is called."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""keyproviderid = """+str(keyproviderid)+""";"""+"")
    try:
        _EnableEncryptionAtRestResult = ctx.element.enable_encryption_at_rest(key_provider_id=keyproviderid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_EnableEncryptionAtRestResult), indent=4))
        return
    else:
        cli_utils.print_result(_EnableEncryptionAtRestResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('disablemaintenancemode', short_help="""Take a node out of maintenance mode. This should be called after maintenance is complete and the node is online. """, cls=SolidFireCommand)
@click.option('--nodes',
              type=str,
              required=True,
              prompt=True,
              help="""List of NodeIDs to take out of maintenance mode """)
@pass_context
def disablemaintenancemode(ctx,
           # Mandatory main parameter
           nodes):
    """Take a node out of maintenance mode. This should be called after maintenance is complete and the node is online."""

    

    cli_utils.establish_connection(ctx)
    

    nodes = parser.parse_array(nodes)
    

    

    ctx.logger.info(""": """"""nodes = """ + str(nodes)+""";"""+"")
    try:
        _MaintenanceModeResult = ctx.element.disable_maintenance_mode(nodes=nodes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_MaintenanceModeResult), indent=4))
        return
    else:
        cli_utils.print_result(_MaintenanceModeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getlicensekey', short_help="""You can use the GetLicenseKey method to get the current license key. """, cls=SolidFireCommand)
@pass_context
def getlicensekey(ctx):
    """You can use the GetLicenseKey method to get the current license key."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetLicenseKeyResult = ctx.element.get_license_key()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetLicenseKeyResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetLicenseKeyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('disableencryptionatrest', short_help="""Initiate the process of removing the password from self-encrypting drives (SEDs) within the cluster. """, cls=SolidFireCommand)
@pass_context
def disableencryptionatrest(ctx):
    """Initiate the process of removing the password from self-encrypting drives (SEDs) within the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _DisableEncryptionAtRestResult = ctx.element.disable_encryption_at_rest()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DisableEncryptionAtRestResult), indent=4))
        return
    else:
        cli_utils.print_result(_DisableEncryptionAtRestResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getprotectiondomainlayout', short_help="""GetProtectionDomainLayout returns all of the Protection Domain information for the cluster. """, cls=SolidFireCommand)
@pass_context
def getprotectiondomainlayout(ctx):
    """GetProtectionDomainLayout returns all of the Protection Domain information for the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetProtectionDomainLayoutResult = ctx.element.get_protection_domain_layout()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetProtectionDomainLayoutResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetProtectionDomainLayoutResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setntpinfo', short_help="""SetNtpInfo enables you to configure NTP on cluster nodes. The values you set with this interface apply to all nodes in the cluster. If an NTP broadcast server periodically broadcasts time information on your network, you can optionally configure nodes as broadcast clients. Note: NetApp recommends using NTP servers that are internal to your network, rather than the installation defaults. """, cls=SolidFireCommand)
@click.option('--servers',
              type=str,
              required=True,
              prompt=True,
              help="""List of NTP servers to add to each nodes NTP configuration. """)
@click.option('--broadcastclient',
              type=bool,
              required=False,
              help="""Enables every node in the cluster as a broadcast client. """)
@pass_context
def setntpinfo(ctx,
           # Mandatory main parameter
           servers,
           # Optional main parameter
           broadcastclient = None):
    """SetNtpInfo enables you to configure NTP on cluster nodes. The values you set with this interface apply to all nodes in the cluster. If an NTP broadcast server periodically broadcasts time information on your network, you can optionally configure nodes as broadcast clients."""
    """Note: NetApp recommends using NTP servers that are internal to your network, rather than the installation defaults."""

    

    cli_utils.establish_connection(ctx)
    

    servers = parser.parse_array(servers)
    
    

    

    ctx.logger.info(""": """"""servers = """ + str(servers)+";" + """broadcastclient = """+str(broadcastclient)+""";"""+"")
    try:
        _SetNtpInfoResult = ctx.element.set_ntp_info(servers=servers, broadcastclient=broadcastclient)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetNtpInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetNtpInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getmasternodeid', short_help="""GetClusterMasterNodeID enables you to retrieve the ID of the node that can perform cluster-wide administration tasks and holds the storage virtual IP address (SVIP) and management virtual IP address (MVIP). """, cls=SolidFireCommand)
@pass_context
def getmasternodeid(ctx):
    """GetClusterMasterNodeID enables you to retrieve the ID of the node that can perform cluster-wide administration tasks and holds the"""
    """storage virtual IP address (SVIP) and management virtual IP address (MVIP)."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClusterMasterNodeIDResult = ctx.element.get_cluster_master_node_id()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterMasterNodeIDResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterMasterNodeIDResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getbinassignmentproperties', short_help="""GetBinAssignmentProperties enables you to retrieve the bin assignment properties in the database. """, cls=SolidFireCommand)
@pass_context
def getbinassignmentproperties(ctx):
    """GetBinAssignmentProperties enables you to retrieve the bin assignment properties in the database."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetBinAssignmentPropertiesResult = ctx.element.get_bin_assignment_properties()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetBinAssignmentPropertiesResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetBinAssignmentPropertiesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsslcertificate', short_help="""You can use the GetSSLCertificate method to retrieve the SSL certificate that is currently active on the cluster. """, cls=SolidFireCommand)
@pass_context
def getsslcertificate(ctx):
    """You can use the GetSSLCertificate method to retrieve the SSL certificate that is currently active on the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetSSLCertificateResult = ctx.element.get_sslcertificate()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetSSLCertificateResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetSSLCertificateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstats', short_help="""GetClusterStats enables you to retrieve high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster. """, cls=SolidFireCommand)
@pass_context
def getstats(ctx):
    """GetClusterStats enables you to retrieve high-level activity measurements for the cluster. Values returned are cumulative from the"""
    """creation of the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClusterStatsResult = ctx.element.get_cluster_stats()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterStatsResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getconfig', short_help="""The GetClusterConfig API method enables you to return information about the cluster configuration this node uses to communicate with the cluster that it is a part of. """, cls=SolidFireCommand)
@pass_context
def getconfig(ctx):
    """The GetClusterConfig API method enables you to return information about the cluster configuration this node uses to communicate with the cluster that it is a part of."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClusterConfigResult = ctx.element.get_cluster_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('removesslcertificate', short_help="""You can use the RemoveSSLCertificate method to remove the user SSL certificate and private key for the cluster. After the certificate and private key are removed, the cluster is configured to use the default certificate and private key. """, cls=SolidFireCommand)
@pass_context
def removesslcertificate(ctx):
    """You can use the RemoveSSLCertificate method to remove the user SSL certificate and private key for the cluster."""
    """After the certificate and private key are removed, the cluster is configured to use the default certificate and private key."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _RemoveSSLCertificateResult = ctx.element.remove_sslcertificate()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveSSLCertificateResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveSSLCertificateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getntpinfo', short_help="""GetNtpInfo enables you to return the current network time protocol (NTP) configuration information. """, cls=SolidFireCommand)
@pass_context
def getntpinfo(ctx):
    """GetNtpInfo enables you to return the current network time protocol (NTP) configuration information."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetNtpInfoResult = ctx.element.get_ntp_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetNtpInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetNtpInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listinterfacepreferences', short_help="""Lists all the existing cluster interface preferences. """, cls=SolidFireCommand)
@pass_context
def listinterfacepreferences(ctx):
    """Lists all the existing cluster interface preferences."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListClusterInterfacePreferencesResult = ctx.element.list_cluster_interface_preferences()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListClusterInterfacePreferencesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListClusterInterfacePreferencesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstructure', short_help="""You can use the GetClusterStructure method to back up the current storage cluster configuration information. If the storage cluster configuration is changed while this method is running, the contents of the configuration backup will be unpredictable. You can save this data to a text file and restore it on other clusters, or the cluster in the case of a disaster. """, cls=SolidFireCommand)
@pass_context
def getstructure(ctx):
    """You can use the GetClusterStructure method to back up the current storage cluster configuration information. If the storage cluster configuration is changed while this method is running, the contents of the configuration backup will be unpredictable. You can save this data to a text file and restore it on other clusters, or the cluster in the case of a disaster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClusterStructureResult = ctx.element.get_cluster_structure()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterStructureResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterStructureResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getcapacity', short_help="""You can use the GetClusterCapacity method to return the high-level capacity measurements for an entire cluster. You can use the fields returned from this method to calculate the efficiency rates that are displayed in the Element OS Web UI. You can use the following calculations in scripts to return the efficiency rates for thin provisioning, deduplication, compression, and overall efficiency. """, cls=SolidFireCommand)
@pass_context
def getcapacity(ctx):
    """You can use the GetClusterCapacity method to return the high-level capacity measurements for an entire cluster. You can use the fields returned from this method to calculate the efficiency rates that are displayed in the Element OS Web UI. You can use the following calculations in scripts to return the efficiency rates for thin provisioning, deduplication, compression, and overall efficiency."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClusterCapacityResult = ctx.element.get_cluster_capacity()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterCapacityResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterCapacityResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('resetsupplementaltlsciphers', short_help="""You can use the ResetSupplementalTlsCiphers method to restore the supplemental ciphers to their defaults. """, cls=SolidFireCommand)
@pass_context
def resetsupplementaltlsciphers(ctx):
    """You can use the ResetSupplementalTlsCiphers method to restore the supplemental ciphers to their defaults."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ResetSupplementalTlsCiphersResult = ctx.element.reset_supplemental_tls_ciphers()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ResetSupplementalTlsCiphersResult), indent=4))
        return
    else:
        cli_utils.print_result(_ResetSupplementalTlsCiphersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsystemstatus', short_help="""GetSystemStatus enables you to return whether a reboot ir required or not. """, cls=SolidFireCommand)
@pass_context
def getsystemstatus(ctx):
    """GetSystemStatus enables you to return whether a reboot ir required or not."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetSystemStatusResult = ctx.element.get_system_status()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetSystemStatusResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetSystemStatusResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getlimits', short_help="""GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of Element OS, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools. Note: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method. """, cls=SolidFireCommand)
@pass_context
def getlimits(ctx):
    """GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of Element OS, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools."""
    """Note: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetLimitsResult = ctx.element.get_limits()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetLimitsResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetLimitsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setprotectiondomainlayout', short_help="""Used to assign Nodes to user-defined Protection Domains. This information must be provided for all Active Nodes in the cluster, and no information may be provided for Nodes that are not Active. All Nodes in a given Chassis must be assigned to the same user-defined Protection Domain. The same ProtectionDomainType must be supplied for all nodes. ProtectionDomainTypes that are not user-defined such as Node and Chassis, must not be included. If any of these are not true, the Custom Protection Domains will be ignored, and an appropriate error will be returned. """, cls=SolidFireCommand)
@click.option('--protectiondomainlayout',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["nodeid","protectiondomains"],
              required=True,
              help="""The Protection Domains for each Node.  Has the following subparameters: --nodeid --protectiondomains """)
@click.option('--nodeid',
              required=True,
              prompt=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The unique identifier for the node. """,
              cls=SolidFireOption)
@click.option('--protectiondomains',
              required=True,
              prompt=True,
              is_flag=True,
              multiple=True,
              subparameters = [ "protectiondomainname","protectiondomaintype" ,],
              help="""[subparameter] A ProtectionDomain is the Name and Type of a ProtectionDomain. Has the following subparamters: --protectiondomainname --protectiondomaintype""",
              cls=SolidFireOption
              )              
@click.option('--protectiondomainname',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The Protection Domain Name. """,
              cls=SolidFireOption)
@click.option('--protectiondomaintype',
              required=True,
              prompt=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The Protection Domain Type. """,
              cls=SolidFireOption)
@pass_context
def setprotectiondomainlayout(ctx,
           protectiondomainlayout,
           nodeid,
           protectiondomains,
           protectiondomainname,
           protectiondomaintype):
    """Used to assign Nodes to user-defined Protection Domains. This information must be provided for all"""
    """Active Nodes in the cluster, and no information may be provided for Nodes that are not Active. All Nodes"""
    """in a given Chassis must be assigned to the same user-defined Protection Domain. The same"""
    """ProtectionDomainType must be supplied for all nodes. ProtectionDomainTypes that are not user-defined"""
    """such as Node and Chassis, must not be included. If any of these are not true, the Custom Protection"""
    """Domains will be ignored, and an appropriate error will be returned."""

    

    cli_utils.establish_connection(ctx)

    # Creating ProtectionDomainObject
    protectionDomainArray = []
    for index in range(0,len(protectiondomainname)):
        protectionDomainList = []
        protectionDomain = ProtectionDomain(protection_domain_name=protectiondomainname[index],protection_domain_type=protectiondomaintype[index])
        protectionDomainList.append(protectionDomain)
        protectionDomainArray.append(protectionDomainList)

    # Creating ProtectionDomainLayout Object
    protectiondomainlayoutArray = None
    if len(protectiondomainlayout) == 1 and nodeid[0] is None and protectiondomainname[0] is None and protectiondomaintype[0] is None:
        protectiondomainlayoutArray = []
    elif(protectiondomainlayout is not None and protectiondomainlayout != ()):
        protectiondomainlayoutArray = []
        try:
            for i, _protectiondomainlayout in enumerate(protectiondomainlayout):
                protectiondomainlayoutArray.append(NodeProtectionDomains(node_id=nodeid[i], protection_domains=protectionDomainArray[i]))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    
    ctx.logger.info(""": """"""protectiondomainlayout = """ + str(protectiondomainlayoutArray)+""";"""+"")
    try:
        _SetProtectionDomainLayoutResult = ctx.element.set_protection_domain_layout(protection_domain_layout=protectiondomainlayoutArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetProtectionDomainLayoutResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetProtectionDomainLayoutResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsupportedtlsciphers', short_help="""You can use the GetSupportedTlsCiphers method to get a list of the supported TLS ciphers. """, cls=SolidFireCommand)
@pass_context
def getsupportedtlsciphers(ctx):
    """You can use the GetSupportedTlsCiphers method to get a list of the supported TLS ciphers."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetSupportedTlsCiphersResult = ctx.element.get_supported_tls_ciphers()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetSupportedTlsCiphersResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetSupportedTlsCiphersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enablemaintenancemode', short_help="""Prepare a node for maintenance. Maintenance includes anything that will require the node to be powered-off or restarted. """, cls=SolidFireCommand)
@click.option('--nodes',
              type=str,
              required=True,
              prompt=True,
              help="""List of NodeIDs to put in maintenance mode """)
@click.option('--perminuteprimaryswaplimit',
              type=int,
              required=False,
              help="""Number of primaries to swap per minute. If not specified, all will be swapped at once. """)
@click.option('--timeout',
              type=str,
              required=False,
              help="""How long to allow maintenance mode to remain enabled before automatically disabling. Formatted in HH:mm:ss. If not specified, it will remain enabled until explicitly disabled """)
@click.option('--forcewithunresolvedfaults',
              type=bool,
              required=False,
              help="""Force maintenance mode to be enabled even with blocking cluster faults present. """)
@pass_context
def enablemaintenancemode(ctx,
           # Mandatory main parameter
           nodes,
           # Optional main parameter
           perminuteprimaryswaplimit = None,
           # Optional main parameter
           timeout = None,
           # Optional main parameter
           forcewithunresolvedfaults = None):
    """Prepare a node for maintenance. Maintenance includes anything that will require the node to be powered-off or restarted."""

    

    cli_utils.establish_connection(ctx)
    

    nodes = parser.parse_array(nodes)
    
    
    
    

    

    ctx.logger.info(""": """"""nodes = """ + str(nodes)+";" + """perminuteprimaryswaplimit = """+str(perminuteprimaryswaplimit)+";" + """timeout = """+str(timeout)+";" + """forcewithunresolvedfaults = """+str(forcewithunresolvedfaults)+""";"""+"")
    try:
        _MaintenanceModeResult = ctx.element.enable_maintenance_mode(nodes=nodes, per_minute_primary_swap_limit=perminuteprimaryswaplimit, timeout=timeout, force_with_unresolved_faults=forcewithunresolvedfaults)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_MaintenanceModeResult), indent=4))
        return
    else:
        cli_utils.print_result(_MaintenanceModeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createinterfacepreference', short_help="""Creates a new cluster preference and stores it on the storage cluster. The ClusterInterfacePreference related APIs can be used by internal interfaces to the storage cluster such as HCI and UI to store arbitrary information in the cluster. Since the API calls in the UI are visible to customers, these APIs are made public. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""Name of the cluster interface preference. """)
@click.option('--value',
              type=str,
              required=True,
              prompt=True,
              help="""Value of the cluster interface preference. """)
@pass_context
def createinterfacepreference(ctx,
           # Mandatory main parameter
           name,
           # Mandatory main parameter
           value):
    """Creates a new cluster preference and stores it on the storage cluster. The ClusterInterfacePreference"""
    """related APIs can be used by internal interfaces to the storage cluster such as HCI and UI to store arbitrary"""
    """information in the cluster. Since the API calls in the UI are visible to customers, these APIs are made public."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""name = """ + str(name)+";"+"""value = """ + str(value)+""";"""+"")
    try:
        _CreateClusterInterfacePreferenceResult = ctx.element.create_cluster_interface_preference(name=name, value=value)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateClusterInterfacePreferenceResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateClusterInterfacePreferenceResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listfaults', short_help="""ListClusterFaults enables you to retrieve information about any faults detected on the cluster. With this method, you can retrieve both current faults as well as faults that have been resolved. The system caches faults every 30 seconds. """, cls=SolidFireCommand)
@click.option('--bestpractices',
              type=bool,
              required=False,
              help="""Specifies whether to include faults triggered by suboptimal system configuration. Possible values are: true false """)
@click.option('--faulttypes',
              type=str,
              required=False,
              help="""Determines the types of faults returned. Possible values are: current: List active, unresolved faults. resolved: List faults that were previously detected and resolved. all: (Default) List both current and resolved faults. You can see the fault status in the resolved field of the Cluster Fault object. """)
@pass_context
def listfaults(ctx,
           # Optional main parameter
           bestpractices = None,
           # Optional main parameter
           faulttypes = None):
    """ListClusterFaults enables you to retrieve information about any faults detected on the cluster. With this method, you can retrieve both current faults as well as faults that have been resolved. The system caches faults every 30 seconds."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""bestpractices = """+str(bestpractices)+";" + """faulttypes = """+str(faulttypes)+""";"""+"")
    try:
        _ListClusterFaultsResult = ctx.element.list_cluster_faults(best_practices=bestpractices, fault_types=faulttypes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListClusterFaultsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListClusterFaultsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listsyncjobs', short_help="""ListSyncJobs returns information about synchronization jobs that are running on a SolidFire cluster. The type of synchronization jobs that are returned with this method are block, slice, clone, and remote. """, cls=SolidFireCommand)
@pass_context
def listsyncjobs(ctx):
    """ListSyncJobs returns information about synchronization jobs that are running on a SolidFire cluster. The type of"""
    """synchronization jobs that are returned with this method are block, slice, clone, and remote."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListSyncJobsResult = ctx.element.list_sync_jobs()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSyncJobsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSyncJobsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setsslcertificate', short_help="""You can use the SetSSLCertificate method to set a user SSL certificate and a private key for the cluster. """, cls=SolidFireCommand)
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
    """You can use the SetSSLCertificate method to set a user SSL certificate and a private key for the cluster."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""certificate = """ + str(certificate)+";"+"""privatekey = """ + str(privatekey)+""";"""+"")
    try:
        _SetSSLCertificateResult = ctx.element.set_sslcertificate(certificate=certificate, private_key=privatekey)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetSSLCertificateResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetSSLCertificateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setconfig', short_help="""The SetClusterConfig API method enables you to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified, see Cluster Object Attributes. To display the current cluster interface settings for a node, run the GetClusterConfig API method. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)

@click.option('--cipi',
              type=str,
              required=False,
              help="""Network interface used for cluster communication. """)

@click.option('--clustercluster',
              type=str,
              required=False,
              help="""Unique cluster name. """)

@click.option('--ensemble',
              type=str,
              required=False,
              help="""Nodes that are participating in the cluster. """)

@click.option('--mipi',
              type=str,
              required=False,
              help="""Network interface used for node management. """)

@click.option('--name',
              type=str,
              required=False,
              help="""Unique cluster name. """)

@click.option('--nodeid',
              type=int,
              required=False,
              help=""" """)

@click.option('--pendingnodeid',
              type=int,
              required=False,
              help=""" """)

@click.option('--role',
              type=str,
              required=False,
              help="""Identifies the role of the node """)

@click.option('--sipi',
              type=str,
              required=False,
              help="""Network interface used for storage. """)

@click.option('--state',
              type=str,
              required=False,
              help=""" """)

@click.option('--encryptioncapable',
              type=bool,
              required=False,
              help="""This field indicates whether the node supports encryption. """)

@click.option('--fipsdriveconfiguration',
              type=bool,
              required=False,
              help="""This field indicates whether the node supports FIPS 140-2 certified drives. """)

@click.option('--haslocaladmin',
              type=bool,
              required=False,
              help=""" """)

@click.option('--version',
              type=str,
              required=False,
              help=""" """)
@pass_context
def setconfig(ctx,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           cipi = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clustercluster = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           ensemble = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           mipi = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           name = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           nodeid = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           pendingnodeid = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           role = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           sipi = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           state = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           encryptioncapable = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           fipsdriveconfiguration = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           haslocaladmin = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           version = None):
    """The SetClusterConfig API method enables you to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified, see Cluster Object Attributes. To display the current cluster"""
    """interface settings for a node, run the GetClusterConfig API method."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    cluster = None
    if(cipi is not None or
       clustercluster is not None or
       ensemble is not None or
       mipi is not None or
       name is not None or
       nodeid is not None or
       pendingnodeid is not None or
       role is not None or
       sipi is not None or
       state is not None or
       encryptioncapable is not None or
       fipsdriveconfiguration is not None or
       haslocaladmin is not None or
       version is not None or
       False):
        if not ( True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
""")
        kwargsDict = dict()
        kwargsDict["cipi"] = cipi
        kwargsDict["cluster"] = clustercluster
        kwargsDict["ensemble"] = ensemble
        kwargsDict["mipi"] = mipi
        kwargsDict["name"] = name
        kwargsDict["node_id"] = nodeid
        kwargsDict["pending_node_id"] = pendingnodeid
        kwargsDict["role"] = role
        kwargsDict["sipi"] = sipi
        kwargsDict["state"] = state
        kwargsDict["encryption_capable"] = encryptioncapable
        kwargsDict["fips_drive_configuration"] = fipsdriveconfiguration
        kwargsDict["has_local_admin"] = haslocaladmin
        kwargsDict["version"] = version

        cluster = ClusterConfig(**kwargsDict)
    

    

    ctx.logger.info(""": """"""cluster = """ + str(cluster)+""";"""+"")
    try:
        _SetClusterConfigResult = ctx.element.set_cluster_config(cluster=cluster)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetClusterConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetClusterConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listprotectiondomainlevels', short_help="""ListProtectionDomainLevels returns the Tolerance and Resiliency of the cluster from the perspective of each of the supported ProtectionDomainTypes. """, cls=SolidFireCommand)
@pass_context
def listprotectiondomainlevels(ctx):
    """ListProtectionDomainLevels returns the Tolerance and Resiliency of the cluster from the perspective"""
    """of each of the supported ProtectionDomainTypes."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListProtectionDomainLevelsResult = ctx.element.list_protection_domain_levels()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListProtectionDomainLevelsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListProtectionDomainLevelsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


# SetClusterStructure has been intentionally excluded from the python cli because
# the input values would be too complex to reasonably support in a CLI.


@cli.command('getstate', short_help="""The GetClusterState API method enables you to indicate if a node is part of a cluster or not. The three states are: Available: Node has not been configured with a cluster name. Pending: Node is pending for a specific named cluster and can be added. Active: Node is an active member of a cluster and may not be added to another cluster. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--force',
              type=bool,
              required=True,
              prompt=True,
              help="""To run this command, the force parameter must be set to true. """)
@pass_context
def getstate(ctx,
           # Mandatory main parameter
           force):
    """The GetClusterState API method enables you to indicate if a node is part of a cluster or not. The three states are:"""
    """Available: Node has not been configured with a cluster name."""
    """Pending: Node is pending for a specific named cluster and can be added."""
    """Active: Node is an active member of a cluster and may not be added to another"""
    """cluster."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""force = """ + str(force)+""";"""+"")
    try:
        _GetClusterStateResult = ctx.element.get_cluster_state(force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterStateResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterStateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('deleteallsupportbundles', short_help="""DeleteAllSupportBundles enables you to delete all support bundles generated with the CreateSupportBundle API method. """, cls=SolidFireCommand)
@pass_context
def deleteallsupportbundles(ctx):
    """DeleteAllSupportBundles enables you to delete all support bundles generated with the CreateSupportBundle API method."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _DeleteAllSupportBundlesResult = ctx.element.delete_all_support_bundles()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteAllSupportBundlesResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteAllSupportBundlesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getapi', short_help="""You can use the GetAPI method to return a list of all the API methods and supported API endpoints that can be used in the system. """, cls=SolidFireCommand)
@pass_context
def getapi(ctx):
    """You can use the GetAPI method to return a list of all the API methods and supported API endpoints that can be used in the system."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetAPIResult = ctx.element.get_api()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetAPIResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetAPIResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyinterfacepreference', short_help="""Modifies an existing cluster interface preference. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""Name of the cluster interface preference. """)
@click.option('--value',
              type=str,
              required=True,
              prompt=True,
              help="""Value of the cluster interface preference. """)
@pass_context
def modifyinterfacepreference(ctx,
           # Mandatory main parameter
           name,
           # Mandatory main parameter
           value):
    """Modifies an existing cluster interface preference."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""name = """ + str(name)+";"+"""value = """ + str(value)+""";"""+"")
    try:
        _ModifyClusterInterfacePreferenceResult = ctx.element.modify_cluster_interface_preference(name=name, value=value)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyClusterInterfacePreferenceResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyClusterInterfacePreferenceResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getinterfacepreference', short_help="""Retrieves an existing cluster interface preference. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""Name of the cluster interface preference. """)
@pass_context
def getinterfacepreference(ctx,
           # Mandatory main parameter
           name):
    """Retrieves an existing cluster interface preference."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""name = """ + str(name)+""";"""+"")
    try:
        _GetClusterInterfacePreferenceResult = ctx.element.get_cluster_interface_preference(name=name)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterInterfacePreferenceResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterInterfacePreferenceResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('testaddressavailability', short_help="""You can use the TestAddressAvailability method to check to see if a certain IP address is inuse on an interface within the storage cluster. """, cls=SolidFireCommand)
@click.option('--interface',
              type=str,
              required=True,
              prompt=True,
              help="""The target network interface (such as eth0, Bond10G, etc). """)
@click.option('--address',
              type=str,
              required=True,
              prompt=True,
              help="""The IP address to scan for on the target interface. """)
@click.option('--virtualnetworktag',
              type=int,
              required=False,
              help="""The target VLAN ID. """)
@click.option('--timeout',
              type=int,
              required=False,
              help="""The timeout in seconds for testing the target address. """)
@pass_context
def testaddressavailability(ctx,
           # Mandatory main parameter
           interface,
           # Mandatory main parameter
           address,
           # Optional main parameter
           virtualnetworktag = None,
           # Optional main parameter
           timeout = None):
    """You can use the TestAddressAvailability method to check to see if a certain IP address is inuse on an interface within the storage cluster."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    

    

    ctx.logger.info(""": """"""interface = """ + str(interface)+";"+"""address = """ + str(address)+";" + """virtualnetworktag = """+str(virtualnetworktag)+";" + """timeout = """+str(timeout)+""";"""+"")
    try:
        _TestAddressAvailabilityResult = ctx.element.test_address_availability(interface=interface, address=address, virtual_network_tag=virtualnetworktag, timeout=timeout)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestAddressAvailabilityResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestAddressAvailabilityResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getfullthreshold', short_help="""You can use GetClusterFullThreshold to view the stages set for cluster fullness levels. This method returns all fullness metrics for the cluster. Note: When a cluster reaches the Error stage of block cluster fullness, the maximum IOPS on all volumes are reduced linearly to the volume's minimum IOPS as the cluster approaches the Critical stage. This helps prevent the cluster from reaching the Critical stage of block cluster fullness. """, cls=SolidFireCommand)
@pass_context
def getfullthreshold(ctx):
    """You can use GetClusterFullThreshold to view the stages set for cluster fullness levels. This method returns all fullness metrics for the"""
    """cluster."""
    """Note: When a cluster reaches the Error stage of block cluster fullness, the maximum IOPS on all volumes are reduced linearly to the volume's minimum IOPS as the cluster approaches the Critical stage. This helps prevent the cluster from"""
    """reaching the Critical stage of block cluster fullness."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClusterFullThresholdResult = ctx.element.get_cluster_full_threshold()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterFullThresholdResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterFullThresholdResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('clearfaults', short_help="""You can use the ClearClusterFaults method to clear information about both current and previously detected faults. Both resolved and unresolved faults can be cleared. """, cls=SolidFireCommand)
@click.option('--faulttypes',
              type=str,
              required=False,
              help="""Determines the types of faults cleared. Possible values are: current: Faults that are currently detected and have not been resolved. resolved: (Default) Faults that were previously detected and resolved. all: Both current and resolved faults are cleared. The fault status can be determined by the resolved field of the fault object. """)
@pass_context
def clearfaults(ctx,
           # Optional main parameter
           faulttypes = None):
    """You can use the ClearClusterFaults method to clear information about both current and previously detected faults. Both resolved"""
    """and unresolved faults can be cleared."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""faulttypes = """+str(faulttypes)+""";"""+"")
    try:
        _ClearClusterFaultsResult = ctx.element.clear_cluster_faults(fault_types=faulttypes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ClearClusterFaultsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ClearClusterFaultsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyfullthreshold', short_help="""You can use ModifyClusterFullThreshold to change the level at which the system generates an event when the storage cluster approaches a certain capacity utilization. You can use the threshold settings to indicate the acceptable amount of utilized block storage or metadata storage before the system generates a warning. For example, if you want to be alerted when the system reaches 3% below the "Error" level block storage utilization, enter a value of "3" for the stage3BlockThresholdPercent parameter. If this level is reached, the system sends an alert to the Event Log in the Cluster Management Console. """, cls=SolidFireCommand)
@click.option('--stage2awarethreshold',
              type=int,
              required=False,
              help="""The number of nodes of capacity remaining in the cluster before the system triggers a capacity notification. """)
@click.option('--stage3blockthresholdpercent',
              type=int,
              required=False,
              help="""The percentage of block storage utilization below the "Error" threshold that causes the system to trigger a cluster "Warning" alert. """)
@click.option('--stage3metadatathresholdpercent',
              type=int,
              required=False,
              help="""The percentage of metadata storage utilization below the "Error" threshold that causes the system to trigger a cluster "Warning" alert. """)
@click.option('--maxmetadataoverprovisionfactor',
              type=int,
              required=False,
              help="""A value representative of the number of times metadata space can be overprovisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes can be created. """)
@pass_context
def modifyfullthreshold(ctx,
           # Optional main parameter
           stage2awarethreshold = None,
           # Optional main parameter
           stage3blockthresholdpercent = None,
           # Optional main parameter
           stage3metadatathresholdpercent = None,
           # Optional main parameter
           maxmetadataoverprovisionfactor = None):
    """You can use ModifyClusterFullThreshold to change the level at which the system generates an event when the storage cluster approaches a certain capacity utilization. You can use the threshold settings to indicate the acceptable amount of utilized block storage or metadata storage before the system generates a warning. For example, if you want to be alerted when the system reaches 3% below the "Error" level block storage utilization, enter a value of "3" for the stage3BlockThresholdPercent parameter. If this level is reached, the system sends an alert to the Event Log in the Cluster Management Console."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    

    

    ctx.logger.info(""": """"""stage2awarethreshold = """+str(stage2awarethreshold)+";" + """stage3blockthresholdpercent = """+str(stage3blockthresholdpercent)+";" + """stage3metadatathresholdpercent = """+str(stage3metadatathresholdpercent)+";" + """maxmetadataoverprovisionfactor = """+str(maxmetadataoverprovisionfactor)+""";"""+"")
    try:
        _ModifyClusterFullThresholdResult = ctx.element.modify_cluster_full_threshold(stage2_aware_threshold=stage2awarethreshold, stage3_block_threshold_percent=stage3blockthresholdpercent, stage3_metadata_threshold_percent=stage3metadatathresholdpercent, max_metadata_over_provision_factor=maxmetadataoverprovisionfactor)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyClusterFullThresholdResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyClusterFullThresholdResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""The CreateCluster method enables you to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the management IP (MIP) of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. You only need to use this method once each time a new cluster is initialized. Note: You need to log in to the node that is used as the master node for the cluster. After you log in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then, run the CreateCluster method. """, cls=SolidFireCommand)
@click.option('--accepteula',
              type=bool,
              required=False,
              help="""Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. """)
@click.option('--serialnumber',
              type=str,
              required=False,
              help="""Nine-digit alphanumeric Serial Number. May be required on software-based platforms. """)
@click.option('--ordernumber',
              type=str,
              required=False,
              help="""Alphanumeric sales order number. May be required on software-based platforms. """)
@click.option('--mvip',
              type=str,
              required=True,
              prompt=True,
              help="""Floating (virtual) IP address for the cluster on the management network. """)
@click.option('--svip',
              type=str,
              required=True,
              prompt=True,
              help="""Floating (virtual) IP address for the cluster on the storage (iSCSI) network. """)
@click.option('--username',
              type=str,
              required=True,
              prompt=True,
              help="""Username for the cluster admin. """)
@click.option('--password',
              type=str,
              required=True,
              prompt=True,
              help="""Initial password for the cluster admin account. """)
@click.option('--nodes',
              type=str,
              required=True,
              prompt=True,
              help="""CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@click.option('--enablesoftwareencryptionatrest',
              type=bool,
              required=False,
              help="""Enable this flag to use software-based encryption-at-rest. Defaults to true on SolidFire software-only clusters. Defaults to false on all other clusters. """)
@pass_context
def create(ctx,
           # Mandatory main parameter
           mvip,
           # Mandatory main parameter
           svip,
           # Mandatory main parameter
           username,
           # Mandatory main parameter
           password,
           # Mandatory main parameter
           nodes,
           # Optional main parameter
           accepteula = None,
           # Optional main parameter
           serialnumber = None,
           # Optional main parameter
           ordernumber = None,
           # Optional main parameter
           attributes = None,
           # Optional main parameter
           enablesoftwareencryptionatrest = None):
    """The CreateCluster method enables you to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the management IP (MIP) of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. You only need to use this method once each time a new cluster is initialized."""
    """Note: You need to log in to the node that is used as the master node for the cluster. After you log in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the"""
    """cluster. Then, run the CreateCluster method."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    
    
    

    nodes = parser.parse_array(nodes)
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    
    

    

    ctx.logger.info(""": """"""mvip = """ + str(mvip)+";"+"""svip = """ + str(svip)+";"+"""username = """ + str(username)+";"+"""password = """ + str(password)+";"+"""nodes = """ + str(nodes)+";" + """accepteula = """+str(accepteula)+";" + """serialnumber = """+str(serialnumber)+";" + """ordernumber = """+str(ordernumber)+";" + """attributes = """+str(kwargsDict)+";" + """enablesoftwareencryptionatrest = """+str(enablesoftwareencryptionatrest)+""";"""+"")
    try:
        _CreateClusterResult = ctx.element.create_cluster(mvip=mvip, svip=svip, username=username, password=password, nodes=nodes, accept_eula=accepteula, serial_number=serialnumber, order_number=ordernumber, attributes=kwargsDict, enable_software_encryption_at_rest=enablesoftwareencryptionatrest)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateClusterResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateClusterResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getcompletestats', short_help="""NetApp engineering uses the GetCompleteStats API method to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. NetApp does not recommend using GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster. """, cls=SolidFireCommand)
@pass_context
def getcompletestats(ctx):
    """NetApp engineering uses the GetCompleteStats API method to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. NetApp does not recommend using GetCompleteStats for collecting performance data or any other"""
    """management integration with a SolidFire cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _dict = ctx.element.get_complete_stats()
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



@cli.command('checkproposednodeadditions', short_help="""CheckProposedNodeAdditions validates that adding a node (or nodes) to an existing cluster is likely to succeed.  Any problems with the proposed new cluster are returned as errors with a human-readable description and unique error code. """, cls=SolidFireCommand)
@click.option('--nodes',
              type=str,
              required=True,
              prompt=True,
              help="""List of node IPs for the nodes that will be added to the cluster. """)
@pass_context
def checkproposednodeadditions(ctx,
           # Mandatory main parameter
           nodes):
    """CheckProposedNodeAdditions validates that adding a node (or nodes) to an existing cluster is likely to succeed.  Any problems with the proposed new cluster are returned as errors with a human-readable description and unique error code."""

    

    cli_utils.establish_connection(ctx)
    

    nodes = parser.parse_array(nodes)
    

    

    ctx.logger.info(""": """"""nodes = """ + str(nodes)+""";"""+"")
    try:
        _CheckProposedResult = ctx.element.check_proposed_node_additions(nodes=nodes)
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



@cli.command('getrawstats', short_help="""NetApp engineering uses the GetRawStats API method to troubleshoot new features. The data returned from GetRawStats is not documented, changes frequently, and is not guaranteed to be accurate. NetApp does not recommend using GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster. """, cls=SolidFireCommand)
@pass_context
def getrawstats(ctx):
    """NetApp engineering uses the GetRawStats API method to troubleshoot new features. The data returned from GetRawStats is not documented, changes frequently, and is not guaranteed to be accurate. NetApp does not recommend using GetCompleteStats for collecting performance data or any other"""
    """management integration with a SolidFire cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _dict = ctx.element.get_raw_stats()
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



@cli.command('getversioninfo', short_help="""GetClusterVersionInfo enables you to retrieve information about the Element software version running on each node in the cluster. This method also returns information about nodes that are currently in the process of upgrading software. """, cls=SolidFireCommand)
@pass_context
def getversioninfo(ctx):
    """GetClusterVersionInfo enables you to retrieve information about the Element software version running on each node in the cluster."""
    """This method also returns information about nodes that are currently in the process of upgrading software."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClusterVersionInfoResult = ctx.element.get_cluster_version_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterVersionInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterVersionInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listevents', short_help="""ListEvents returns events detected on the cluster, sorted from oldest to newest. """, cls=SolidFireCommand)
@click.option('--maxevents',
              type=int,
              required=False,
              help="""Specifies the maximum number of events to return. """)
@click.option('--starteventid',
              type=int,
              required=False,
              help="""Specifies the beginning of a range of events to return. """)
@click.option('--endeventid',
              type=int,
              required=False,
              help="""Specifies the end of a range of events to return. """)
@click.option('--eventtype',
              type=str,
              required=False,
              help="""Specifies the type of events to return. """)
@click.option('--serviceid',
              type=int,
              required=False,
              help="""Specifies that only events with this ServiceID will be returned. """)
@click.option('--nodeid',
              type=int,
              required=False,
              help="""Specifies that only events with this NodeID will be returned. """)
@click.option('--driveid',
              type=int,
              required=False,
              help="""Specifies that only events with this DriveID will be returned. """)
@click.option('--startreporttime',
              type=str,
              required=False,
              help="""Specifies that only events reported after this time will be returned. """)
@click.option('--endreporttime',
              type=str,
              required=False,
              help="""Specifies that only events reported earlier than this time will be returned. """)
@click.option('--startpublishtime',
              type=str,
              required=False,
              help="""Specifies that only events published after this time will be returned. """)
@click.option('--endpublishtime',
              type=str,
              required=False,
              help="""Specifies that only events published earlier than this time will be returned. """)
@pass_context
def listevents(ctx,
           # Optional main parameter
           maxevents = None,
           # Optional main parameter
           starteventid = None,
           # Optional main parameter
           endeventid = None,
           # Optional main parameter
           eventtype = None,
           # Optional main parameter
           serviceid = None,
           # Optional main parameter
           nodeid = None,
           # Optional main parameter
           driveid = None,
           # Optional main parameter
           startreporttime = None,
           # Optional main parameter
           endreporttime = None,
           # Optional main parameter
           startpublishtime = None,
           # Optional main parameter
           endpublishtime = None):
    """ListEvents returns events detected on the cluster, sorted from oldest to newest."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    
    
    
    
    
    
    

    

    ctx.logger.info(""": """"""maxevents = """+str(maxevents)+";" + """starteventid = """+str(starteventid)+";" + """endeventid = """+str(endeventid)+";" + """eventtype = """+str(eventtype)+";" + """serviceid = """+str(serviceid)+";" + """nodeid = """+str(nodeid)+";" + """driveid = """+str(driveid)+";" + """startreporttime = """+str(startreporttime)+";" + """endreporttime = """+str(endreporttime)+";" + """startpublishtime = """+str(startpublishtime)+";" + """endpublishtime = """+str(endpublishtime)+""";"""+"")
    try:
        _ListEventsResult = ctx.element.list_events(max_events=maxevents, start_event_id=starteventid, end_event_id=endeventid, event_type=eventtype, service_id=serviceid, node_id=nodeid, drive_id=driveid, start_report_time=startreporttime, end_report_time=endreporttime, start_publish_time=startpublishtime, end_publish_time=endpublishtime)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListEventsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListEventsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getactivetlsciphers', short_help="""You can use the GetActiveTlsCiphers method to get a list of the TLS ciphers that are currently accepted on the cluster. """, cls=SolidFireCommand)
@pass_context
def getactivetlsciphers(ctx):
    """You can use the GetActiveTlsCiphers method to get a list of the TLS ciphers that are currently accepted on the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetActiveTlsCiphersResult = ctx.element.get_active_tls_ciphers()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetActiveTlsCiphersResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetActiveTlsCiphersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setlicensekey', short_help="""You can use the SetLicenseKey method to set the SerialNumber And OrderNumber for the cluster. """, cls=SolidFireCommand)
@click.option('--serialnumber',
              type=str,
              required=True,
              prompt=True,
              help="""The new Serial Number for this cluster. """)
@click.option('--ordernumber',
              type=str,
              required=True,
              prompt=True,
              help="""The new sales order number for this cluster. """)
@pass_context
def setlicensekey(ctx,
           # Mandatory main parameter
           serialnumber,
           # Mandatory main parameter
           ordernumber):
    """You can use the SetLicenseKey method to set the SerialNumber And OrderNumber for the cluster."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""serialnumber = """ + str(serialnumber)+";"+"""ordernumber = """ + str(ordernumber)+""";"""+"")
    try:
        _SetLicenseKeyResult = ctx.element.set_license_key(serial_number=serialnumber, order_number=ordernumber)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetLicenseKeyResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetLicenseKeyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getinfo', short_help="""GetClusterInfo enables you to return configuration information about the cluster. """, cls=SolidFireCommand)
@pass_context
def getinfo(ctx):
    """GetClusterInfo enables you to return configuration information about the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClusterInfoResult = ctx.element.get_cluster_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createsupportbundle', short_help="""CreateSupportBundle enables you to create a support bundle file under the node's directory. After creation, the bundle is stored on the node as a tar.gz file. """, cls=SolidFireCommand)
@click.option('--bundlename',
              type=str,
              required=False,
              help="""The unique name for the support bundle. If no name is provided, "supportbundle" and the node name are used as the filename. """)
@click.option('--extraargs',
              type=str,
              required=False,
              help="""Passed to the sf_make_support_bundle script. You should use this parameter only at the request of NetApp SolidFire Support. """)
@click.option('--timeoutsec',
              type=int,
              required=False,
              help="""The number of seconds to allow the support bundle script to run before stopping. The default value is 1500 seconds. """)
@pass_context
def createsupportbundle(ctx,
           # Optional main parameter
           bundlename = None,
           # Optional main parameter
           extraargs = None,
           # Optional main parameter
           timeoutsec = None):
    """CreateSupportBundle enables you to create a support bundle file under the node's directory. After creation, the bundle is stored on the node as a tar.gz file."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    

    ctx.logger.info(""": """"""bundlename = """+str(bundlename)+";" + """extraargs = """+str(extraargs)+";" + """timeoutsec = """+str(timeoutsec)+""";"""+"")
    try:
        _CreateSupportBundleResult = ctx.element.create_support_bundle(bundle_name=bundlename, extra_args=extraargs, timeout_sec=timeoutsec)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateSupportBundleResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateSupportBundleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


