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
    """testkeyserverkmip listkeyproviderskmip listkeyserverskmip createkeyserverkmip deletekeyserverkmip getkeyproviderkmip addkeyservertoproviderkmip removekeyserverfromproviderkmip getkeyserverkmip getclientcertificatesignrequest createpublicprivatekeypair deletekeyproviderkmip modifykeyserverkmip testkeyproviderkmip getfipsreport createkeyproviderkmip """

@cli.command('testkeyserverkmip', short_help="""Test whether the specified KMIP (Key Management Interoperability Protocol) Key Server is functioning normally. """, cls=SolidFireCommand)
@click.option('--keyserverid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the KMIP Key Server to test. """)
@pass_context
def testkeyserverkmip(ctx,
           # Mandatory main parameter
           keyserverid):
    """Test whether the specified KMIP (Key Management Interoperability Protocol) Key Server is functioning normally."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""keyserverid = """ + str(keyserverid)+""";"""+"")
    try:
        _TestKeyServerKmipResult = ctx.element.test_key_server_kmip(key_server_id=keyserverid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestKeyServerKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestKeyServerKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listkeyproviderskmip', short_help="""Returns the list of KMIP (Key Management Interoperability Protocol) Key Providers which have been created via CreateKeyProviderKmip.  The list can optionally be filtered by specifying additional parameters. """, cls=SolidFireCommand)
@click.option('--keyproviderisactive',
              type=bool,
              required=False,
              help="""If omitted, returned KMIP Key Provider objects will not be filtered based on whether they're active. If true, returns only KMIP Key Provider objects which are active (providing keys which are currently in use). If false, returns only KMIP Key Provider objects which are inactive (not providing any keys and able to be deleted). """)
@click.option('--kmipkeyproviderhasserverassigned',
              type=bool,
              required=False,
              help="""If omitted, returned KMIP Key Provider objects will not be filtered based on whether they have a KMIP Key Server assigned. If true, returns only KMIP Key Provider objects which have a KMIP Key Server assigned. If false, returns only KMIP Key Provider objects which do not have a KMIP Key Server assigned. """)
@pass_context
def listkeyproviderskmip(ctx,
           # Optional main parameter
           keyproviderisactive = None,
           # Optional main parameter
           kmipkeyproviderhasserverassigned = None):
    """Returns the list of KMIP (Key Management Interoperability Protocol) Key Providers which have been created via CreateKeyProviderKmip.  The list can optionally be filtered by specifying additional parameters."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""keyproviderisactive = """+str(keyproviderisactive)+";" + """kmipkeyproviderhasserverassigned = """+str(kmipkeyproviderhasserverassigned)+""";"""+"")
    try:
        _ListKeyProvidersKmipResult = ctx.element.list_key_providers_kmip(key_provider_is_active=keyproviderisactive, kmip_key_provider_has_server_assigned=kmipkeyproviderhasserverassigned)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListKeyProvidersKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListKeyProvidersKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listkeyserverskmip', short_help="""Returns the list of KMIP (Key Management Interoperability Protocol) Key Servers which have been created via CreateKeyServerKmip.  The list can optionally be filtered by specifying additional parameters. """, cls=SolidFireCommand)
@click.option('--keyproviderid',
              type=int,
              required=False,
              help="""If omitted, returned KMIP Key Server objects will not be filtered based on whether they're assigned to the specified KMIP Key Provider. If specified, returned KMIP Key Server objects will be filtered to those assigned to the specified KMIP Key Provider. """)
@click.option('--kmipassignedproviderisactive',
              type=bool,
              required=False,
              help="""If omitted, returned KMIP Key Server objects will not be filtered based on whether they're active. If true, returns only KMIP Key Server objects which are active (providing keys which are currently in use). If false, returns only KMIP Key Server objects which are inactive (not providing any keys and able to be deleted). """)
