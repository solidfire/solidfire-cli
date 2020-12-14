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
    """enableidpauthentication getidpauthenticationstate disableidpauthentication deleteidpconfiguration listidpconfigurations createidpconfiguration addidpclusteradmin updateidpconfiguration """

@cli.command('enableidpauthentication', short_help="""Enable support for authentication using a third party Identity Provider (IdP) for the cluster. Once IdP authentication is enabled, cluster and Ldap admins will no longer be able to access the cluster via supported UIs and any active authenticated sessions will be invalidated/logged out. Only third party IdP authenticated users will be able to access the cluster via the supported UIs. """, cls=SolidFireCommand)
@click.option('--idpconfigurationid',
              type=str,
              required=False,
              help="""UUID for the third party Identity Provider (IdP) Configuration.   If only one IdP Configuration exists, then we will default to enabling that configuration. """)
@pass_context
def enableidpauthentication(ctx,
           # Optional main parameter
           idpconfigurationid = None):
    """Enable support for authentication using a third party Identity Provider (IdP) for the cluster."""
    """Once IdP authentication is enabled, cluster and Ldap admins will no longer be able to access the cluster via supported UIs and any active authenticated sessions will be invalidated/logged out."""
    """Only third party IdP authenticated users will be able to access the cluster via the supported UIs."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""idpconfigurationid = """+str(idpconfigurationid)+""";"""+"")
    try:
        _EnableIdpAuthenticationResult = ctx.element.enable_idp_authentication(idp_configuration_id=idpconfigurationid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_EnableIdpAuthenticationResult), indent=4))
        return
    else:
        cli_utils.print_result(_EnableIdpAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getidpauthenticationstate', short_help="""Return information regarding the state of authentication using third party Identity Providers """, cls=SolidFireCommand)
@pass_context
def getidpauthenticationstate(ctx):
    """Return information regarding the state of authentication using third party Identity Providers"""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetIdpAuthenticationStateResult = ctx.element.get_idp_authentication_state()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetIdpAuthenticationStateResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetIdpAuthenticationStateResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('disableidpauthentication', short_help="""Disable support for authentication using third party Identity Providers (IdP) for the cluster. Once disabled, users authenticated by third party IdPs will no longer be able to access the cluster and any active authenticated sessions will be invalidated/logged out. Ldap and cluster admins will be able to access the cluster via supported UIs. """, cls=SolidFireCommand)
@pass_context
def disableidpauthentication(ctx):
    """Disable support for authentication using third party Identity Providers (IdP) for the cluster."""
    """Once disabled, users authenticated by third party IdPs will no longer be able to access the cluster and any active authenticated sessions will be invalidated/logged out."""
    """Ldap and cluster admins will be able to access the cluster via supported UIs."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _DisableIdpAuthenticationResult = ctx.element.disable_idp_authentication()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DisableIdpAuthenticationResult), indent=4))
        return
    else:
        cli_utils.print_result(_DisableIdpAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('deleteidpconfiguration', short_help="""Delete an existing configuration with a third party Identity Provider (IdP) for the cluster. Deleting the last IdP Configuration will remove the SAML Service Provider certificate from the cluster. """, cls=SolidFireCommand)
@click.option('--idpconfigurationid',
              type=str,
              required=False,
              help="""UUID for the third party Identity Provider (IdP) Configuration. """)
@click.option('--idpname',
              type=str,
              required=False,
              help="""Name for identifying and retrieving IdP provider for SAML 2.0 single sign-on. """)
@pass_context
def deleteidpconfiguration(ctx,
           # Optional main parameter
           idpconfigurationid = None,
           # Optional main parameter
           idpname = None):
    """Delete an existing configuration with a third party Identity Provider (IdP) for the cluster."""
    """Deleting the last IdP Configuration will remove the SAML Service Provider certificate from the cluster."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""idpconfigurationid = """+str(idpconfigurationid)+";" + """idpname = """+str(idpname)+""";"""+"")
    try:
        _DeleteIdpConfigurationResult = ctx.element.delete_idp_configuration(idp_configuration_id=idpconfigurationid, idp_name=idpname)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteIdpConfigurationResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteIdpConfigurationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listidpconfigurations', short_help="""List configurations for third party Identity Provider(s) (IdP), optionally providing either enabledOnly flag to retrieve the currently enabled IdP configuration, or an IdP metadata UUID or IdP name to query a specific IdP configuration information. """, cls=SolidFireCommand)
@click.option('--idpconfigurationid',
              type=str,
              required=False,
              help="""UUID for the third party Identity Provider (IdP) Configuration. """)
@click.option('--idpname',
              type=str,
              required=False,
              help="""Filters the result to an IdP configuration information for a specific IdP name. """)
@click.option('--enabledonly',
              type=bool,
              required=False,
              help="""Filters the result to return the currently enabled Idp configuration. """)
