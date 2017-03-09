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
    """getinfo getapi getconfig getsnmpstate getsnmpinfo disablesnmp deleteallsupportbundles getsystemstatus getversioninfo listfaults listadmins create disableencryptionatrest addadmin setntpinfo setconfig modifyadmin getsnmptrapinfo listevents clearfaults removeadmin getstats getlimits getcurrentadmin createsupportbundle enablesnmp getntpinfo listsyncjobs setsnmptrapinfo setsnmpacl snmpsendtesttraps getsnmpacl getstate getcapacity modifyfullthreshold getmasternodeid setsnmpinfo getfullthreshold enableencryptionatrest """

@cli.command('getinfo', short_help="""Return configuration information about the cluster. """, cls=SolidFireCommand)
@pass_context
def getinfo(ctx):
    """Return configuration information about the cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetClusterInfoResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetClusterInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getapi', short_help="""Retrieves the current version of the API and a list of all supported versions. """, cls=SolidFireCommand)
@pass_context
def getapi(ctx):
    """Retrieves the current version of the API and a list of all supported versions."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetAPIResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetAPIResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getconfig', short_help="""The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of.  Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def getconfig(ctx):
    """The GetClusterConfig API method is used to return information about the cluster configuration this node uses to communicate with the cluster it is a part of."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetClusterConfigResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetClusterConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsnmpstate', short_help="""GetSnmpState is used to return the current state of the SNMP feature.  Note: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future. """, cls=SolidFireCommand)
@pass_context
def getsnmpstate(ctx):
    """GetSnmpState is used to return the current state of the SNMP feature."""
    """"""
    """Note: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetSnmpStateResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetSnmpStateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsnmpinfo', short_help="""GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information.  Note: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage. """, cls=SolidFireCommand)
@pass_context
def getsnmpinfo(ctx):
    """GetSnmpInfo is used to return the current simple network management protocol (SNMP) configuration information."""
    """"""
    """Note: GetSnmpInfo will be available for Element OS 8 and prior releases. It will be deprecated after Element OS 8. There are two new SNMP API methods that you should migrate over to. They are GetSnmpState and GetSnmpACL. Please see details in this document for their descriptions and usage."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetSnmpInfoResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetSnmpInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('disablesnmp', short_help="""DisableSnmp is used to disable SNMP on the cluster nodes. """, cls=SolidFireCommand)
@pass_context
def disablesnmp(ctx):
    """DisableSnmp is used to disable SNMP on the cluster nodes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _DisableSnmpResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DisableSnmpResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('deleteallsupportbundles', short_help="""DeleteAllSupportBundles is used to delete all support bundles generated with the CreateSupportBundle API method. """, cls=SolidFireCommand)