@click.option('--kmiphasproviderassigned',
              type=bool,
              required=False,
              help="""If omitted, returned KMIP Key Server objects will not be filtered based on whether they have a KMIP Key Provider assigned. If true, returns only KMIP Key Server objects which have a KMIP Key Provider assigned. If false, returns only KMIP Key Server objects which do not have a KMIP Key Provider assigned. """)
@pass_context
def listkeyserverskmip(ctx,
           # Optional main parameter
           keyproviderid = None,
           # Optional main parameter
           kmipassignedproviderisactive = None,
           # Optional main parameter
           kmiphasproviderassigned = None):
    """Returns the list of KMIP (Key Management Interoperability Protocol) Key Servers which have been created via CreateKeyServerKmip.  The list can optionally be filtered by specifying additional parameters."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    

    ctx.logger.info(""": """"""keyproviderid = """+str(keyproviderid)+";" + """kmipassignedproviderisactive = """+str(kmipassignedproviderisactive)+";" + """kmiphasproviderassigned = """+str(kmiphasproviderassigned)+""";"""+"")
    try:
        _ListKeyServersKmipResult = ctx.element.list_key_servers_kmip(key_provider_id=keyproviderid, kmip_assigned_provider_is_active=kmipassignedproviderisactive, kmip_has_provider_assigned=kmiphasproviderassigned)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListKeyServersKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListKeyServersKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createkeyserverkmip', short_help="""Creates a KMIP (Key Management Interoperability Protocol) Key Server with the specified attributes. The server will not be contacted as part of this operation so it need not exist or be configured prior. For clustered Key Server configurations, the hostnames or IP Addresses, of all server nodes, must be provided in the kmipKeyServerHostnames parameter. """, cls=SolidFireCommand)
@click.option('--kmipcacertificate',
              type=str,
              required=True,
              prompt=True,
              help="""The public key certificate of the external key server's root CA. This will be used to verify the certificate presented by external key server in the TLS communication. For key server clusters where individual servers use different CAs, provide a concatenated string containing the root certificates of all the CAs. """)
@click.option('--kmipclientcertificate',
              type=str,
              required=True,
              prompt=True,
              help="""A PEM format Base64 encoded PKCS#10 X.509 certificate used by the Solidfire KMIP client. """)
@click.option('--kmipkeyserverhostnames',
              type=str,
              required=True,
              prompt=True,
              help="""Array of the hostnames or IP addresses associated with this KMIP Key Server. Multiple hostnames or IP addresses must only be provided if the key servers are in a clustered configuration. """)
