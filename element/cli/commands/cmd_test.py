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
    """list connectsvip ping connectmvip listutilities connectensemble """

@cli.command('list', short_help="""You can use the ListTests API method to return the tests that are available to run on a node. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def list(ctx):
    """You can use the ListTests API method to return the tests that are available to run on a node."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListTestsResult = ctx.element.list_tests()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListTestsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListTestsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('connectsvip', short_help="""The TestConnectSvip API method enables you to test the storage connection to the cluster. The test pings the SVIP using ICMP packets, and when successful, connects as an iSCSI initiator. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--svip',
              type=str,
              required=False,
              help="""If specified, tests the storage connection of a different SVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. """)
@pass_context
def connectsvip(ctx,
           # Optional main parameter
           svip = None):
    """The TestConnectSvip API method enables you to test the storage connection to the cluster. The test pings the SVIP using ICMP packets, and when successful, connects as an iSCSI initiator."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""svip = """+str(svip)+""";"""+"")
    try:
        _TestConnectSvipResult = ctx.element.test_connect_svip(svip=svip)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestConnectSvipResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestConnectSvipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ping', short_help="""The TestPing API allows to test the reachability to IP address(s) using ICMP packets. Source address(v4 or v6), interface and vlan tag can be specified. If not Bond1G/10G network is used to reach the target address. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--attempts',
              type=int,
              required=False,
              help="""Specifies the number of times the system should repeat the test ping. The default value is 5. """)
@click.option('--hosts',
              type=str,
              required=False,
              help="""Specifies a comma-separated list of addresses or hostnames of devices to ping. """)
@click.option('--totaltimeoutsec',
              type=int,
              required=False,
              help="""Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. """)
@click.option('--packetsize',
              type=int,
              required=False,
              help="""Specifies the number of bytes to send in the ICMP packet that is sent to each IP. The number must be less than the maximum MTU specified in the network configuration. """)
@click.option('--pingtimeoutmsec',
              type=int,
              required=False,
              help="""Specifies the number of milliseconds to wait for each individual ping response. The default value is 500 ms. """)
@click.option('--prohibitfragmentation',
              type=bool,
              required=False,
              help="""Specifies that the Do not Fragment (DF) flag is enabled for the ICMP packets. """)
@click.option('--sourceaddressv4',
              type=str,
              required=False,
              help="""The ipv4 source address to be used in the ICMP ping packets sourceAddressV4 or sourceAddressV6 is required """)
@click.option('--sourceaddressv6',
              type=str,
              required=False,
              help="""The ipv6 source address to be used in the ICMP ping packets sourceAddressV4 or sourceAddressV6 is required """)
@click.option('--interface',
              type=str,
              required=False,
              help="""Existing interface on which the temporary vlan interface is created """)
@click.option('--virtualnetworktag',
              type=int,
              required=False,
              help="""VLAN on which host addresses reachability needs to be tested The temporary vlan interface is created with this tag """)
@pass_context
def ping(ctx,
           # Optional main parameter
           attempts = None,
           # Optional main parameter
           hosts = None,
           # Optional main parameter
           totaltimeoutsec = None,
           # Optional main parameter
           packetsize = None,
           # Optional main parameter
           pingtimeoutmsec = None,
           # Optional main parameter
           prohibitfragmentation = None,
           # Optional main parameter
           sourceaddressv4 = None,
           # Optional main parameter
           sourceaddressv6 = None,
           # Optional main parameter
           interface = None,
           # Optional main parameter
           virtualnetworktag = None):
    """The TestPing API allows to test the reachability to IP address(s) using ICMP packets. Source address(v4 or v6), interface and vlan tag can be specified. If not Bond1G/10G network is used to reach the target address."""
    """The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    
    
    
    
    
    

    

    ctx.logger.info(""": """"""attempts = """+str(attempts)+";" + """hosts = """+str(hosts)+";" + """totaltimeoutsec = """+str(totaltimeoutsec)+";" + """packetsize = """+str(packetsize)+";" + """pingtimeoutmsec = """+str(pingtimeoutmsec)+";" + """prohibitfragmentation = """+str(prohibitfragmentation)+";" + """sourceaddressv4 = """+str(sourceaddressv4)+";" + """sourceaddressv6 = """+str(sourceaddressv6)+";" + """interface = """+str(interface)+";" + """virtualnetworktag = """+str(virtualnetworktag)+""";"""+"")
    try:
        _TestPingResult = ctx.element.test_ping(attempts=attempts, hosts=hosts, total_timeout_sec=totaltimeoutsec, packet_size=packetsize, ping_timeout_msec=pingtimeoutmsec, prohibit_fragmentation=prohibitfragmentation, source_address_v4=sourceaddressv4, source_address_v6=sourceaddressv6, interface=interface, virtual_network_tag=virtualnetworktag)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestPingResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestPingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('connectmvip', short_help="""The TestConnectMvip API method enables you to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--mvip',
              type=str,
              required=False,
              help="""If specified, tests the management connection of a different MVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. """)
@pass_context
def connectmvip(ctx,
           # Optional main parameter
           mvip = None):
    """The TestConnectMvip API method enables you to test the"""
    """management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""mvip = """+str(mvip)+""";"""+"")
    try:
        _TestConnectMvipResult = ctx.element.test_connect_mvip(mvip=mvip)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestConnectMvipResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestConnectMvipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listutilities', short_help="""You can use the ListUtilities API method to return the operations that are available to run on a node.  Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def listutilities(ctx):
    """You can use the ListUtilities API method to return the operations that are available to run on a node. """
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListUtilitiesResult = ctx.element.list_utilities()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListUtilitiesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListUtilitiesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('connectensemble', short_help="""The TestConnectEnsemble API method enables you to verify connectivity with a specified database ensemble. By default, it uses the ensemble for the cluster that the node is associated with. Alternatively, you can provide a different ensemble to test connectivity with. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--ensemble',
              type=str,
              required=False,
              help="""Uses a comma-separated list of ensemble node cluster IP addresses to test connectivity. This parameter is optional. """)
@pass_context
def connectensemble(ctx,
           # Optional main parameter
           ensemble = None):
    """The TestConnectEnsemble API method enables you to verify connectivity with a specified database ensemble. By default, it uses the ensemble for the cluster that the node is associated with. Alternatively, you can provide a different ensemble to test connectivity with."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""ensemble = """+str(ensemble)+""";"""+"")
    try:
        _TestConnectEnsembleResult = ctx.element.test_connect_ensemble(ensemble=ensemble)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestConnectEnsembleResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestConnectEnsembleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


