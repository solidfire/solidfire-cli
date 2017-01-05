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
from solidfire.models import *
from uuid import UUID
from element import exceptions


@click.group()
@pass_context
def cli(ctx):
    """AddAdmin ClearFaults Create CreateSupportBundle DeleteAllSupportBundles DisableEncryptionAtRest DisableSnmp EnableEncryptionAtRest EnableSnmp GetAPI GetCapacity GetConfig GetFullThreshold GetInfo GetMasterNodeID GetState GetStats GetVersionInfo GetCurrentAdmin GetLimits GetNtpInfo GetSnmpACL GetSnmpInfo GetSnmpState GetSnmpTrapInfo GetSystemStatus ListAdmins ListFaults ListEvents ListSyncJobs ModifyAdmin ModifyFullThreshold RemoveAdmin SetConfig SetNtpInfo SetSnmpACL SetSnmpInfo SetSnmpTrapInfo SnmpSendTestTraps """

@cli.command('AddAdmin', short_help="""AddClusterAdmin adds a new Cluster Admin. A Cluster Admin can be used to manage the cluster via the API and management tools. Cluster Admins are completely separate and unrelated to standard tenant accounts.  Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise. """)
@click.option('--username',
              type=str,
              required=True,
              help="""Unique username for this Cluster Admin. """)
@click.option('--password',
              type=str,
              required=True,
              help="""Password used to authenticate this Cluster Admin. """)
@click.option('--access',
              type=str,
              required=True,
              help="""Controls which methods this Cluster Admin can use. For more details on the levels of access, see "Access Control" in the Element API Guide. """)
