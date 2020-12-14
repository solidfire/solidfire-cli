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
    """add remove deleteauthsessionsbyusername listactiveauthsessions modify list getcurrent listauthsessionsbyusername deleteauthsessionsby setloginbanner listauthsessionsby deleteauthsession getloginbanner """

@cli.command('add', short_help="""You can use AddClusterAdmin to add a new cluster admin account. A cluster ddmin can manage the cluster using the API and management tools. Cluster admins are completely separate and unrelated to standard tenant accounts. Each cluster admin can be restricted to a subset of the API. NetApp recommends using multiple cluster admin accounts for different users and applications. You should give each cluster admin the minimal permissions necessary; this reduces the potential impact of credential compromise. You must accept the End User License Agreement (EULA) by setting the acceptEula parameter to true to add a cluster administrator account to the system. """, cls=SolidFireCommand)
@click.option('--username',
              type=str,
              required=True,
              prompt=True,
              help="""Unique username for this cluster admin. Must be between 1 and 1024 characters in length. """)
@click.option('--password',
              type=str,
              required=True,
              prompt=True,
              help="""Password used to authenticate this cluster admin. """)
@click.option('--access',
              type=str,
              required=True,
              prompt=True,
              help="""Controls which methods this cluster admin can use. For more details on the levels of access, see Access Control in the Element API Reference Guide. """)