@pass_context
def deleteallsupportbundles(ctx):
    """DeleteAllSupportBundles is used to delete all support bundles generated with the CreateSupportBundle API method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _DeleteAllSupportBundlesResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DeleteAllSupportBundlesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsystemstatus', short_help="""""", cls=SolidFireCommand)
@pass_context
def getsystemstatus(ctx):
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetSystemStatusResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetSystemStatusResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getversioninfo', short_help="""Return information about the Element software version running on each node in the cluster. Information about the nodes that are currently in the process of upgrading software is also returned. """, cls=SolidFireCommand)
@pass_context
def getversioninfo(ctx):
    """Return information about the Element software version running on each node in the cluster."""
    """Information about the nodes that are currently in the process of upgrading software is also returned."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetClusterVersionInfoResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetClusterVersionInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listfaults', short_help="""ListClusterFaults is used to retrieve information about any faults detected on the cluster. With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds. """, cls=SolidFireCommand)
@click.option('--exceptions',
              type=bool,
              required=False,
              help=""" """)
@click.option('--bestpractices',
              type=bool,
              required=False,
              help="""Include faults triggered by sub-optimal system configuration. Possible values: true, false """)
@click.option('--update',
              type=bool,
              required=False,
              help=""" """)
@click.option('--faulttypes',
              type=str,
              required=False,
              help="""Determines the types of faults returned: current: List active, unresolved faults. resolved: List faults that were previously detected and resolved. all: (Default) List both current and resolved faults. You can see the fault status in the 'resolved' field of the Cluster Fault object. """)
@pass_context
def listfaults(ctx,
           # Optional main parameter
           exceptions = None,
           # Optional main parameter
           bestpractices = None,
           # Optional main parameter
           update = None,
           # Optional main parameter
           faulttypes = None):
    """ListClusterFaults is used to retrieve information about any faults detected on the cluster."""
    """With this method, both current and resolved faults can be retrieved. The system caches faults every 30 seconds."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                
    

    ctx.logger.info("""exceptions = """+str(exceptions)+""";"""+"""bestpractices = """+str(bestpractices)+""";"""+"""update = """+str(update)+""";"""+"""faulttypes = """+str(faulttypes)+""";"""+"")
    try:
        _ListClusterFaultsResult = ctx.element.(exceptions=exceptions, best_practices=bestpractices, update=update, fault_types=faulttypes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListClusterFaultsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listadmins', short_help="""ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrators that have different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. LDAP administrators can also be created when setting up an LDAP system on the cluster. """, cls=SolidFireCommand)
@click.option('--showhidden',
              type=bool,
              required=False,
              help=""" """)
@pass_context
def listadmins(ctx,
           # Optional main parameter
           showhidden = None):
    """ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrators that have different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. LDAP administrators can also be created when setting up an LDAP system on the cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""showhidden = """+str(showhidden)+""";"""+"")
    try:
        _ListClusterAdminsResult = ctx.element.(show_hidden=showhidden)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListClusterAdminsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""The CreateCluster method is used to initialize the node in a cluster that has ownership of the "mvip" and "svip" addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized.  Note: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method. """, cls=SolidFireCommand)
@click.option('--accepteula',
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
@click.option('--repcount',
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
              help="""List of Name/Value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def create(ctx,
           # Mandatory main parameter
           mvip,
           # Mandatory main parameter
           svip,
           # Mandatory main parameter
           repcount,
           # Mandatory main parameter
           username,
           # Mandatory main parameter
           password,
           # Mandatory main parameter
           nodes,
           # Optional main parameter
           accepteula = None,
           # Optional main parameter
           attributes = None):
    """The CreateCluster method is used to initialize the node in a cluster that has ownership of the &quot;mvip&quot; and &quot;svip&quot; addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized."""
    """"""
    """Note: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                            

    nodes = parser.parse_array(nodes)    

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""accepteula = """+str(accepteula)+""";"""+"""mvip = """+str(mvip)+""";"""+"""svip = """+str(svip)+""";"""+"""repcount = """+str(repcount)+""";"""+"""username = """+str(username)+""";"""+"""password = """+str(password)+""";"""+"""nodes = """+str(nodes)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _CreateClusterResult = ctx.element.(mvip=mvip, svip=svip, rep_count=repcount, username=username, password=password, nodes=nodes, accept_eula=accepteula, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateClusterResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('disableencryptionatrest', short_help="""The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method. This disable method is asynchronous and returns a response before encryption is disabled. You can use the GetClusterInfo method to poll the system to see when the process has completed. """, cls=SolidFireCommand)
@pass_context
def disableencryptionatrest(ctx):
    """The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method."""
    """This disable method is asynchronous and returns a response before encryption is disabled."""
    """You can use the GetClusterInfo method to poll the system to see when the process has completed."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _DisableEncryptionAtRestResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DisableEncryptionAtRestResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('addadmin', short_help="""AddClusterAdmin adds a new Cluster Admin. A Cluster Admin can be used to manage the cluster via the API and management tools. Cluster Admins are completely separate and unrelated to standard tenant accounts.  Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise. """, cls=SolidFireCommand)
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
@click.option('--accepteula',
              type=bool,
              required=False,
              help="""Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of Name/Value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def addadmin(ctx,
           # Mandatory main parameter
           username,
           # Mandatory main parameter
           password,
           # Mandatory main parameter
           access,
           # Optional main parameter
           accepteula = None,
           # Optional main parameter
           attributes = None):
    """AddClusterAdmin adds a new Cluster Admin. A Cluster Admin can be used to manage the cluster via the API and management tools. Cluster Admins are completely separate and unrelated to standard tenant accounts."""
    """"""
    """Each Cluster Admin can be restricted to a sub-set of the API. SolidFire recommends using multiple Cluster Admins for different users and applications. Each Cluster Admin should be given the minimal permissions necessary to reduce the potential impact of credential compromise."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            

    access = parser.parse_array(access)        

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""username = """+str(username)+""";"""+"""password = """+str(password)+""";"""+"""access = """+str(access)+""";"""+"""accepteula = """+str(accepteula)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _AddClusterAdminResult = ctx.element.(username=username, password=password, access=access, accept_eula=accepteula, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_AddClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setntpinfo', short_help="""SetNtpInfo is used to configure the NTP on cluster nodes. The values set with this interface apply to all nodes in the cluster. The nodes can only be configured as a server where a host is selected to administrate the networking and/or a broadcast client where each host sends each message to each peer. """, cls=SolidFireCommand)
@click.option('--servers',
              type=str,
              required=True,
              help="""List of NTP servers to add to each node's NTP configuration. """)
@click.option('--broadcastclient',
              type=bool,
              required=False,
              help="""Enable every node in the cluster as a broadcase client. """)
@pass_context
def setntpinfo(ctx,
           # Mandatory main parameter
           servers,
           # Optional main parameter
           broadcastclient = None):
    """SetNtpInfo is used to configure the NTP on cluster nodes. The values set with this interface apply to all nodes in the cluster. The nodes can only be configured as a server where a host is selected to administrate the networking and/or a broadcast client where each host sends each message to each peer."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    servers = parser.parse_array(servers)    
    

    ctx.logger.info("""servers = """+str(servers)+""";"""+"""broadcastclient = """+str(broadcastclient)+""";"""+"")
    try:
        _SetNtpInfoResult = ctx.element.(servers=servers, broadcastclient=broadcastclient)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetNtpInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setconfig', short_help="""The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method.  Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)

@click.option('--clusterconfigcipi',
              type=str,
              required=False,
              help="""Network interface used for cluster communication. """)

@click.option('--clusterconfigclustercluster',
              type=str,
              required=False,
              help="""Unique cluster name. """)

@click.option('--clusterconfigensemble',
              type=str,
              required=False,
              help="""Nodes that are participating in the cluster. """)

@click.option('--clusterconfigmipi',
              type=str,
              required=False,
              help="""Network interface used for node management. """)

@click.option('--clusterconfigname',
              type=str,
              required=False,
              help="""Unique cluster name. """)

@click.option('--clusterconfignodeid',
              type=int,
              required=False,
              help=""" """)

@click.option('--clusterconfigpendingnodeid',
              type=int,
              required=False,
              help=""" """)

@click.option('--clusterconfigrole',
              type=str,
              required=False,
              help="""Identifies the role of the node """)

@click.option('--clusterconfigsipi',
              type=str,
              required=False,
              help="""Network interface used for storage. """)

@click.option('--clusterconfigstate',
              type=str,
              required=False,
              help=""" """)

@click.option('--clusterconfigencryptioncapable',
              type=bool,
              required=False,
              help=""" """)

@click.option('--clusterconfighaslocaladmin',
              type=bool,
              required=False,
              help=""" """)

@click.option('--clusterconfigversion',
              type=str,
              required=False,
              help=""" """)
@pass_context
def setconfig(ctx,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigcipi = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigclustercluster = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigensemble = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigmipi = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigname = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfignodeid = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigpendingnodeid = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigrole = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigsipi = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigstate = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigencryptioncapable = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfighaslocaladmin = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           clusterconfigversion = None):
    """The SetClusterConfig API method is used to set the configuration this node uses to communicate with the cluster it is associated with. To see the states in which these objects can be modified see Cluster Object on page 109. To display the current cluster interface settings for a node, run the GetClusterConfig API method."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    cluster = None
    if(clusterconfigcipi is not None or
       clusterconfigclustercluster is not None or
       clusterconfigensemble is not None or
       clusterconfigmipi is not None or
       clusterconfigname is not None or
       clusterconfignodeid is not None or
       clusterconfigpendingnodeid is not None or
       clusterconfigrole is not None or
       clusterconfigsipi is not None or
       clusterconfigstate is not None or
       clusterconfigencryptioncapable is not None or
       clusterconfighaslocaladmin is not None or
       clusterconfigversion is not None or
       False):
        if not ( True):
            ctx.logger.error("""If you choose to provide clusterconfig, you must include all of the following parameters:
""")
        kwargsDict = dict()
        kwargsDict["cipi"] = clusterconfigcipi
        kwargsDict["cluster"] = clusterconfigclustercluster
        kwargsDict["ensemble"] = clusterconfigensemble
        kwargsDict["mipi"] = clusterconfigmipi
        kwargsDict["name"] = clusterconfigname
        kwargsDict["node_id"] = clusterconfignodeid
        kwargsDict["pending_node_id"] = clusterconfigpendingnodeid
        kwargsDict["role"] = clusterconfigrole
        kwargsDict["sipi"] = clusterconfigsipi
        kwargsDict["state"] = clusterconfigstate
        kwargsDict["encryption_capable"] = clusterconfigencryptioncapable
        kwargsDict["has_local_admin"] = clusterconfighaslocaladmin
        kwargsDict["version"] = clusterconfigversion

        cluster = ClusterConfig(**kwargsDict)
    

    ctx.logger.info("""cluster = """+str(cluster)+""";"""+"")
    try:
        _SetClusterConfigResult = ctx.element.(cluster=cluster)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetClusterConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyadmin', short_help="""ModifyClusterAdmin is used to change the settings for a Cluster Admin or LDAP Cluster Admin. Access for the administrator Cluster Admin account cannot be changed. """, cls=SolidFireCommand)
@click.option('--clusteradminid',
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
              help="""List of Name/Value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def modifyadmin(ctx,
           # Mandatory main parameter
           clusteradminid,
           # Optional main parameter
           password = None,
           # Optional main parameter
           access = None,
           # Optional main parameter
           attributes = None):
    """ModifyClusterAdmin is used to change the settings for a Cluster Admin or LDAP Cluster Admin. Access for the administrator Cluster Admin account cannot be changed."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            

    access = parser.parse_array(access)    

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""clusteradminid = """+str(clusteradminid)+""";"""+"""password = """+str(password)+""";"""+"""access = """+str(access)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _ModifyClusterAdminResult = ctx.element.(cluster_admin_id=clusteradminid, password=password, access=access, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsnmptrapinfo', short_help="""GetSnmpTrapInfo is used to return current SNMP trap configuration information. """, cls=SolidFireCommand)
@click.option('--id',
              type=int,
              required=False,
              help=""" """)
@pass_context
def getsnmptrapinfo(ctx,
           # Optional main parameter
           id = None):
    """GetSnmpTrapInfo is used to return current SNMP trap configuration information."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""id = """+str(id)+""";"""+"")
    try:
        _GetSnmpTrapInfoResult = ctx.element.(id=id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetSnmpTrapInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listevents', short_help="""ListEvents returns events detected on the cluster, sorted from oldest to newest. """, cls=SolidFireCommand)
@click.option('--maxevents',
              type=int,
              required=False,
              help="""Specifies the maximum number of events to return. """)
@click.option('--starteventid',
              type=int,
              required=False,
              help="""Identifies the beginning of a range of events to return. """)
@click.option('--endeventid',
              type=int,
              required=False,
              help="""Identifies the end of a range of events to return. """)
@click.option('--eventqueuetype',
              type=str,
              required=False,
              help=""" """)
@pass_context
def listevents(ctx,
           # Optional main parameter
           maxevents = None,
           # Optional main parameter
           starteventid = None,
           # Optional main parameter
           endeventid = None,
           # Optional main parameter
           eventqueuetype = None):
    """ListEvents returns events detected on the cluster, sorted from oldest to newest."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                
    

    ctx.logger.info("""maxevents = """+str(maxevents)+""";"""+"""starteventid = """+str(starteventid)+""";"""+"""endeventid = """+str(endeventid)+""";"""+"""eventqueuetype = """+str(eventqueuetype)+""";"""+"")
    try:
        _ListEventsResult = ctx.element.(max_events=maxevents, start_event_id=starteventid, end_event_id=endeventid, event_queue_type=eventqueuetype)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListEventsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('clearfaults', short_help="""ClearClusterFaults is used to clear information about both current faults that are resolved as well as faults that were previously detected and resolved can be cleared. """, cls=SolidFireCommand)
@click.option('--faulttype',
              type=str,
              required=False,
              help="""Determines the types of faults cleared: current: Faults that are currently detected and have not been resolved. resolved: Faults that were previously detected and resolved. all: Both current and resolved faults are cleared. The fault status can be determined by the "resolved" field of the fault object. """)
@pass_context
def clearfaults(ctx,
           # Optional main parameter
           faulttype = None):
    """ClearClusterFaults is used to clear information about both current faults that are resolved as well as faults that were previously detected and resolved can be cleared."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""faulttype = """+str(faulttype)+""";"""+"")
    try:
        _ClearClusterFaultsResult = ctx.element.(fault_type=faulttype)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ClearClusterFaultsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('removeadmin', short_help="""RemoveClusterAdmin is used to remove a Cluster Admin. The "admin" Cluster Admin cannot be removed. """, cls=SolidFireCommand)
@click.option('--clusteradminid',
              type=int,
              required=True,
              help="""ClusterAdminID for the Cluster Admin to remove. """)
@pass_context
def removeadmin(ctx,
           # Mandatory main parameter
           clusteradminid):
    """RemoveClusterAdmin is used to remove a Cluster Admin. The &quot;admin&quot; Cluster Admin cannot be removed."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""clusteradminid = """+str(clusteradminid)+""";"""+"")
    try:
        _RemoveClusterAdminResult = ctx.element.(cluster_admin_id=clusteradminid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_RemoveClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstats', short_help="""GetClusterStats is used to return high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster. """, cls=SolidFireCommand)
@pass_context
def getstats(ctx):
    """GetClusterStats is used to return high-level activity measurements for the cluster. Values returned are cumulative from the creation of the cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetClusterStatsResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetClusterStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getlimits', short_help="""GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of  Element, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools.NOTE: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method. """, cls=SolidFireCommand)
@pass_context
def getlimits(ctx):
    """GetLimits enables you to retrieve the limit values set by the API. These values might change between releases of  Element, but do not change without an update to the system. Knowing the limit values set by the API can be useful when writing API scripts for user-facing tools.NOTE: The GetLimits method returns the limits for the current software version regardless of the API endpoint version used to pass the method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetLimitsResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetLimitsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getcurrentadmin', short_help="""GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was ncreated when the cluster was created. """, cls=SolidFireCommand)
@pass_context
def getcurrentadmin(ctx):
    """GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was ncreated when the cluster was created."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetCurrentClusterAdminResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetCurrentClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createsupportbundle', short_help="""CreateSupportBundle is used to create a support bundle file under the node's directory. When the bundle has been successfully created, the bundle is stored on the node as a tar.gz file. """, cls=SolidFireCommand)
@click.option('--bundlename',
              type=str,
              required=False,
              help="""Unique name for each support bundle created. If no name is provided, then 'supportbundle' and the node name is used as a file name. """)
@click.option('--extraargs',
              type=str,
              required=False,
              help="""This parameter is fed to the sf_make_support_bundle script. Should be used only at the request of SolidFire Support. """)
@click.option('--timeoutsec',
              type=int,
              required=False,
              help="""The number of seconds to let the support bundle script run before timing out and stopping. Default is 1500 seconds. """)
@pass_context
def createsupportbundle(ctx,
           # Optional main parameter
           bundlename = None,
           # Optional main parameter
           extraargs = None,
           # Optional main parameter
           timeoutsec = None):
    """CreateSupportBundle is used to create a support bundle file under the node&#x27;s directory. When the bundle has been successfully created, the bundle is stored on the node as a tar.gz file."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""bundlename = """+str(bundlename)+""";"""+"""extraargs = """+str(extraargs)+""";"""+"""timeoutsec = """+str(timeoutsec)+""";"""+"")
    try:
        _CreateSupportBundleResult = ctx.element.(bundle_name=bundlename, extra_args=extraargs, timeout_sec=timeoutsec)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateSupportBundleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enablesnmp', short_help="""EnableSnmp is used to enable SNMP on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp. """, cls=SolidFireCommand)