@click.option('--kmipkeyservername',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the KMIP Key Server.  This name is only used for display purposes and does not need to be unique. """)
@click.option('--kmipkeyserverport',
              type=int,
              required=False,
              help="""The port number associated with this KMIP Key Server (typically 5696). """)
@pass_context
def createkeyserverkmip(ctx,
           # Mandatory main parameter
           kmipcacertificate,
           # Mandatory main parameter
           kmipclientcertificate,
           # Mandatory main parameter
           kmipkeyserverhostnames,
           # Mandatory main parameter
           kmipkeyservername,
           # Optional main parameter
           kmipkeyserverport = None):
    """Creates a KMIP (Key Management Interoperability Protocol) Key Server with the specified attributes. The server will not be contacted as part of this operation so it need not exist or be configured prior."""
    """For clustered Key Server configurations, the hostnames or IP Addresses, of all server nodes, must be provided in the kmipKeyServerHostnames parameter."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    kmipkeyserverhostnames = parser.parse_array(kmipkeyserverhostnames)
    
    
    

    

    ctx.logger.info(""": """"""kmipcacertificate = """ + str(kmipcacertificate)+";"+"""kmipclientcertificate = """ + str(kmipclientcertificate)+";"+"""kmipkeyserverhostnames = """ + str(kmipkeyserverhostnames)+";"+"""kmipkeyservername = """ + str(kmipkeyservername)+";" + """kmipkeyserverport = """+str(kmipkeyserverport)+""";"""+"")
    try:
        _CreateKeyServerKmipResult = ctx.element.create_key_server_kmip(kmip_ca_certificate=kmipcacertificate, kmip_client_certificate=kmipclientcertificate, kmip_key_server_hostnames=kmipkeyserverhostnames, kmip_key_server_name=kmipkeyservername, kmip_key_server_port=kmipkeyserverport)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateKeyServerKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateKeyServerKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('deletekeyserverkmip', short_help="""Delete the specified KMIP (Key Management Interoperability Protocol) Key Server.  A KMIP Key Server can be deleted unless it's the last one assigned to its provider, and that provider is active (providing keys which are currently in use). """, cls=SolidFireCommand)
@click.option('--keyserverid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the KMIP Key Server to delete. """)
@pass_context
def deletekeyserverkmip(ctx,
           # Mandatory main parameter
           keyserverid):
    """Delete the specified KMIP (Key Management Interoperability Protocol) Key Server.  A KMIP Key Server can be deleted unless it's the last one assigned to its provider, and that provider is active (providing keys which are currently in use)."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""keyserverid = """ + str(keyserverid)+""";"""+"")
    try:
        _DeleteKeyServerKmipResult = ctx.element.delete_key_server_kmip(key_server_id=keyserverid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteKeyServerKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteKeyServerKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getkeyproviderkmip', short_help="""Returns the specified KMIP (Key Management Interoperability Protocol) Key Provider object. """, cls=SolidFireCommand)
@click.option('--keyproviderid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the KMIP Key Provider object to return. """)
@pass_context
def getkeyproviderkmip(ctx,
           # Mandatory main parameter
           keyproviderid):
    """Returns the specified KMIP (Key Management Interoperability Protocol) Key Provider object."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""keyproviderid = """ + str(keyproviderid)+""";"""+"")
    try:
        _GetKeyProviderKmipResult = ctx.element.get_key_provider_kmip(key_provider_id=keyproviderid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetKeyProviderKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetKeyProviderKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('addkeyservertoproviderkmip', short_help="""Adds (assigns) the specified KMIP (Key Management Interoperability Protocol) Key Server to the specified Key Provider.  This will result in contacting the server to verify it's functional, as well as to synchronize keys in the event that there are multiple key servers assigned to the provider.  This synchronization may result in conflicts which could cause this to fail.  If the specified KMIP Key Server is already assigned to the specified Key Provider, this is a no-op and no error will be returned.  The assignment can be removed (unassigned) using RemoveKeyServerFromProviderKmip. """, cls=SolidFireCommand)
@click.option('--keyproviderid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the Key Provider to assign the KMIP Key Server to. """)
@click.option('--keyserverid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the KMIP Key Server to assign. """)
@pass_context
def addkeyservertoproviderkmip(ctx,
           # Mandatory main parameter
           keyproviderid,
           # Mandatory main parameter
           keyserverid):
    """Adds (assigns) the specified KMIP (Key Management Interoperability Protocol) Key Server to the specified Key Provider.  This will result in contacting the server to verify it's functional, as well as to synchronize keys in the event that there are multiple key servers assigned to the provider.  This synchronization may result in conflicts which could cause this to fail.  If the specified KMIP Key Server is already assigned to the specified Key Provider, this is a no-op and no error will be returned.  The assignment can be removed (unassigned) using RemoveKeyServerFromProviderKmip."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    

    ctx.logger.info(""": """"""keyproviderid = """ + str(keyproviderid)+";"+"""keyserverid = """ + str(keyserverid)+""";"""+"")
    try:
        _AddKeyServerToProviderKmipResult = ctx.element.add_key_server_to_provider_kmip(key_provider_id=keyproviderid, key_server_id=keyserverid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AddKeyServerToProviderKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_AddKeyServerToProviderKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('removekeyserverfromproviderkmip', short_help="""Remove (unassign) the specified KMIP (Key Management Interoperability Protocol) Key Server from the provider it was assigned to via AddKeyServerToProviderKmip (if any).  A KMIP Key Server can be unassigned from its provider unless it's the last one and that provider is active (providing keys which are currently in use).  If the specified KMIP Key Server is not assigned to a provider, this is a no-op and no error will be returned. """, cls=SolidFireCommand)
@click.option('--keyserverid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the KMIP Key Server to unassign. """)
@pass_context
def removekeyserverfromproviderkmip(ctx,
           # Mandatory main parameter
           keyserverid):
    """Remove (unassign) the specified KMIP (Key Management Interoperability Protocol) Key Server from the provider it was assigned to via AddKeyServerToProviderKmip (if any).  A KMIP Key Server can be unassigned from its provider unless it's the last one and that provider is active (providing keys which are currently in use).  If the specified KMIP Key Server is not assigned to a provider, this is a no-op and no error will be returned."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""keyserverid = """ + str(keyserverid)+""";"""+"")
    try:
        _RemoveKeyServerFromProviderKmipResult = ctx.element.remove_key_server_from_provider_kmip(key_server_id=keyserverid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveKeyServerFromProviderKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveKeyServerFromProviderKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getkeyserverkmip', short_help="""Returns the specified KMIP (Key Management Interoperability Protocol) Key Server object. """, cls=SolidFireCommand)
@click.option('--keyserverid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the KMIP Key Server object to return. """)
@pass_context
def getkeyserverkmip(ctx,
           # Mandatory main parameter
           keyserverid):
    """Returns the specified KMIP (Key Management Interoperability Protocol) Key Server object."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""keyserverid = """ + str(keyserverid)+""";"""+"")
    try:
        _GetKeyServerKmipResult = ctx.element.get_key_server_kmip(key_server_id=keyserverid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetKeyServerKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetKeyServerKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getclientcertificatesignrequest', short_help="""Generates a Certificate Sign Request which can be signed by a Certificate Authority to generate a client certificate for the cluster.  This is part of establishing a trust relationship for interacting with external services. """, cls=SolidFireCommand)
@pass_context
def getclientcertificatesignrequest(ctx):
    """Generates a Certificate Sign Request which can be signed by a Certificate Authority to generate a client certificate for the cluster.  This is part of establishing a trust relationship for interacting with external services."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClientCertificateSignRequestResult = ctx.element.get_client_certificate_sign_request()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClientCertificateSignRequestResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClientCertificateSignRequestResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createpublicprivatekeypair', short_help="""Creates SSL public and private keys. These keys can be used to generate Certificate Sign Requests. There can be only one key pair in use for the cluster. To replace the existing keys, make sure that they are not being used by any providers before invoking this API. """, cls=SolidFireCommand)
@click.option('--commonname',
              type=str,
              required=False,
              help="""This is the X.509 distinguished name Common Name field (CN). """)
@click.option('--organization',
              type=str,
              required=False,
              help="""This is the X.509 distinguished name Organization Name field (O). """)
@click.option('--organizationalunit',
              type=str,
              required=False,
              help="""This is the X.509 distinguished name Organizational Unit Name field (OU). """)
@click.option('--locality',
              type=str,
              required=False,
              help="""This is the X.509 distinguished name Locality Name field (L). """)
@click.option('--state',
              type=str,
              required=False,
              help="""This is the X.509 distinguished name State or Province Name field (ST or SP or S). """)
@click.option('--country',
              type=str,
              required=False,
              help="""This is the X.509 distinguished name Country field (C). """)
@click.option('--emailaddress',
              type=str,
              required=False,
              help="""This is the X.509 distinguished name Email Address field (MAIL). """)
@pass_context
def createpublicprivatekeypair(ctx,
           # Optional main parameter
           commonname = None,
           # Optional main parameter
           organization = None,
           # Optional main parameter
           organizationalunit = None,
           # Optional main parameter
           locality = None,
           # Optional main parameter
           state = None,
           # Optional main parameter
           country = None,
           # Optional main parameter
           emailaddress = None):
    """Creates SSL public and private keys. These keys can be used to generate Certificate Sign Requests."""
    """There can be only one key pair in use for the cluster. To replace the existing keys, make sure that they are not being used by any providers before invoking this API."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    
    
    

    

    ctx.logger.info(""": """"""commonname = """+str(commonname)+";" + """organization = """+str(organization)+";" + """organizationalunit = """+str(organizationalunit)+";" + """locality = """+str(locality)+";" + """state = """+str(state)+";" + """country = """+str(country)+";" + """emailaddress = """+str(emailaddress)+""";"""+"")
    try:
        _CreatePublicPrivateKeyPairResult = ctx.element.create_public_private_key_pair(common_name=commonname, organization=organization, organizational_unit=organizationalunit, locality=locality, state=state, country=country, email_address=emailaddress)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreatePublicPrivateKeyPairResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreatePublicPrivateKeyPairResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('deletekeyproviderkmip', short_help="""Delete the specified inactive Key Provider. """, cls=SolidFireCommand)
@click.option('--keyproviderid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the Key Provider to delete. """)
@pass_context
def deletekeyproviderkmip(ctx,
           # Mandatory main parameter
           keyproviderid):
    """Delete the specified inactive Key Provider."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""keyproviderid = """ + str(keyproviderid)+""";"""+"")
    try:
        _DeleteKeyProviderKmipResult = ctx.element.delete_key_provider_kmip(key_provider_id=keyproviderid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteKeyProviderKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteKeyProviderKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifykeyserverkmip', short_help="""Modifies a KMIP (Key Management Interoperability Protocol) Key Server to the specified attributes. The only required parameter is the keyServerID. A request which contains only the keyServerID will be a no-op and no error will be returned. Any other parameters which are specified will replace the existing values on the KMIP Key Server with the specified keyServerID. Because this server might be part of an active provider this will result in contacting the server to verify it's functional. Multiple hostnames or IP addresses must only be provided to the kmipKeyServerHostnames parameter if the key servers are in a clustered configuration. """, cls=SolidFireCommand)
@click.option('--kmipcacertificate',
              type=str,
              required=False,
              help="""The public key certificate of the external key server's root CA. This will be used to verify the certificate presented by external key server in the TLS communication. For key server clusters where individual servers use different CAs, provide a concatenated string containing the root certificates of all the CAs. """)
@click.option('--kmipclientcertificate',
              type=str,
              required=False,
              help="""A PEM format Base64 encoded PKCS#10 X.509 certificate used by the Solidfire KMIP client. """)
@click.option('--kmipkeyserverhostnames',
              type=str,
              required=False,
              help="""Array of the hostnames or IP addresses associated with this KMIP Key Server. Multiple hostnames or IP addresses must only be provided if the key servers are in a clustered configuration. """)
@click.option('--keyserverid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the KMIP Key Server to modify. """)
@click.option('--kmipkeyservername',
              type=str,
              required=False,
              help="""The name of the KMIP Key Server.  This name is only used for display purposes and does not need to be unique. """)
@click.option('--kmipkeyserverport',
              type=int,
              required=False,
              help="""The port number associated with this KMIP Key Server (typically 5696). """)
@pass_context
def modifykeyserverkmip(ctx,
           # Mandatory main parameter
           keyserverid,
           # Optional main parameter
           kmipcacertificate = None,
           # Optional main parameter
           kmipclientcertificate = None,
           # Optional main parameter
           kmipkeyserverhostnames = None,
           # Optional main parameter
           kmipkeyservername = None,
           # Optional main parameter
           kmipkeyserverport = None):
    """Modifies a KMIP (Key Management Interoperability Protocol) Key Server to the specified attributes. The only required parameter is the keyServerID. A request which contains only the keyServerID will be a no-op and no error will be returned. Any other parameters which are specified will replace the existing values on the KMIP Key Server with the specified keyServerID. Because this server might be part of an active provider this will result in contacting the server to verify it's functional. Multiple hostnames or IP addresses must only be provided to the kmipKeyServerHostnames parameter if the key servers are in a clustered configuration."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    kmipkeyserverhostnames = parser.parse_array(kmipkeyserverhostnames)
    
    
    
    

    

    ctx.logger.info(""": """"""keyserverid = """ + str(keyserverid)+";" + """kmipcacertificate = """+str(kmipcacertificate)+";" + """kmipclientcertificate = """+str(kmipclientcertificate)+";" + """kmipkeyserverhostnames = """+str(kmipkeyserverhostnames)+";" + """kmipkeyservername = """+str(kmipkeyservername)+";" + """kmipkeyserverport = """+str(kmipkeyserverport)+""";"""+"")
    try:
        _ModifyKeyServerKmipResult = ctx.element.modify_key_server_kmip(key_server_id=keyserverid, kmip_ca_certificate=kmipcacertificate, kmip_client_certificate=kmipclientcertificate, kmip_key_server_hostnames=kmipkeyserverhostnames, kmip_key_server_name=kmipkeyservername, kmip_key_server_port=kmipkeyserverport)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyKeyServerKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyKeyServerKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('testkeyproviderkmip', short_help="""Test whether the specified Key Provider is functioning normally. """, cls=SolidFireCommand)
@click.option('--keyproviderid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the Key Provider to test. """)
@pass_context
def testkeyproviderkmip(ctx,
           # Mandatory main parameter
           keyproviderid):
    """Test whether the specified Key Provider is functioning normally."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""keyproviderid = """ + str(keyproviderid)+""";"""+"")
    try:
        _TestKeyProviderKmipResult = ctx.element.test_key_provider_kmip(key_provider_id=keyproviderid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestKeyProviderKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestKeyProviderKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getfipsreport', short_help="""GetFipsReport enables you to retrieve FIPS compliance status on a per node basis. """, cls=SolidFireCommand)
@pass_context
def getfipsreport(ctx):
    """GetFipsReport enables you to retrieve FIPS compliance status on a per node basis."""

    

    cli_utils.establish_connection(ctx)
    

    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetFipsReportResult = ctx.element.get_fips_report()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetFipsReportResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetFipsReportResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createkeyproviderkmip', short_help="""Creates a KMIP (Key Management Interoperability Protocol) Key Provider with the specified name.  A Key Provider defines a mechanism and location to retrieve authentication keys.  A KMIP Key Provider represents a collection of one or more KMIP Key Servers.  A newly created KMIP Key Provider will not have any KMIP Key Servers assigned to it.  To create a KMIP Key Server see CreateKeyServerKmip and to assign it to a provider created via this method see AddKeyServerToProviderKmip. """, cls=SolidFireCommand)
@click.option('--keyprovidername',
              type=str,
              required=True,
              prompt=True,
              help="""The name to associate with the created KMIP Key Provider.  This name is only used for display purposes and does not need to be unique. """)
@pass_context
def createkeyproviderkmip(ctx,
           # Mandatory main parameter
           keyprovidername):
    """Creates a KMIP (Key Management Interoperability Protocol) Key Provider with the specified name.  A Key Provider defines a mechanism and location to retrieve authentication keys.  A KMIP Key Provider represents a collection of one or more KMIP Key Servers.  A newly created KMIP Key Provider will not have any KMIP Key Servers assigned to it.  To create a KMIP Key Server see CreateKeyServerKmip and to assign it to a provider created via this method see AddKeyServerToProviderKmip."""

    

    cli_utils.establish_connection(ctx)
    
    

    

    ctx.logger.info(""": """"""keyprovidername = """ + str(keyprovidername)+""";"""+"")
    try:
        _CreateKeyProviderKmipResult = ctx.element.create_key_provider_kmip(key_provider_name=keyprovidername)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateKeyProviderKmipResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateKeyProviderKmipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