@click.option('--accepteula',
              type=bool,
              required=True,
              prompt=True,
              help="""Required to indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def add(ctx,
           # Mandatory main parameter
           username,
           # Mandatory main parameter
           password,
           # Mandatory main parameter
           access,
           # Mandatory main parameter
           accepteula,
           # Optional main parameter
           attributes = None):
    """You can use AddClusterAdmin to add a new cluster admin account. A cluster ddmin can manage the cluster using the API and management tools. Cluster admins are completely separate and unrelated to standard tenant accounts."""
    """Each cluster admin can be restricted to a subset of the API. NetApp recommends using multiple cluster admin accounts for different users and applications. You should give each cluster admin the minimal permissions necessary; this reduces the potential impact of credential compromise."""
    """You must accept the End User License Agreement (EULA) by setting the acceptEula parameter to true to add a cluster administrator account to the system."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    access = parser.parse_array(access)
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    

    ctx.logger.info(""": """"""username = """ + str(username)+";"+"""password = """ + str(password)+";"+"""access = """ + str(access)+";"+"""accepteula = """ + str(accepteula)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _AddClusterAdminResult = ctx.element.add_cluster_admin(username=username, password=password, access=access, accept_eula=accepteula, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AddClusterAdminResult), indent=4))
        return
    else:
        cli_utils.print_result(_AddClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""One can use this API to remove a local cluster admin, an LDAP cluster admin, or a third  party Identity Provider (IdP) cluster admin.   One cannot remove the administrator cluster admin account.   When an IdP Admin is removed that has authenticated sessions associated with a third party  Identity Provider (IdP), those sessions will either logout or possibly experience a loss of  access rights within their current session.  The access rights loss will depend on whether the  removed IdP cluster admin matched one of multiple IdP cluster admins from a given user's  SAML Attributes and the remaining set of matching IdP cluster admins results in a reduced  set of aggregate access rights.   Other cluster admin user types will be logged out upon their cluster admin removal. """, cls=SolidFireCommand)
@click.option('--clusteradminid',
              type=int,
              required=True,
              prompt=True,
              help="""ClusterAdminID for the cluster admin to remove. """)
@pass_context
def remove(ctx,
           # Mandatory main parameter
           clusteradminid):
    """One can use this API to remove a local cluster admin, an LDAP cluster admin, or a third """
    """party Identity Provider (IdP) cluster admin.  """
    """One cannot remove the administrator cluster admin account.  """
    """When an IdP Admin is removed that has authenticated sessions associated with a third party """
    """Identity Provider (IdP), those sessions will either logout or possibly experience a loss of """
    """access rights within their current session.  The access rights loss will depend on whether the """
    """removed IdP cluster admin matched one of multiple IdP cluster admins from a given user's """
    """SAML Attributes and the remaining set of matching IdP cluster admins results in a reduced """
    """set of aggregate access rights.  """
    """Other cluster admin user types will be logged out upon their cluster admin removal."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""clusteradminid = """ + str(clusteradminid)+""";"""+"")
    try:
        _RemoveClusterAdminResult = ctx.element.remove_cluster_admin(cluster_admin_id=clusteradminid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveClusterAdminResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('deleteauthsessionsbyusername', short_help="""Deletes all auth sessions for the given user. A caller not in AccessGroup ClusterAdmins / Administrator may only delete their own sessions. A caller with ClusterAdmins / Administrator privileges may delete sessions belonging to any user. To see the list of sessions that could be deleted, use ListAuthSessionsByUsername with the same parameters. """, cls=SolidFireCommand)
@click.option('--username',
              type=str,
              required=False,
              help="""Name that uniquely identifies the user. When authMethod is Cluster, this specifies the ClusterAdmin username. When authMethod is Ldap, this specifies the user's LDAP DN. When authMethod is Idp, this may specify the user's IdP uid or NameID. If the IdP is not configured to return either, this specifies a random UUID issued when the session was created. Only a caller in the ClusterAdmins / Administrator AccessGroup can provide this parameter. """)
@click.option('--authmethod',
              type=AuthMethod,
              required=False,
              help="""Authentication method of the user sessions to be deleted. Only a caller in the ClusterAdmins / Administrator AccessGroup can provide this parameter. """)
@pass_context
def deleteauthsessionsbyusername(ctx,
           # Optional main parameter
           username = None,
           # Optional main parameter
           authmethod = None):
    """Deletes all auth sessions for the given user."""
    """A caller not in AccessGroup ClusterAdmins / Administrator may only delete their own sessions."""
    """A caller with ClusterAdmins / Administrator privileges may delete sessions belonging to any user."""
    """To see the list of sessions that could be deleted, use ListAuthSessionsByUsername with the same parameters."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    
    if authmethod is not None:
        authmethod = authmethod.get_value()

    ctx.logger.info(""": """"""username = """+str(username)+";" + """authmethod = """+str(authmethod)+""";"""+"")
    try:
        _DeleteAuthSessionsResult = ctx.element.delete_auth_sessions_by_username(username=username, auth_method=authmethod)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteAuthSessionsResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteAuthSessionsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listactiveauthsessions', short_help="""Lists all active auth sessions. This is only callable by a user with Administrative access rights. """, cls=SolidFireCommand)
@pass_context
def listactiveauthsessions(ctx):
    """Lists all active auth sessions."""
    """This is only callable by a user with Administrative access rights."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListAuthSessionsResult = ctx.element.list_active_auth_sessions()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListAuthSessionsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListAuthSessionsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""You can use ModifyClusterAdmin to change the settings for a cluster admin, LDAP cluster admin,  or third party Identity Provider (IdP) cluster admin.  You cannot change access for the  administrator cluster admin account. """, cls=SolidFireCommand)
@click.option('--clusteradminid',
              type=int,
              required=True,
              prompt=True,
              help="""ClusterAdminID for the cluster admin, LDAP cluster admin, or IdP cluster admin to modify. """)
@click.option('--password',
              type=str,
              required=False,
              help="""Password used to authenticate this cluster admin. This parameter does not apply for an LDAP or IdP cluster admin. """)