@click.option('--snmpv3enabled',
              type=bool,
              required=True,
              help="""If set to "true", then SNMP v3 is enabled on each node in the cluster. If set to "false", then SNMP v2 is enabled. """)
@pass_context
def enablesnmp(ctx,
           # Mandatory main parameter
           snmpv3enabled):
    """EnableSnmp is used to enable SNMP on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""snmpv3enabled = """+str(snmpv3enabled)+""";"""+"")
    try:
        _EnableSnmpResult = ctx.element.(snmp_v3_enabled=snmpv3enabled)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_EnableSnmpResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getntpinfo', short_help="""GetNtpInfo is used to return the current network time protocol (NTP) configuration information. """, cls=SolidFireCommand)
@pass_context
def getntpinfo(ctx):
    """GetNtpInfo is used to return the current network time protocol (NTP) configuration information."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetNtpInfoResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetNtpInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listsyncjobs', short_help="""ListSyncJobs is used to return information about synchronization jobs that are running on a SolidFire cluster. Synchronization jobs that are returned with this method are, "slice," "clone" and "remote." """, cls=SolidFireCommand)
@pass_context
def listsyncjobs(ctx):
    """ListSyncJobs is used to return information about synchronization jobs that are running on a SolidFire cluster. Synchronization jobs that are returned with this method are, &quot;slice,&quot; &quot;clone&quot; and &quot;remote.&quot;"""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListSyncJobsResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListSyncJobsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setsnmptrapinfo', short_help="""SetSnmpTrapInfo is used to enable and disable the generation of SolidFire SNMP notifications (traps) and to specify the set of network host computers that are to receive the notifications. The values passed with each SetSnmpTrapInfo method replaces all values set in any previous method to SetSnmpTrapInfo. """, cls=SolidFireCommand)
@click.option('--traprecipients',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["host", "community", "port", ],
              required=True,
              help="""List of hosts that are to receive the traps generated by the Cluster Master. At least one object is required if any one of the trap types is enabled.  Has the following subparameters: --host --community --port """)
@click.option('--host',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The IP address or host name of the target network management station. """,
              cls=SolidFireOption)