@click.option('--accept_eula',
              type=bool,
              required=False,
              help="""Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def AddAdmin(ctx,
           username,
           password,
           access,
           accept_eula = None,
           attributes = None):
    """AddClusterAdmin adds a new Cluster Admin. A Cluster Admin can be used to manage the cluster via the API and management tools. Cluster Admins are completely separate and unrelated to standard tenant accounts."""
    """"""
    """Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    access = parser.parse_array(access)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    AddClusterAdminResult = ctx.element.add_cluster_admin(username=username, password=password, access=access, accept_eula=accept_eula, attributes=attributes)
    cli_utils.print_result(AddClusterAdminResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ClearFaults', short_help="""ClearClusterFaults is used to clear information about both current faults that are resolved as well as faults that were previously detected and resolved can be cleared. """)
@click.option('--fault_types',
              type=str,
              required=False,
              help="""Determines the types of faults cleared:<br/> <b>current</b>: Faults that are currently detected and have not been resolved.<br/> <b>resolved</b>: Faults that were previously detected and resolved.<br/> <b>all</b>: Both current and resolved faults are cleared. The fault status can be determined by the "resolved" field of the fault object. """)
@pass_context
def ClearFaults(ctx,
           fault_types = None):
    """ClearClusterFaults is used to clear information about both current faults that are resolved as well as faults that were previously detected and resolved can be cleared."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ClearClusterFaultsResult = ctx.element.clear_cluster_faults(fault_types=fault_types)
    cli_utils.print_result(ClearClusterFaultsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Create', short_help="""The CreateCluster method is used to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized.  Note: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method. """)
@click.option('--accept_eula',
              type=bool,
              required=False,
              help="""Indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. """)
@click.option('--mvip',
              type=str,
              required=True,
              help="""Floating (virtual) IP address for the cluster on the management network. """)
@click.option('--svip',
              type=str,
              required=True,
              help="""Floating (virtual) IP address for the cluster on the storage (iSCSI) network. """)
@click.option('--rep_count',
              type=int,
              required=True,
              help="""Number of replicas of each piece of data to store in the cluster. Valid value is "2". """)
@click.option('--username',
              type=str,
              required=True,
              help="""User name for the cluster admin. """)
@click.option('--password',
              type=str,
              required=True,
              help="""Initial password for the cluster admin account. """)
@click.option('--nodes',
              type=str,
              required=True,
              help="""CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Create(ctx,
           mvip,
           svip,
           rep_count,
           username,
           password,
           nodes,
           accept_eula = None,
           attributes = None):
    """The CreateCluster method is used to initialize the node in a cluster that has ownership of the &quot;mvip&quot; and &quot;svip&quot; addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized."""
    """"""
    """Note: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    nodes = parser.parse_array(nodes)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    CreateClusterResult = ctx.element.create_cluster(mvip=mvip, svip=svip, rep_count=rep_count, username=username, password=password, nodes=nodes, accept_eula=accept_eula, attributes=attributes)
    cli_utils.print_result(CreateClusterResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CreateSupportBundle', short_help="""CreateSupportBundle is used to create a support bundle file under the node's directory. When the bundle has been successfully created, the bundle is stored on the node as a tar.gz file. """)
@click.option('--bundle_name',
              type=str,
              required=False,
              help="""Unique name for each support bundle created. If no name is provided, then 'supportbundle' and the node name is used as a file name. """)
@click.option('--extra_args',
              type=str,
              required=False,
              help="""This parameter is fed to the sf_make_support_bundle script. Should be used only at the request of SolidFire Support. """)
@click.option('--timeout_sec',
              type=int,
              required=False,
              help="""The number of seconds to let the support bundle script run before timing out and stopping. Default is 1500 seconds. """)
@pass_context
def CreateSupportBundle(ctx,
           bundle_name = None,
           extra_args = None,
           timeout_sec = None):
    """CreateSupportBundle is used to create a support bundle file under the node's directory. When the bundle has been successfully created, the bundle is stored on the node as a tar.gz file."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    CreateSupportBundleResult = ctx.element.create_support_bundle(bundle_name=bundle_name, extra_args=extra_args, timeout_sec=timeout_sec)
    cli_utils.print_result(CreateSupportBundleResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('DeleteAllSupportBundles', short_help="""DeleteAllSupportBundles is used to delete all support bundles generated with the CreateSupportBundle API method. """)
@pass_context
def DeleteAllSupportBundles(ctx):
    """DeleteAllSupportBundles is used to delete all support bundles generated with the CreateSupportBundle API method."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    DeleteAllSupportBundlesResult = ctx.element.delete_all_support_bundles()
    cli_utils.print_result(DeleteAllSupportBundlesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('DisableEncryptionAtRest', short_help="""The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method. This disable method is asynchronous and returns a response before encryption is disabled. You can use the GetClusterInfo method to poll the system to see when the process has completed. """)
@pass_context
def DisableEncryptionAtRest(ctx):
    """The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method."""
    """This disable method is asynchronous and returns a response before encryption is disabled."""
    """You can use the GetClusterInfo method to poll the system to see when the process has completed."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    DisableEncryptionAtRestResult = ctx.element.disable_encryption_at_rest()
    cli_utils.print_result(DisableEncryptionAtRestResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('DisableSnmp', short_help="""DisableSnmp is used to disable SNMP on the cluster nodes. """)
@pass_context
def DisableSnmp(ctx):
    """DisableSnmp is used to disable SNMP on the cluster nodes."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    DisableSnmpResult = ctx.element.disable_snmp()
    cli_utils.print_result(DisableSnmpResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('EnableEncryptionAtRest', short_help="""The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed. Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need. Note: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed. """)
@pass_context
def EnableEncryptionAtRest(ctx):
    """The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed."""
    """Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need."""
    """Note: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    EnableEncryptionAtRestResult = ctx.element.enable_encryption_at_rest()
    cli_utils.print_result(EnableEncryptionAtRestResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('EnableSnmp', short_help="""EnableSnmp is used to enable SNMP on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp. """)
@click.option('--snmp_v3_enabled',
              type=bool,
              required=True,
              help="""If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled. """)
@pass_context
def EnableSnmp(ctx,
           snmp_v3_enabled):
    """EnableSnmp is used to enable SNMP on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    EnableSnmpResult = ctx.element.enable_snmp(snmp_v3_enabled=snmp_v3_enabled)
    cli_utils.print_result(EnableSnmpResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetAPI', short_help="""Retrieves the current version of the API and a list of all supported versions. """)
@pass_context
def GetAPI(ctx):
    """Retrieves the current version of the API and a list of all supported versions."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetAPIResult = ctx.element.get_api()
    cli_utils.print_result(GetAPIResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetCapacity', short_help="""Return the high-level capacity measurements for an entire cluster. The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface. """)
@pass_context
def GetCapacity(ctx):
    """Return the high-level capacity measurements for an entire cluster."""
    """The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetClusterCapacityResult = ctx.element.get_cluster_capacity()
    cli_utils.print_result(GetClusterCapacityResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetConfig', short_help="""The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of.  Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@pass_context
def GetConfig(ctx):
    """The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetClusterConfigResult = ctx.element.get_cluster_config()
    cli_utils.print_result(GetClusterConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetFullThreshold', short_help="""GetClusterFullThreshold is used to view the stages set for cluster fullness levels. All levels are returned when this method is entered. """)
@pass_context
def GetFullThreshold(ctx):
    """GetClusterFullThreshold is used to view the stages set for cluster fullness levels. All levels are returned when this method is entered."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetClusterFullThresholdResult = ctx.element.get_cluster_full_threshold()
    cli_utils.print_result(GetClusterFullThresholdResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetInfo', short_help="""Return configuration information about the cluster. """)
@pass_context
def GetInfo(ctx):
    """Return configuration information about the cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetClusterInfoResult = ctx.element.get_cluster_info()
    cli_utils.print_result(GetClusterInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetMasterNodeID', short_help="""GetClusterMasterNodeID is used to return the ID of the node that can perform cluster-wide administration tasks and holds the storage virtual IP (SVIP) and management virtual IP (MVIP). """)
@pass_context
def GetMasterNodeID(ctx):
    """GetClusterMasterNodeID is used to return the ID of the node that can perform cluster-wide administration tasks and holds the storage virtual IP (SVIP) and management virtual IP (MVIP)."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetClusterMasterNodeIDResult = ctx.element.get_cluster_master_node_id()
    cli_utils.print_result(GetClusterMasterNodeIDResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetState', short_help="""The GetClusterState method is used to indicate if a node is part of a cluster or not. The three states are: Available: Node has not been configured with a cluster name.Pending: Node is pending for a specific named cluster and can be added.Active: Node is active and a member of a cluster and may not be added to another cluster. """)
@click.option('--force',
              type=bool,
              required=True,
              help="""To run this command, the force parameter must be set to true. """)
@pass_context
def GetState(ctx,
           force):
    """The GetClusterState method is used to indicate if a node is part of a cluster or not. The three states are: Available: Node has not been configured with a cluster name.Pending: Node is pending for a specific named cluster and can be added.Active: Node is active and a member of a cluster and may not be added to another cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetClusterStateResult = ctx.element.get_cluster_state(force=force)
    cli_utils.print_result(GetClusterStateResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetStats', short_help="""GetClusterStats is used to return high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster. """)
@pass_context
def GetStats(ctx):
    """GetClusterStats is used to return high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetClusterStatsResult = ctx.element.get_cluster_stats()
    cli_utils.print_result(GetClusterStatsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetVersionInfo', short_help="""Return information about the Element software version running on each node in the cluster. Information about the nodes that are currently in the process of upgrading software is also returned. """)
@pass_context
def GetVersionInfo(ctx):
    """Return information about the Element software version running on each node in the cluster."""
    """Information about the nodes that are currently in the process of upgrading software is also returned."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetClusterVersionInfoResult = ctx.element.get_cluster_version_info()
    cli_utils.print_result(GetClusterVersionInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetCurrentAdmin', short_help="""GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was ncreated when the cluster was created. """)
@pass_context
def GetCurrentAdmin(ctx):
    """GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was ncreated when the cluster was created."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetCurrentClusterAdminResult = ctx.element.get_current_cluster_admin()
    cli_utils.print_result(GetCurrentClusterAdminResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetLimits', short_help="""GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of  Element, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools.NOTE: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method. """)
@pass_context
def GetLimits(ctx):
    """GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of  Element, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools.NOTE: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetLimitsResult = ctx.element.get_limits()
    cli_utils.print_result(GetLimitsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetNtpInfo', short_help="""GetNtpInfo is used to return the current network time protocol (NTP) configuration information. """)
@pass_context
def GetNtpInfo(ctx):
    """GetNtpInfo is used to return the current network time protocol (NTP) configuration information."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetNtpInfoResult = ctx.element.get_ntp_info()
    cli_utils.print_result(GetNtpInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetSnmpACL', short_help="""GetSnmpACL is used to return the current SNMP access permissions on the cluster nodes. """)
@pass_context
def GetSnmpACL(ctx):
    """GetSnmpACL is used to return the current SNMP access permissions on the cluster nodes."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetSnmpACLResult = ctx.element.get_snmp_acl()
    cli_utils.print_result(GetSnmpACLResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetSnmpInfo', short_help="""GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information.  Note: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage. """)
@pass_context
def GetSnmpInfo(ctx):
    """GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information."""
    """"""
    """Note: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetSnmpInfoResult = ctx.element.get_snmp_info()
    cli_utils.print_result(GetSnmpInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetSnmpState', short_help="""GetSnmpState is used to return the current state of the SNMP feature.  Note: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future. """)
@pass_context
def GetSnmpState(ctx):
    """GetSnmpState is used to return the current state of the SNMP feature."""
    """"""
    """Note: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetSnmpStateResult = ctx.element.get_snmp_state()
    cli_utils.print_result(GetSnmpStateResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetSnmpTrapInfo', short_help="""GetSnmpTrapInfo is used to return current SNMP trap configuration information. """)
@pass_context
def GetSnmpTrapInfo(ctx):
    """GetSnmpTrapInfo is used to return current SNMP trap configuration information."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetSnmpTrapInfoResult = ctx.element.get_snmp_trap_info()
    cli_utils.print_result(GetSnmpTrapInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetSystemStatus', short_help="""""")
@pass_context
def GetSystemStatus(ctx):
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetSystemStatusResult = ctx.element.get_system_status()
    cli_utils.print_result(GetSystemStatusResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListAdmins', short_help="""ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrators that have different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. LDAP administrators can also be created when setting up an LDAP system on the cluster. """)
@pass_context
def ListAdmins(ctx):
    """ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrators that have different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. LDAP administrators can also be created when setting up an LDAP system on the cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListClusterAdminsResult = ctx.element.list_cluster_admins()
    cli_utils.print_result(ListClusterAdminsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListFaults', short_help="""ListClusterFaults is used to retrieve information about any faults detected on the cluster. With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds. """)
@click.option('--exceptions',
              type=bool,
              required=False,
              help="""""")
@click.option('--best_practices',
              type=bool,
              required=False,
              help="""Include faults triggered by sub-optimal system configuration. Possible values: true, false """)
@click.option('--update',
              type=bool,
              required=False,
              help="""""")
@click.option('--fault_types',
              type=str,
              required=False,
              help="""Determines the types of faults returned: current: List active, unresolved faults. <b>resolved</b>: List faults that were previously detected and resolved. <b>all</b>: (Default) List both current and resolved faults. You can see the fault status in the 'resolved' field of the Cluster Fault object. """)
@pass_context
def ListFaults(ctx,
           exceptions = None,
           best_practices = None,
           update = None,
           fault_types = None):
    """ListClusterFaults is used to retrieve information about any faults detected on the cluster."""
    """With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListClusterFaultsResult = ctx.element.list_cluster_faults(exceptions=exceptions, best_practices=best_practices, update=update, fault_types=fault_types)
    cli_utils.print_result(ListClusterFaultsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListEvents', short_help="""ListEvents returns events detected on the cluster, sorted from oldest to newest. """)
@click.option('--max_events',
              type=int,
              required=False,
              help="""Specifies the maximum number of events to return. """)
@click.option('--start_event_id',
              type=int,
              required=False,
              help="""Identifies the beginning of a range of events to return. """)
@click.option('--end_event_id',
              type=int,
              required=False,
              help="""Identifies the end of a range of events to return. """)
@click.option('--event_queue_type',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListEvents(ctx,
           max_events = None,
           start_event_id = None,
           end_event_id = None,
           event_queue_type = None):
    """ListEvents returns events detected on the cluster, sorted from oldest to newest."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListEventsResult = ctx.element.list_events(max_events=max_events, start_event_id=start_event_id, end_event_id=end_event_id, event_queue_type=event_queue_type)
    cli_utils.print_result(ListEventsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListSyncJobs', short_help="""ListSyncJobs is used to return information about synchronization jobs that are running on a SolidFire cluster. Synchronization jobs that are returned with this method are, "slice," "clone" and "remote." """)
@pass_context
def ListSyncJobs(ctx):
    """ListSyncJobs is used to return information about synchronization jobs that are running on a SolidFire cluster. Synchronization jobs that are returned with this method are, &quot;slice,&quot; &quot;clone&quot; and &quot;remote.&quot;"""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListSyncJobsResult = ctx.element.list_sync_jobs()
    cli_utils.print_result(ListSyncJobsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ModifyAdmin', short_help="""ModifyClusterAdmin is used to change the settings for a Cluster Admin or LDAP Cluster Admin. Access for the administrator Cluster Admin account cannot be changed. """)
@click.option('--cluster_admin_id',
              type=int,
              required=True,
              help="""ClusterAdminID for the Cluster Admin or LDAP Cluster Admin to modify. """)
@click.option('--password',
              type=str,
              required=False,
              help="""Password used to authenticate this Cluster Admin. """)
@click.option('--access',
              type=str,
              required=False,
              help="""Controls which methods this Cluster Admin can use. For more details on the levels of access, see "Access Control" in the Element API Guide. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def ModifyAdmin(ctx,
           cluster_admin_id,
           password = None,
           access = None,
           attributes = None):
    """ModifyClusterAdmin is used to change the settings for a Cluster Admin or LDAP Cluster Admin. Access for the administrator Cluster Admin account cannot be changed."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    access = parser.parse_array(access)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ModifyClusterAdminResult = ctx.element.modify_cluster_admin(cluster_admin_id=cluster_admin_id, password=password, access=access, attributes=attributes)
    cli_utils.print_result(ModifyClusterAdminResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ModifyFullThreshold', short_help="""ModifyClusterFullThreshold is used to change the level at which an event is generated when the storage cluster approaches the capacity utilization requested. The number entered in this setting is used to indicate the number of node failures the system is required to recover from. For example, on a 10 node cluster, if you want to be alerted when the system cannot recover from 3 nodes failures, enter the value of "3". When this number is reached, a message alert is sent to the Event Log in the Cluster Management Console. """)
@click.option('--stage2_aware_threshold',
              type=int,
              required=False,
              help="""Number of nodes worth of capacity remaining on the cluster that triggers a notification. """)
@click.option('--stage3_block_threshold_percent',
              type=int,
              required=False,
              help="""Percent below "Error" state to raise a cluster "Warning" alert. """)
@click.option('--max_metadata_over_provision_factor',
              type=int,
              required=False,
              help="""A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. """)
@pass_context
def ModifyFullThreshold(ctx,
           stage2_aware_threshold = None,
           stage3_block_threshold_percent = None,
           max_metadata_over_provision_factor = None):
    """ModifyClusterFullThreshold is used to change the level at which an event is generated when the storage cluster approaches the capacity utilization requested. The number entered in this setting is used to indicate the number of node failures the system is required to recover from. For example, on a 10 node cluster, if you want to be alerted when the system cannot recover from 3 nodes failures, enter the value of &quot;3&quot;. When this number is reached, a message alert is sent to the Event Log in the Cluster Management Console."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ModifyClusterFullThresholdResult = ctx.element.modify_cluster_full_threshold(stage2_aware_threshold=stage2_aware_threshold, stage3_block_threshold_percent=stage3_block_threshold_percent, max_metadata_over_provision_factor=max_metadata_over_provision_factor)
    cli_utils.print_result(ModifyClusterFullThresholdResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveAdmin', short_help="""RemoveClusterAdmin is used to remove a Cluster Admin. The "admin" Cluster Admin cannot be removed. """)
@click.option('--cluster_admin_id',
              type=int,
              required=True,
              help="""ClusterAdminID for the Cluster Admin to remove. """)
@pass_context
def RemoveAdmin(ctx,
           cluster_admin_id):
    """RemoveClusterAdmin is used to remove a Cluster Admin. The &quot;admin&quot; Cluster Admin cannot be removed."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    RemoveClusterAdminResult = ctx.element.remove_cluster_admin(cluster_admin_id=cluster_admin_id)
    cli_utils.print_result(RemoveClusterAdminResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SetConfig', short_help="""The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method.  Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@click.option('--cluster_config_cipi',
              type=str,
              required=False,
              help="""Network interface used for cluster communication. """)
@click.option('--cluster_config_cluster',
              type=str,
              required=False,
              help="""Unique cluster name. """)
@click.option('--cluster_config_ensemble',
              type=str,
              required=False,
              help="""Nodes that are participating in the cluster. """)
@click.option('--cluster_config_mipi',
              type=str,
              required=False,
              help="""Network interface used for node management. """)
@click.option('--cluster_config_name',
              type=str,
              required=False,
              help="""Unique cluster name. """)
@click.option('--cluster_config_node_id',
              type=int,
              required=False,
              help="""""")
@click.option('--cluster_config_pending_node_id',
              type=int,
              required=False,
              help="""""")
@click.option('--cluster_config_role',
              type=str,
              required=False,
              help="""Identifies the role of the node """)
@click.option('--cluster_config_sipi',
              type=str,
              required=False,
              help="""Network interface used for storage. """)
@click.option('--cluster_config_state',
              type=str,
              required=False,
              help="""""")
@pass_context
def SetConfig(ctx,
           cluster_config_cipi = None,
           cluster_config_cluster = None,
           cluster_config_ensemble = None,
           cluster_config_mipi = None,
           cluster_config_name = None,
           cluster_config_node_id = None,
           cluster_config_pending_node_id = None,
           cluster_config_role = None,
           cluster_config_sipi = None,
           cluster_config_state = None):
    """The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    cluster = None
    if(cluster is not None or False):
        kwargsDict = dict()
        kwargsDict["cipi"] = cluster_config_cipi
        kwargsDict["cluster"] = cluster_config_cluster
        kwargsDict["ensemble"] = cluster_config_ensemble
        kwargsDict["mipi"] = cluster_config_mipi
        kwargsDict["name"] = cluster_config_name
        kwargsDict["node_id"] = cluster_config_node_id
        kwargsDict["pending_node_id"] = cluster_config_pending_node_id
        kwargsDict["role"] = cluster_config_role
        kwargsDict["sipi"] = cluster_config_sipi
        kwargsDict["state"] = cluster_config_state

        cluster = ClusterConfig(**kwargsDict)

    SetClusterConfigResult = ctx.element.set_cluster_config(cluster=cluster)
    cli_utils.print_result(SetClusterConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SetNtpInfo', short_help="""SetNtpInfo is used to configure the NTP on cluster nodes. The values set with this interface apply to all nodes in the cluster. The nodes can only be configured as a server where a host is selected to administrate the networking and/or a broadcast client where each host sends each message to each peer. """)
@click.option('--servers',
              type=str,
              required=True,
              help="""List of NTP servers to add to each node's NTP configuration. """)
@click.option('--broadcastclient',
              type=bool,
              required=False,
              help="""Enable every node in the cluster as a broadcase client. """)
@pass_context
def SetNtpInfo(ctx,
           servers,
           broadcastclient = None):
    """SetNtpInfo is used to configure the NTP on cluster nodes. The values set with this interface apply to all nodes in the cluster. The nodes can only be configured as a server where a host is selected to administrate the networking and/or a broadcast client where each host sends each message to each peer."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    servers = parser.parse_array(servers)

    SetNtpInfoResult = ctx.element.set_ntp_info(servers=servers, broadcastclient=broadcastclient)
    cli_utils.print_result(SetNtpInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SetSnmpACL', short_help="""SetSnmpACL is used to configure SNMP access permissions on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all "network" or "usmUsers" values set with the older SetSnmpInfo. """)
@click.option('--snmp_network_access',
              type=str,
              required=True,
              help="""<br/><b>ro</b>: read-only access.* <br/><b>rw</b>: for read-write access. <br/><b>rosys</b>: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. """)
@click.option('--snmp_network_cidr',
              type=int,
              required=True,
              help="""A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. """)
@click.option('--snmp_network_community',
              type=str,
              required=True,
              help="""SNMP community string. """)
@click.option('--snmp_network_network',
              type=str,
              required=True,
              help="""This parameter along with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. """)
@click.option('--snmp_v3_usm_user_access',
              type=str,
              required=True,
              help="""<br/><b>rouser</b>: read-only access.* <br/><b>rwuser</b>: for read-write access. <br/><b>rosys</b>: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. """)
@click.option('--snmp_v3_usm_user_name',
              type=str,
              required=True,
              help="""The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. """)
@click.option('--snmp_v3_usm_user_password',
              type=str,
              required=True,
              help="""The password of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." """)
@click.option('--snmp_v3_usm_user_passphrase',
              type=str,
              required=True,
              help="""The passphrase of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." """)
@click.option('--snmp_v3_usm_user_sec_level',
              type=str,
              required=True,
              help="""<br/><b>noauth</b>: No password or passphrase is required. <br/><b>auth</b>: A password is required for user access. <br/><b>priv</b>: A password and passphrase is required for user access. """)
@pass_context
def SetSnmpACL(ctx,
           snmp_network_access,
           snmp_network_cidr,
           snmp_network_community,
           snmp_network_network,
           snmp_v3_usm_user_access,
           snmp_v3_usm_user_name,
           snmp_v3_usm_user_password,
           snmp_v3_usm_user_passphrase,
           snmp_v3_usm_user_sec_level):
    """SetSnmpACL is used to configure SNMP access permissions on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all &quot;network&quot; or &quot;usmUsers&quot; values set with the older SetSnmpInfo."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    networks = None
    if(networks is not None or usm_users is not None or False):
        kwargsDict = dict()
        kwargsDict["access"] = snmp_network_access
        kwargsDict["cidr"] = snmp_network_cidr
        kwargsDict["community"] = snmp_network_community
        kwargsDict["network"] = snmp_network_network

        networks = SnmpNetwork(**kwargsDict)

    networks = parser.parse_array(networks)

    usm_users = None
    if(networks is not None or usm_users is not None or False):
        kwargsDict = dict()
        kwargsDict["access"] = snmp_v3_usm_user_access
        kwargsDict["name"] = snmp_v3_usm_user_name
        kwargsDict["password"] = snmp_v3_usm_user_password
        kwargsDict["passphrase"] = snmp_v3_usm_user_passphrase
        kwargsDict["sec_level"] = snmp_v3_usm_user_sec_level

        usm_users = SnmpV3UsmUser(**kwargsDict)

    usm_users = parser.parse_array(usm_users)

    SetSnmpACLResult = ctx.element.set_snmp_acl(networks=networks, usm_users=usm_users)
    cli_utils.print_result(SetSnmpACLResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SetSnmpInfo', short_help="""SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.  Note: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future. """)
@click.option('--snmp_network_access',
              type=str,
              required=True,
              help="""<br/><b>ro</b>: read-only access.* <br/><b>rw</b>: for read-write access. <br/><b>rosys</b>: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. """)
@click.option('--snmp_network_cidr',
              type=int,
              required=True,
              help="""A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. """)
@click.option('--snmp_network_community',
              type=str,
              required=True,
              help="""SNMP community string. """)
@click.option('--snmp_network_network',
              type=str,
              required=True,
              help="""This parameter along with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. """)
@click.option('--enabled',
              type=bool,
              required=False,
              help="""If set to "true", then SNMP is enabled on each node in the cluster. """)
@click.option('--snmp_v3_enabled',
              type=bool,
              required=False,
              help="""If set to "true", then SNMP v3 is enabled on each node in the cluster. """)
@click.option('--snmp_v3_usm_user_access',
              type=str,
              required=True,
              help="""<br/><b>rouser</b>: read-only access.* <br/><b>rwuser</b>: for read-write access. <br/><b>rosys</b>: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. """)
@click.option('--snmp_v3_usm_user_name',
              type=str,
              required=True,
              help="""The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. """)
@click.option('--snmp_v3_usm_user_password',
              type=str,
              required=True,
              help="""The password of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." """)
@click.option('--snmp_v3_usm_user_passphrase',
              type=str,
              required=True,
              help="""The passphrase of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." """)
@click.option('--snmp_v3_usm_user_sec_level',
              type=str,
              required=True,
              help="""<br/><b>noauth</b>: No password or passphrase is required. <br/><b>auth</b>: A password is required for user access. <br/><b>priv</b>: A password and passphrase is required for user access. """)
@pass_context
def SetSnmpInfo(ctx,
           snmp_network_access = None,
           snmp_network_cidr = None,
           snmp_network_community = None,
           snmp_network_network = None,
           enabled = None,
           snmp_v3_enabled = None,
           snmp_v3_usm_user_access = None,
           snmp_v3_usm_user_name = None,
           snmp_v3_usm_user_password = None,
           snmp_v3_usm_user_passphrase = None,
           snmp_v3_usm_user_sec_level = None):
    """SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo."""
    """"""
    """Note: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    networks = None
    if(networks is not None or enabled is not None or snmp_v3_enabled is not None or usm_users is not None or False):
        kwargsDict = dict()
        kwargsDict["access"] = snmp_network_access
        kwargsDict["cidr"] = snmp_network_cidr
        kwargsDict["community"] = snmp_network_community
        kwargsDict["network"] = snmp_network_network

        networks = SnmpNetwork(**kwargsDict)

    networks = parser.parse_array(networks)

    usm_users = None
    if(networks is not None or enabled is not None or snmp_v3_enabled is not None or usm_users is not None or False):
        kwargsDict = dict()
        kwargsDict["access"] = snmp_v3_usm_user_access
        kwargsDict["name"] = snmp_v3_usm_user_name
        kwargsDict["password"] = snmp_v3_usm_user_password
        kwargsDict["passphrase"] = snmp_v3_usm_user_passphrase
        kwargsDict["sec_level"] = snmp_v3_usm_user_sec_level

        usm_users = SnmpV3UsmUser(**kwargsDict)

    usm_users = parser.parse_array(usm_users)

    SetSnmpInfoResult = ctx.element.set_snmp_info(networks=networks, enabled=enabled, snmp_v3_enabled=snmp_v3_enabled, usm_users=usm_users)
    cli_utils.print_result(SetSnmpInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SetSnmpTrapInfo', short_help="""SetSnmpTrapInfo is used to enable and disable the generation of SolidFire SNMP notifications (traps) and to specify the set of network host computers that are to receive the notifications. The values passed with each SetSnmpTrapInfo method replaces all values set in any previous method to SetSnmpTrapInfo. """)
@click.option('--snmp_trap_recipient_host',
              type=str,
              required=True,
              help="""The IP address or host name of the target network management station. """)
@click.option('--snmp_trap_recipient_community',
              type=str,
              required=True,
              help="""SNMP community string. """)
@click.option('--snmp_trap_recipient_port',
              type=int,
              required=True,
              help="""The UDP port number on the host where the trap is to be sent. Valid range is 1 - 65535. 0 (zero) is not a valid port number. Default is 162. """)
@click.option('--cluster_fault_traps_enabled',
              type=bool,
              required=True,
              help="""If "true", when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients. """)
@click.option('--cluster_fault_resolved_traps_enabled',
              type=bool,
              required=True,
              help="""If "true", when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients. """)
@click.option('--cluster_event_traps_enabled',
              type=bool,
              required=True,
              help="""If "true", when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients. """)
@pass_context
def SetSnmpTrapInfo(ctx,
           cluster_fault_traps_enabled,
           cluster_fault_resolved_traps_enabled,
           cluster_event_traps_enabled,
           snmp_trap_recipient_host,
           snmp_trap_recipient_community,
           snmp_trap_recipient_port):
    """SetSnmpTrapInfo is used to enable and disable the generation of SolidFire SNMP notifications (traps) and to specify the set of network host computers that are to receive the notifications. The values passed with each SetSnmpTrapInfo method replaces all values set in any previous method to SetSnmpTrapInfo."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    trap_recipients = None
    if(trap_recipients is not None or cluster_fault_traps_enabled is not None or cluster_fault_resolved_traps_enabled is not None or cluster_event_traps_enabled is not None or False):
        kwargsDict = dict()
        kwargsDict["host"] = snmp_trap_recipient_host
        kwargsDict["community"] = snmp_trap_recipient_community
        kwargsDict["port"] = snmp_trap_recipient_port

        trap_recipients = SnmpTrapRecipient(**kwargsDict)

    trap_recipients = parser.parse_array(trap_recipients)

    SetSnmpTrapInfoResult = ctx.element.set_snmp_trap_info(trap_recipients=trap_recipients, cluster_fault_traps_enabled=cluster_fault_traps_enabled, cluster_fault_resolved_traps_enabled=cluster_fault_resolved_traps_enabled, cluster_event_traps_enabled=cluster_event_traps_enabled)
    cli_utils.print_result(SetSnmpTrapInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SnmpSendTestTraps', short_help="""SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager. """)
@pass_context
def SnmpSendTestTraps(ctx):
    """SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    SnmpSendTestTrapsResult = ctx.element.snmp_send_test_traps()
    cli_utils.print_result(SnmpSendTestTrapsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