@click.option('--access',
              type=str,
              required=False,
              help="""Controls which methods this cluster admin can use. For more details, see Access Control in the Element API Reference Guide. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           clusteradminid,
           # Optional main parameter
           password = None,
           # Optional main parameter
           access = None,
           # Optional main parameter
           attributes = None):
    """You can use ModifyClusterAdmin to change the settings for a cluster admin, LDAP cluster admin, """
    """or third party Identity Provider (IdP) cluster admin.  You cannot change access for the """
    """administrator cluster admin account."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    access = parser.parse_array(access)
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    

    ctx.logger.info(""": """"""clusteradminid = """ + str(clusteradminid)+";" + """password = """+str(password)+";" + """access = """+str(access)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _ModifyClusterAdminResult = ctx.element.modify_cluster_admin(cluster_admin_id=clusteradminid, password=password, access=access, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyClusterAdminResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be  several cluster administrator accounts with different levels of permissions.  There can be only  one primary cluster administrator in the system. The primary Cluster Admin is the  administrator that was created when the cluster was created. """, cls=SolidFireCommand)
@pass_context
def list(ctx):
    """ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be """
    """several cluster administrator accounts with different levels of permissions.  There can be only """
    """one primary cluster administrator in the system. The primary Cluster Admin is the """
    """administrator that was created when the cluster was created."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListClusterAdminsResult = ctx.element.list_cluster_admins()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListClusterAdminsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListClusterAdminsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getcurrent', short_help="""GetCurrentClusterAdmin returns information about the calling ClusterAdmin. If the authMethod in the return value is Ldap or Idp, then other fields in the return value may contain data aggregated from multiple LdapAdmins or IdpAdmins, respectively. """, cls=SolidFireCommand)
@pass_context
def getcurrent(ctx):
    """GetCurrentClusterAdmin returns information about the calling ClusterAdmin."""
    """If the authMethod in the return value is Ldap or Idp, then other fields in the return value may contain data aggregated from multiple LdapAdmins or IdpAdmins, respectively."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetCurrentClusterAdminResult = ctx.element.get_current_cluster_admin()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetCurrentClusterAdminResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetCurrentClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listauthsessionsbyusername', short_help="""Lists all auth sessions for the given user. A caller not in AccessGroup ClusterAdmins / Administrator privileges may only list their own sessions. A caller with ClusterAdmins / Administrator privileges may list sessions belonging to any user. """, cls=SolidFireCommand)
@click.option('--username',
              type=str,
              required=False,
              help="""Name that uniquely identifies the user. When authMethod is Cluster, this specifies the ClusterAdmin username. When authMethod is Ldap, this specifies the user's LDAP DN. When authMethod is Idp, this may specify the user's IdP uid or NameID. If the IdP is not configured to return either, this specifies a random UUID issued when the session was created. Only a caller in the ClusterAdmins / Administrator AccessGroup can provide this parameter. """)
@click.option('--authmethod',
              type=AuthMethod,
              required=False,
              help="""Authentication method of the user sessions to be listed. Only a caller in the ClusterAdmins / Administrator AccessGroup can provide this parameter. """)
@pass_context
def listauthsessionsbyusername(ctx,
           # Optional main parameter
           username = None,
           # Optional main parameter
           authmethod = None):
    """Lists all auth sessions for the given user."""
    """A caller not in AccessGroup ClusterAdmins / Administrator privileges may only list their own sessions."""
    """A caller with ClusterAdmins / Administrator privileges may list sessions belonging to any user."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    
    if authmethod is not None:
        authmethod = authmethod.get_value()

    ctx.logger.info(""": """"""username = """+str(username)+";" + """authmethod = """+str(authmethod)+""";"""+"")
    try:
        _ListAuthSessionsResult = ctx.element.list_auth_sessions_by_username(username=username, auth_method=authmethod)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListAuthSessionsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListAuthSessionsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('deleteauthsessionsby', short_help="""Deletes all auth sessions associated with the specified ClusterAdminID.  If the specified ClusterAdminID maps to a group of users, all auth sessions for all members of that group will be deleted. To see the list of sessions that could be deleted, use ListAuthSessionsByClusterAdmin with the same parameter. """, cls=SolidFireCommand)
@click.option('--clusteradminid',
              type=int,
              required=True,
              prompt=True,
              help="""ID that identifies a clusterAdmin. """)
@pass_context
def deleteauthsessionsby(ctx,
           # Mandatory main parameter
           clusteradminid):
    """Deletes all auth sessions associated with the specified ClusterAdminID. """
    """If the specified ClusterAdminID maps to a group of users, all auth sessions for all members of that group will be deleted."""
    """To see the list of sessions that could be deleted, use ListAuthSessionsByClusterAdmin with the same parameter."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""clusteradminid = """ + str(clusteradminid)+""";"""+"")
    try:
        _DeleteAuthSessionsResult = ctx.element.delete_auth_sessions_by_cluster_admin(cluster_admin_id=clusteradminid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteAuthSessionsResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteAuthSessionsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setloginbanner', short_help="""You can use the SetLoginBanner method to set the active Terms of Use banner users see when they log on to the web interface. """, cls=SolidFireCommand)
@click.option('--banner',
              type=str,
              required=False,
              help="""The desired text of the Terms of Use banner. """)
@click.option('--enabled',
              type=bool,
              required=False,
              help="""The status of the Terms of Use banner. Possible values: true: The Terms of Use banner is displayed upon web interface login. false: The Terms of Use banner is not displayed upon web interface login. """)
@pass_context
def setloginbanner(ctx,
           # Optional main parameter
           banner = None,
           # Optional main parameter
           enabled = None):
    """You can use the SetLoginBanner method to set the active Terms of Use banner users see when they log on to the web interface."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""banner = """+str(banner)+";" + """enabled = """+str(enabled)+""";"""+"")
    try:
        _SetLoginBannerResult = ctx.element.set_login_banner(banner=banner, enabled=enabled)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_SetLoginBannerResult), indent=4))
        return
    else:
        cli_utils.print_result(_SetLoginBannerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listauthsessionsby', short_help="""List all auth sessions associated with the specified ClusterAdminID.  If the specified ClusterAdminID maps to a group of users, all auth sessions for all members of that group will be listed. """, cls=SolidFireCommand)
@click.option('--clusteradminid',
              type=int,
              required=True,
              prompt=True,
              help="""ID that identifies a clusterAdmin. """)
@pass_context
def listauthsessionsby(ctx,
           # Mandatory main parameter
           clusteradminid):
    """List all auth sessions associated with the specified ClusterAdminID. """
    """If the specified ClusterAdminID maps to a group of users, all auth sessions for all members of that group will be listed."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""clusteradminid = """ + str(clusteradminid)+""";"""+"")
    try:
        _ListAuthSessionsResult = ctx.element.list_auth_sessions_by_cluster_admin(cluster_admin_id=clusteradminid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListAuthSessionsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListAuthSessionsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('deleteauthsession', short_help="""Deletes an individual auth session If the calling user is not in the ClusterAdmins / Administrator AccessGroup, only auth session belonging  to the calling user can be deleted. """, cls=SolidFireCommand)
@click.option('--sessionid',
              type=str,
              required=True,
              prompt=True,
              help="""UUID for the auth session to be deleted. """)
@pass_context
def deleteauthsession(ctx,
           # Mandatory main parameter
           sessionid):
    """Deletes an individual auth session"""
    """If the calling user is not in the ClusterAdmins / Administrator AccessGroup, only auth session belonging """
    """to the calling user can be deleted."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""sessionid = """ + str(sessionid)+""";"""+"")
    try:
        _DeleteAuthSessionResult = ctx.element.delete_auth_session(session_id=sessionid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteAuthSessionResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteAuthSessionResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getloginbanner', short_help="""You can use the GetLoginBanner method to get the currently active Terms of Use banner that users see when they log on to the web interface. """, cls=SolidFireCommand)
@pass_context
def getloginbanner(ctx):
    """You can use the GetLoginBanner method to get the currently active Terms of Use banner that users see when they log on to the web interface."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetLoginBannerResult = ctx.element.get_login_banner()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetLoginBannerResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetLoginBannerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