@click.option('--community',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] SNMP community string. """,
              cls=SolidFireOption)
@click.option('--port',
              required=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The UDP port number on the host where the trap is to be sent. Valid range is 1 - 65535. 0 (zero) is not a valid port number. Default is 162. """,
              cls=SolidFireOption)
@click.option('--clusterfaulttrapsenabled',
              type=bool,
              required=True,
              help="""If "true", when a cluster fault is logged a corresponding solidFireClusterFaultNotification is sent to the configured list of trap recipients. """)
@click.option('--clusterfaultresolvedtrapsenabled',
              type=bool,
              required=True,
              help="""If "true", when a cluster fault is logged a corresponding solidFireClusterFaultResolvedNotification is sent to the configured list of trap recipients. """)
@click.option('--clustereventtrapsenabled',
              type=bool,
              required=True,
              help="""If "true", when a cluster fault is logged a corresponding solidFireClusterEventNotification is sent to the configured list of trap recipients. """)
@pass_context
def setsnmptrapinfo(ctx,
           # Mandatory main parameter
           traprecipients,
           # Mandatory main parameter
           clusterfaulttrapsenabled,
           # Mandatory main parameter
           clusterfaultresolvedtrapsenabled,
           # Mandatory main parameter
           clustereventtrapsenabled,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           host,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           community,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           port):
    """SetSnmpTrapInfo is used to enable and disable the generation of SolidFire SNMP notifications (traps) and to specify the set of network host computers that are to receive the notifications. The values passed with each SetSnmpTrapInfo method replaces all values set in any previous method to SetSnmpTrapInfo."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    traprecipientsArray = []
    if(traprecipients is not None):
        try:
            for i, _traprecipients in enumerate(traprecipients):
                traprecipientsArray.append(SnmpTrapRecipient(host=host[i], community=community[i], port=port[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)            
    

    ctx.logger.info("""traprecipients = """+str(traprecipients)+""";"""+"""clusterfaulttrapsenabled = """+str(clusterfaulttrapsenabled)+""";"""+"""clusterfaultresolvedtrapsenabled = """+str(clusterfaultresolvedtrapsenabled)+""";"""+"""clustereventtrapsenabled = """+str(clustereventtrapsenabled)+""";"""+"")
    try:
        _SetSnmpTrapInfoResult = ctx.element.(trap_recipients=traprecipientsArray, cluster_fault_traps_enabled=clusterfaulttrapsenabled, cluster_fault_resolved_traps_enabled=clusterfaultresolvedtrapsenabled, cluster_event_traps_enabled=clustereventtrapsenabled)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetSnmpTrapInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setsnmpacl', short_help="""SetSnmpACL is used to configure SNMP access permissions on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all "network" or "usmUsers" values set with the older SetSnmpInfo. """, cls=SolidFireCommand)
@click.option('--networks',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["accessnetworks", "cidr", "community", "network", ],
              required=True,
              help="""List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. REQUIRED if SNMP v# is disabled.  Has the following subparameters: --accessnetworks --cidr --community --network """)