@pass_context
def listidpconfigurations(ctx,
           # Optional main parameter
           idpconfigurationid = None,
           # Optional main parameter
           idpname = None,
           # Optional main parameter
           enabledonly = None):
    """List configurations for third party Identity Provider(s) (IdP), optionally providing either enabledOnly flag to retrieve the currently enabled IdP configuration, or an IdP metadata UUID or IdP name to query a specific IdP configuration information."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    

    ctx.logger.info(""": """"""idpconfigurationid = """+str(idpconfigurationid)+";" + """idpname = """+str(idpname)+";" + """enabledonly = """+str(enabledonly)+""";"""+"")
    try:
        _ListIdpConfigurationsResult = ctx.element.list_idp_configurations(idp_configuration_id=idpconfigurationid, idp_name=idpname, enabled_only=enabledonly)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListIdpConfigurationsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListIdpConfigurationsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createidpconfiguration', short_help="""Create a potential trust relationship for authentication using a third party Identity Provider (IdP) for the cluster.   A SAML Service Provider certificate is required for IdP communication, which will be generated as necessary. """, cls=SolidFireCommand)
@click.option('--idpname',
              type=str,
              required=True,
              prompt=True,
              help="""Name used to identify an IdP provider for SAML 2.0 single sign-on. """)
@click.option('--idpmetadata',
              type=str,
              required=True,
              prompt=True,
              help="""IdP Metadata to store. """)
@pass_context
def createidpconfiguration(ctx,
           # Mandatory main parameter
           idpname,
           # Mandatory main parameter
           idpmetadata):
    """Create a potential trust relationship for authentication using a third party Identity Provider (IdP) for the cluster.  """
    """A SAML Service Provider certificate is required for IdP communication, which will be generated as necessary."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""idpname = """ + str(idpname)+";"+"""idpmetadata = """ + str(idpmetadata)+""";"""+"")
    try:
        _CreateIdpConfigurationResult = ctx.element.create_idp_configuration(idp_name=idpname, idp_metadata=idpmetadata)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateIdpConfigurationResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateIdpConfigurationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('addidpclusteradmin', short_help="""Adds a cluster administrator user authenticated by a third party Identity Provider (IdP).   IdP cluster admin accounts are configured based on SAML attribute-value information provided  within the IdP's SAML assertion associated with the user.  If a user successfully  authenticates with the IdP and has SAML attribute statements within the SAML assertion  matching multiple IdP cluster admin accounts, the user will have the combined access level  of those matching IdP cluster admin accounts. """, cls=SolidFireCommand)
@click.option('--username',
              type=str,
              required=True,
              prompt=True,
              help="""A SAML attribute-value mapping to a IdP cluster admin (e.g. email=test@example.com).   This could be defined using a specific SAML subject using NameID, or an entry in the  SAML attribute statement such as eduPersonAffiliation. """)
@click.option('--access',
              type=str,
              required=True,
              prompt=True,
              help="""Controls which methods this IdP Cluster Admin can use. For more details on the levels of access,  see the Access Control appendix in the SolidFire API Reference. """)
@click.option('--accepteula',
              type=bool,
              required=True,
              prompt=True,
              help="""Accept the End User License Agreement. Set to true to add a cluster administrator account to the system. If omitted or set to false, the method call fails. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def addidpclusteradmin(ctx,
           # Mandatory main parameter
           username,
           # Mandatory main parameter
           access,
           # Mandatory main parameter
           accepteula,
           # Optional main parameter
           attributes = None):
    """Adds a cluster administrator user authenticated by a third party Identity Provider (IdP).  """
    """IdP cluster admin accounts are configured based on SAML attribute-value information provided """
    """within the IdP's SAML assertion associated with the user.  If a user successfully """
    """authenticates with the IdP and has SAML attribute statements within the SAML assertion """
    """matching multiple IdP cluster admin accounts, the user will have the combined access level """
    """of those matching IdP cluster admin accounts."""

    

    cli_utils.establish_connection(ctx)
    
    

    access = parser.parse_array(access)
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    

    ctx.logger.info(""": """"""username = """ + str(username)+";"+"""access = """ + str(access)+";"+"""accepteula = """ + str(accepteula)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _AddClusterAdminResult = ctx.element.add_idp_cluster_admin(username=username, access=access, accept_eula=accepteula, attributes=kwargsDict)
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



@cli.command('updateidpconfiguration', short_help="""Update an existing configuration with a third party Identity Provider (IdP) for the cluster. """, cls=SolidFireCommand)
@click.option('--idpconfigurationid',
              type=str,
              required=False,
              help="""UUID for the third party Identity Provider (IdP) Configuration. """)
@click.option('--idpname',
              type=str,
              required=False,
              help="""Name for identifying and retrieving IdP provider for SAML 2.0 single sign-on. """)
@click.option('--newidpname',
              type=str,
              required=False,
              help="""If specified replaces the IdP name. """)
@click.option('--idpmetadata',
              type=str,
              required=False,
              help="""IdP Metadata for configuration and integration details for SAML 2.0 single sign-on. """)
@click.option('--generatenewcertificate',
              type=bool,
              required=False,
              help="""If true, generate new SAML key/certificate and replace the existing pair.  NOTE: Replacing the existing certificate will disrupt the established trust between the Cluster and the Idp until Cluster's Service Provider metadata is reloaded at the Idp If not provided or false, the SAML certificate and key will remain unchanged. """)
@pass_context
def updateidpconfiguration(ctx,
           # Optional main parameter
           idpconfigurationid = None,
           # Optional main parameter
           idpname = None,
           # Optional main parameter
           newidpname = None,
           # Optional main parameter
           idpmetadata = None,
           # Optional main parameter
           generatenewcertificate = None):
    """Update an existing configuration with a third party Identity Provider (IdP) for the cluster."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    

    

    ctx.logger.info(""": """"""idpconfigurationid = """+str(idpconfigurationid)+";" + """idpname = """+str(idpname)+";" + """newidpname = """+str(newidpname)+";" + """idpmetadata = """+str(idpmetadata)+";" + """generatenewcertificate = """+str(generatenewcertificate)+""";"""+"")
    try:
        _UpdateIdpConfigurationResult = ctx.element.update_idp_configuration(idp_configuration_id=idpconfigurationid, idp_name=idpname, new_idp_name=newidpname, idp_metadata=idpmetadata, generate_new_certificate=generatenewcertificate)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_UpdateIdpConfigurationResult), indent=4))
        return
    else:
        cli_utils.print_result(_UpdateIdpConfigurationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


