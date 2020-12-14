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
    """setconfig getconfig """

@cli.command('setconfig', short_help="""Sets LLDP configuration options. If an option isn't set in the request, then it is unchanged from the previous value. """, cls=SolidFireCommand)

@click.option('--enablelldp',
              type=bool,
              required=False,
              help="""Enable the LLDP service """)

@click.option('--enablemed',
              type=bool,
              required=False,
              help="""Enable MED, an extension to LLDP that provides inventory information """)

@click.option('--enableotherprotocols',
              type=bool,
              required=False,
              help="""Enable other discovery protocols: CDP, FDP, EDP, and SONMP. """)
@pass_context
def setconfig(ctx,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           enablelldp = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           enablemed = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           enableotherprotocols = None):
    """Sets LLDP configuration options. If an option isn't set in the request, then it is unchanged from the previous value."""

    

    cli_utils.establish_connection(ctx)
    

    lldpconfig = None
    if(enablelldp is not None or
       enablemed is not None or
       enableotherprotocols is not None or
       False):
        if not ( True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
""")
        kwargsDict = dict()
        kwargsDict["enable_lldp"] = enablelldp
        kwargsDict["enable_med"] = enablemed
        kwargsDict["enable_other_protocols"] = enableotherprotocols

        lldpconfig = LldpConfig(**kwargsDict)
    

    

    ctx.logger.info(""": """"""lldpconfig = """ + str(lldpconfig)+""";"""+"")
    try:
        _GetLldpConfigResult = ctx.element.set_lldp_config(lldp_config=lldpconfig)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetLldpConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetLldpConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getconfig', short_help="""GetLldpConfig returns the current LLDP configuration for this node. """, cls=SolidFireCommand)
@pass_context
def getconfig(ctx):
    """GetLldpConfig returns the current LLDP configuration for this node."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetLldpConfigResult = ctx.element.get_lldp_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetLldpConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetLldpConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