@click.option('--accessnetworks',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] ro: read-only access.* rw: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. """,
              cls=SolidFireOption)
@click.option('--cidr',
              required=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. """,
              cls=SolidFireOption)
@click.option('--community',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] SNMP community string. """,
              cls=SolidFireOption)
@click.option('--network',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] This parameter along with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. """,
              cls=SolidFireOption)
@click.option('--usmusers',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["accessusmusers", "name", "password", "passphrase", "seclevel", ],
              required=True,
              help="""List of users and the type of access they have to the SNMP servers running on the cluster nodes. REQUIRED if SNMP v3 is enabled.  Has the following subparameters: --accessusmusers --name --password --passphrase --seclevel """)
@click.option('--accessusmusers',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] rouser: read-only access.* rwuser: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. """,
              cls=SolidFireOption)
@click.option('--name',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. """,
              cls=SolidFireOption)
@click.option('--password',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The password of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." """,
              cls=SolidFireOption)
@click.option('--passphrase',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The passphrase of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." """,
              cls=SolidFireOption)
@click.option('--seclevel',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] noauth: No password or passphrase is required. auth: A password is required for user access. priv: A password and passphrase is required for user access. """,
              cls=SolidFireOption)
@pass_context
def setsnmpacl(ctx,
           # Mandatory main parameter
           networks,
           # Mandatory main parameter
           usmusers,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           accessnetworks,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           cidr,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           community,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           network,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           accessusmusers,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           password,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           passphrase,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           seclevel):
    """SetSnmpACL is used to configure SNMP access permissions on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all &quot;network&quot; or &quot;usmUsers&quot; values set with the older SetSnmpInfo."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    networksArray = []
    if(networks is not None):
        try:
            for i, _networks in enumerate(networks):
                networksArray.append(SnmpNetwork(access=accessnetworks[i], cidr=cidr[i], community=community[i], network=network[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)    

    usmusersArray = []
    if(usmusers is not None):
        try:
            for i, _usmusers in enumerate(usmusers):
                usmusersArray.append(SnmpV3UsmUser(access=accessusmusers[i], name=name[i], password=password[i], passphrase=passphrase[i], sec_level=seclevel[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""networks = """+str(networks)+""";"""+"""usmusers = """+str(usmusers)+""";"""+"")
    try:
        _SetSnmpACLResult = ctx.element.(networks=networksArray, usm_users=usmusersArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetSnmpACLResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('snmpsendtesttraps', short_help="""SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager. """, cls=SolidFireCommand)
@pass_context
def snmpsendtesttraps(ctx):
    """SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _SnmpSendTestTrapsResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SnmpSendTestTrapsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getsnmpacl', short_help="""GetSnmpACL is used to return the current SNMP access permissions on the cluster nodes. """, cls=SolidFireCommand)
@pass_context
def getsnmpacl(ctx):
    """GetSnmpACL is used to return the current SNMP access permissions on the cluster nodes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetSnmpACLResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetSnmpACLResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstate', short_help="""The GetClusterState method is used to indicate if a node is part of a cluster or not. The three states are: Available: Node has not been configured with a cluster name.Pending: Node is pending for a specific named cluster and can be added.Active: Node is active and a member of a cluster and may not be added to another cluster. """, cls=SolidFireCommand)
@click.option('--force',
              type=bool,
              required=True,
              help="""To run this command, the force parameter must be set to true. """)
@pass_context
def getstate(ctx,
           # Mandatory main parameter
           force):
    """The GetClusterState method is used to indicate if a node is part of a cluster or not. The three states are: Available: Node has not been configured with a cluster name.Pending: Node is pending for a specific named cluster and can be added.Active: Node is active and a member of a cluster and may not be added to another cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""force = """+str(force)+""";"""+"")
    try:
        _GetClusterStateResult = ctx.element.(force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetClusterStateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getcapacity', short_help="""Return the high-level capacity measurements for an entire cluster. The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface. """, cls=SolidFireCommand)
@pass_context
def getcapacity(ctx):
    """Return the high-level capacity measurements for an entire cluster."""
    """The fields returned from this method can be used to calculate the efficiency rates that are displayed in the Element User Interface."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetClusterCapacityResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetClusterCapacityResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyfullthreshold', short_help="""ModifyClusterFullThreshold is used to change the level at which an event is generated when the storage cluster approaches the capacity utilization requested. The number entered in this setting is used to indicate the number of node failures the system is required to recover from. For example, on a 10 node cluster, if you want to be alerted when the system cannot recover from 3 nodes failures, enter the value of "3". When this number is reached, a message alert is sent to the Event Log in the Cluster Management Console. """, cls=SolidFireCommand)
@click.option('--stage2awarethreshold',
              type=int,
              required=False,
              help="""Number of nodes worth of capacity remaining on the cluster that triggers a notification. """)
@click.option('--stage3blockthresholdpercent',
              type=int,
              required=False,
              help="""Percent below "Error" state to raise a cluster "Warning" alert. """)
@click.option('--maxmetadataoverprovisionfactor',
              type=int,
              required=False,
              help="""A value representative of the number of times metadata space can be over provisioned relative to the amount of space available. For example, if there was enough metadata space to store 100 TiB of volumes and this number was set to 5, then 500 TiB worth of volumes could be created. """)
@pass_context
def modifyfullthreshold(ctx,
           # Optional main parameter
           stage2awarethreshold = None,
           # Optional main parameter
           stage3blockthresholdpercent = None,
           # Optional main parameter
           maxmetadataoverprovisionfactor = None):
    """ModifyClusterFullThreshold is used to change the level at which an event is generated when the storage cluster approaches the capacity utilization requested. The number entered in this setting is used to indicate the number of node failures the system is required to recover from. For example, on a 10 node cluster, if you want to be alerted when the system cannot recover from 3 nodes failures, enter the value of &quot;3&quot;. When this number is reached, a message alert is sent to the Event Log in the Cluster Management Console."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""stage2awarethreshold = """+str(stage2awarethreshold)+""";"""+"""stage3blockthresholdpercent = """+str(stage3blockthresholdpercent)+""";"""+"""maxmetadataoverprovisionfactor = """+str(maxmetadataoverprovisionfactor)+""";"""+"")
    try:
        _ModifyClusterFullThresholdResult = ctx.element.(stage2_aware_threshold=stage2awarethreshold, stage3_block_threshold_percent=stage3blockthresholdpercent, max_metadata_over_provision_factor=maxmetadataoverprovisionfactor)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyClusterFullThresholdResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getmasternodeid', short_help="""GetClusterMasterNodeID is used to return the ID of the node that can perform cluster-wide administration tasks and holds the storage virtual IP (SVIP) and management virtual IP (MVIP). """, cls=SolidFireCommand)
@pass_context
def getmasternodeid(ctx):
    """GetClusterMasterNodeID is used to return the ID of the node that can perform cluster-wide administration tasks and holds the storage virtual IP (SVIP) and management virtual IP (MVIP)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetClusterMasterNodeIDResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetClusterMasterNodeIDResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setsnmpinfo', short_help="""SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo.  Note: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future. """, cls=SolidFireCommand)
@click.option('--networks',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["accessnetworks", "cidr", "community", "network", ],
              required=False,
              help="""List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. SNMP v2 only.  Has the following subparameters: --accessnetworks --cidr --community --network """)
@click.option('--accessnetworks',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] ro: read-only access.* rw: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all networks other than the default "localhost" be set to "ro" access, because all SolidFire MIB objects are read-only. """,
              cls=SolidFireOption)
@click.option('--cidr',
              required=False,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] A CIDR network mask. This network mask must be an integer greater than or equal to 0, and less than or equal to 32. It must also not be equal to 31. """,
              cls=SolidFireOption)
@click.option('--community',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] SNMP community string. """,
              cls=SolidFireOption)
@click.option('--network',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] This parameter along with the cidr variable is used to control which network the access and community string apply to. The special value of "default" is used to specify an entry that applies to all networks. The cidr mask is ignored when network value is either a host name or default. """,
              cls=SolidFireOption)
@click.option('--enabled',
              type=bool,
              required=False,
              help="""If set to "true", then SNMP is enabled on each node in the cluster. """)
@click.option('--snmpv3enabled',
              type=bool,
              required=False,
              help="""If set to "true", then SNMP v3 is enabled on each node in the cluster. """)
@click.option('--usmusers',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["accessusmusers", "name", "password", "passphrase", "seclevel", ],
              required=False,
              help="""If SNMP v3 is enabled, this value must be passed in place of the "networks" parameter. SNMP v3 only.  Has the following subparameters: --accessusmusers --name --password --passphrase --seclevel """)
@click.option('--accessusmusers',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] rouser: read-only access.* rwuser: for read-write access. rosys: for read-only access to a restricted set of system information *SolidFire recommends that all USM users be set to "rouser" access, because all SolidFire MIB objects are read-only. """,
              cls=SolidFireOption)
@click.option('--name',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The name of the user. Must contain at least one character, but no more than 32 characters. Blank spaces are not allowed. """,
              cls=SolidFireOption)
@click.option('--password',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The password of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "auth" or "priv." """,
              cls=SolidFireOption)
@click.option('--passphrase',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The passphrase of the user. Must be between 8 and 255 characters long (inclusive). Blank spaces are not allowed. Required if "secLevel" is "priv." """,
              cls=SolidFireOption)
@click.option('--seclevel',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] noauth: No password or passphrase is required. auth: A password is required for user access. priv: A password and passphrase is required for user access. """,
              cls=SolidFireOption)
@pass_context
def setsnmpinfo(ctx,
           # Optional main parameter
           networks = None,
           # Optional subparameter of optional main parameter.
           accessnetworks = None,
           # Optional subparameter of optional main parameter.
           cidr = None,
           # Optional subparameter of optional main parameter.
           community = None,
           # Optional subparameter of optional main parameter.
           network = None,
           # Optional main parameter
           enabled = None,
           # Optional main parameter
           snmpv3enabled = None,
           # Optional main parameter
           usmusers = None,
           # Optional subparameter of optional main parameter.
           accessusmusers = None,
           # Optional subparameter of optional main parameter.
           name = None,
           # Optional subparameter of optional main parameter.
           password = None,
           # Optional subparameter of optional main parameter.
           passphrase = None,
           # Optional subparameter of optional main parameter.
           seclevel = None):
    """SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo."""
    """"""
    """Note: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    networksArray = []
    if(networks is not None):
        try:
            for i, _networks in enumerate(networks):
                networksArray.append(SnmpNetwork(access=accessnetworks[i], cidr=cidr[i], community=community[i], network=network[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)            

    usmusersArray = []
    if(usmusers is not None):
        try:
            for i, _usmusers in enumerate(usmusers):
                usmusersArray.append(SnmpV3UsmUser(access=accessusmusers[i], name=name[i], password=password[i], passphrase=passphrase[i], sec_level=seclevel[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""networks = """+str(networks)+""";"""+"""enabled = """+str(enabled)+""";"""+"""snmpv3enabled = """+str(snmpv3enabled)+""";"""+"""usmusers = """+str(usmusers)+""";"""+"")
    try:
        _SetSnmpInfoResult = ctx.element.(networks=networksArray, enabled=enabled, snmp_v3_enabled=snmpv3enabled, usm_users=usmusersArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetSnmpInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getfullthreshold', short_help="""GetClusterFullThreshold is used to view the stages set for cluster fullness levels. All levels are returned when this method is entered. """, cls=SolidFireCommand)
@pass_context
def getfullthreshold(ctx):
    """GetClusterFullThreshold is used to view the stages set for cluster fullness levels. All levels are returned when this method is entered."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetClusterFullThresholdResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetClusterFullThresholdResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enableencryptionatrest', short_help="""The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed. Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need. Note: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed. """, cls=SolidFireCommand)
@pass_context
def enableencryptionatrest(ctx):
    """The EnableEncryptionAtRest method is used to enable the Advanced Encryption Standard (AES) 256-bit encryption at rest on the cluster so that the cluster can manage the encryption key used for the drives on each node. This feature is not enabled by default. Enabling this operation allows the cluster to automatically manage encryption keys internally for the drives on each node in the cluster. Nodes do not store the keys to unlock drives and the keys are never passed over the network. Two nodes participating in a cluster are required to access the key to disable encryption on a drive. The encryption management does not affect performance or efficiency on the cluster. If an encryption-enabled drive or node is removed from the cluster with the API, all data is secure erased and any data left on the drive cannot be read or accessed."""
    """Enabling or disabling encryption should be performed when the cluster is running and in a healthy state. Encryption can be enabled or disabled at your discretion and can be performed as often as you need."""
    """Note: This process is asynchronous and returns a response before encryption is enabled. The GetClusterInfo method can be used to poll the system to see when the process has completed."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _EnableEncryptionAtRestResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_EnableEncryptionAtRestResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

