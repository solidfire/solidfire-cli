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
    """getbyname list remove getbyid add getefficiency modify """

@cli.command('getbyname', short_help="""GetAccountByName enables you to retrieve details about a specific account, given its username. """, cls=SolidFireCommand)
@click.option('--username',
              type=str,
              required=True,
              prompt=True,
              help="""Username for the account. """)
@pass_context
def getbyname(ctx,
           # Mandatory main parameter
           username):
    """GetAccountByName enables you to retrieve details about a specific account, given its username."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""username = """ + str(username)+""";"""+"")
    try:
        _GetAccountResult = ctx.element.get_account_by_name(username=username)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetAccountResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListAccounts returns the entire list of accounts, with optional paging support. """, cls=SolidFireCommand)
@click.option('--startaccountid',
              type=int,
              required=False,
              help="""Starting AccountID to return. If no account exists with this AccountID, the next account by AccountID order is used as the start of the list. To page through the list, pass the AccountID of the last account in the previous response + 1. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""Maximum number of AccountInfo objects to return. """)
@click.option('--includestoragecontainers',
              type=bool,
              required=False,
              help="""Includes storage containers in the response by default. To exclude storage containers, set to false. """)
@pass_context
def list(ctx,
           # Optional main parameter
           startaccountid = None,
           # Optional main parameter
           limit = None,
           # Optional main parameter
           includestoragecontainers = None):
    """ListAccounts returns the entire list of accounts, with optional paging support."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    

    ctx.logger.info(""": """"""startaccountid = """+str(startaccountid)+";" + """limit = """+str(limit)+";" + """includestoragecontainers = """+str(includestoragecontainers)+""";"""+"")
    try:
        _ListAccountsResult = ctx.element.list_accounts(start_account_id=startaccountid, limit=limit, include_storage_containers=includestoragecontainers)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListAccountsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListAccountsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""RemoveAccount enables you to remove an existing account. You must delete and purge all volumes associated with the account using DeleteVolume before you can remove the account. If volumes on the account are still pending deletion, you cannot use RemoveAccount to remove the account. """, cls=SolidFireCommand)
@click.option('--accountid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the AccountID for the account to be removed. """)
@pass_context
def remove(ctx,
           # Mandatory main parameter
           accountid):
    """RemoveAccount enables you to remove an existing account. You must delete and purge all volumes associated with the account"""
    """using DeleteVolume before you can remove the account. If volumes on the account are still pending deletion, you cannot use"""
    """RemoveAccount to remove the account."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""accountid = """ + str(accountid)+""";"""+"")
    try:
        _RemoveAccountResult = ctx.element.remove_account(account_id=accountid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveAccountResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getbyid', short_help="""GetAccountByID enables you to return details about a specific account, given its accountID. """, cls=SolidFireCommand)
@click.option('--accountid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the account for which details are gathered. """)
@pass_context
def getbyid(ctx,
           # Mandatory main parameter
           accountid):
    """GetAccountByID enables you to return details about a specific account, given its accountID."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""accountid = """ + str(accountid)+""";"""+"")
    try:
        _GetAccountResult = ctx.element.get_account_by_id(account_id=accountid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetAccountResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('add', short_help="""You can use AddAccount to add a new account to the system. You can create new volumes under the new account. The CHAP settings you specify for the account apply to all volumes owned by the account. """, cls=SolidFireCommand)
@click.option('--username',
              type=str,
              required=True,
              prompt=True,
              help="""Specifies the username for this account. (Might be 1 to 64 characters in length). """)
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""The CHAP secret to use for the initiator. If unspecified, a random secret is created. """)
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""The CHAP secret to use for the target (mutual CHAP authentication). If unspecified, a random secret is created. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@click.option('--enablechap',
              type=bool,
              required=False,
              help="""Specify if chap account credentials can be used by an initiator to access volumes. """)
@pass_context
def add(ctx,
           # Mandatory main parameter
           username,
           # Optional main parameter
           initiatorsecret = None,
           # Optional main parameter
           targetsecret = None,
           # Optional main parameter
           attributes = None,
           # Optional main parameter
           enablechap = None):
    """You can use AddAccount to add a new account to the system. You can create new volumes under the new account. The CHAP settings you specify for the account apply to all volumes owned by the account."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    
    
    if initiatorsecret == "AUTO-GENERATE-CHAP-SECRET":
        initiatorsecret = CHAPSecret.auto_generate()
    if targetsecret == "AUTO-GENERATE-CHAP-SECRET":
        targetsecret = CHAPSecret.auto_generate()

    

    ctx.logger.info(""": """"""username = """ + str(username)+";" + """initiatorsecret = """+str(initiatorsecret)+";" + """targetsecret = """+str(targetsecret)+";" + """attributes = """+str(kwargsDict)+";" + """enablechap = """+str(enablechap)+""";"""+"")
    try:
        _AddAccountResult = ctx.element.add_account(username=username, initiator_secret=initiatorsecret, target_secret=targetsecret, attributes=kwargsDict, enable_chap=enablechap)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AddAccountResult), indent=4))
        return
    else:
        cli_utils.print_result(_AddAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getefficiency', short_help="""GetAccountEfficiency enables you to retrieve efficiency statistics about a volume account. This method returns efficiency information only for the account you specify as a parameter. """, cls=SolidFireCommand)
@click.option('--accountid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the volume account for which efficiency statistics are returned. """)
@pass_context
def getefficiency(ctx,
           # Mandatory main parameter
           accountid):
    """GetAccountEfficiency enables you to retrieve efficiency statistics about a volume account. This method returns efficiency information"""
    """only for the account you specify as a parameter."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""accountid = """ + str(accountid)+""";"""+"")
    try:
        _GetEfficiencyResult = ctx.element.get_account_efficiency(account_id=accountid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetEfficiencyResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""ModifyAccount enables you to modify an existing account. When you lock an account, any existing connections from that account are immediately terminated. When you change an account's CHAP settings, any existing connections remain active, and the new CHAP settings are used on subsequent connections or reconnections. To clear an account's attributes, specify {} for the attributes parameter. """, cls=SolidFireCommand)
@click.option('--accountid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the AccountID for the account to be modified. """)
@click.option('--username',
              type=str,
              required=False,
              help="""Specifies the username associated with the account. (Might be 1 to 64 characters in length). """)
@click.option('--status',
              type=str,
              required=False,
              help="""Sets the status for the account. Possible values are: active: The account is active and connections are allowed. locked: The account is locked and connections are refused. """)
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""The CHAP secret to use for the initiator. """)
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""The CHAP secret to use for the target (mutual CHAP authentication). """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@click.option('--enablechap',
              type=bool,
              required=False,
              help="""Specify if chap account credentials can be used by an initiator to access volumes. """)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           accountid,
           # Optional main parameter
           username = None,
           # Optional main parameter
           status = None,
           # Optional main parameter
           initiatorsecret = None,
           # Optional main parameter
           targetsecret = None,
           # Optional main parameter
           attributes = None,
           # Optional main parameter
           enablechap = None):
    """ModifyAccount enables you to modify an existing account."""
    """When you lock an account, any existing connections from that account are immediately terminated. When you change an account's"""
    """CHAP settings, any existing connections remain active, and the new CHAP settings are used on subsequent connections or"""
    """reconnections."""
    """To clear an account's attributes, specify {} for the attributes parameter."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    
    
    if initiatorsecret == "AUTO-GENERATE-CHAP-SECRET":
        initiatorsecret = CHAPSecret.auto_generate()
    if targetsecret == "AUTO-GENERATE-CHAP-SECRET":
        targetsecret = CHAPSecret.auto_generate()

    

    ctx.logger.info(""": """"""accountid = """ + str(accountid)+";" + """username = """+str(username)+";" + """status = """+str(status)+";" + """initiatorsecret = """+str(initiatorsecret)+";" + """targetsecret = """+str(targetsecret)+";" + """attributes = """+str(kwargsDict)+";" + """enablechap = """+str(enablechap)+""";"""+"")
    try:
        _ModifyAccountResult = ctx.element.modify_account(account_id=accountid, username=username, status=status, initiator_secret=initiatorsecret, target_secret=targetsecret, attributes=kwargsDict, enable_chap=enablechap)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyAccountResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


