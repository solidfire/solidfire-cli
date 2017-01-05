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
    """AddLdapClusterAdmin DisableLdapAuthentication EnableLdapAuthentication GetLdapConfiguration TestLdapAuthentication """

@cli.command('AddLdapClusterAdmin', short_help="""AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts.  An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group. """)
@click.option('--username',
              type=str,
              required=True,
              help="""The distinguished user name for the new LDAP cluster admin. """)
@click.option('--access',
              type=str,
              required=True,
              help="""Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. """)
@click.option('--accept_eula',
              type=bool,
              required=False,
              help="""Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def AddLdapClusterAdmin(ctx,
           username,
           access,
           accept_eula = None,
           attributes = None):
    """AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts."""
    """"""
    """An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    access = parser.parse_array(access)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    AddLdapClusterAdminResult = ctx.element.add_ldap_cluster_admin(username=username, access=access, accept_eula=accept_eula, attributes=attributes)
    cli_utils.print_result(AddLdapClusterAdminResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('DisableLdapAuthentication', short_help="""The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in. """)
@pass_context
def DisableLdapAuthentication(ctx):
    """The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    DisableLdapAuthenticationResult = ctx.element.disable_ldap_authentication()
    cli_utils.print_result(DisableLdapAuthenticationResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('EnableLdapAuthentication', short_help="""The EnableLdapAuthentication method is used to configure an LDAP server connection to use for LDAP authentication to a SolidFire cluster. Users that are members on the LDAP server can then log in to a SolidFire storage system using their LDAP authentication userid and password. """)
@click.option('--auth_type',
              type=str,
              required=False,
              help="""Identifies which user authentcation method will be used. <br/> Must be one of the following:<br/> <b>DirectBind</b><br/> <b>SearchAndBind</b> (default) """)
@click.option('--group_search_base_dn',
              type=str,
              required=False,
              help="""The base DN of the tree to start the group search (will do a subtree search from here). """)
@click.option('--group_search_custom_filter',
              type=str,
              required=False,
              help="""REQUIRED for CustomFilter<br/> For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user's groups.<br/> The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. """)
@click.option('--group_search_type',
              type=str,
              required=False,
              help="""Controls the default group search filter used, can be one of the following:<br/> <b>NoGroups</b>: No group support.<br/> <b>ActiveDirectory</b>: (default) Nested membership of all of a user's AD groups.<br/> <b>MemberDN</b>: MemberDN style groups (single-level). """)
@click.option('--search_bind_dn',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind<br/> A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). """)
@click.option('--search_bind_password',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind<br/> The password for the searchBindDN account used for searching. """)
@click.option('--server_uris',
              type=str,
              required=True,
              help="""A list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") """)
@click.option('--user_dntemplate',
              type=str,
              required=False,
              help="""REQUIRED for DirectBind<br/> A string that is used to form a fully qualified user DN.<br/> The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user. """)
@click.option('--user_search_base_dn',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind The base DN of the tree used to start the search (will do a subtree search from here). """)
@click.option('--user_search_filter',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind.<br/> The LDAP filter to use.<br/> The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user.<br/> Example: (&(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login. """)
@pass_context
def EnableLdapAuthentication(ctx,
           server_uris,
           auth_type = None,
           group_search_base_dn = None,
           group_search_custom_filter = None,
           group_search_type = None,
           search_bind_dn = None,
           search_bind_password = None,
           user_dntemplate = None,
           user_search_base_dn = None,
           user_search_filter = None):
    """The EnableLdapAuthentication method is used to configure an LDAP server connection to use for LDAP authentication to a SolidFire cluster. Users that are members on the LDAP server can then log in to a SolidFire storage system using their LDAP authentication userid and password."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    server_uris = parser.parse_array(server_uris)

    EnableLdapAuthenticationResult = ctx.element.enable_ldap_authentication(server_uris=server_uris, auth_type=auth_type, group_search_base_dn=group_search_base_dn, group_search_custom_filter=group_search_custom_filter, group_search_type=group_search_type, search_bind_dn=search_bind_dn, search_bind_password=search_bind_password, user_dntemplate=user_dntemplate, user_search_base_dn=user_search_base_dn, user_search_filter=user_search_filter)
    cli_utils.print_result(EnableLdapAuthenticationResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetLdapConfiguration', short_help="""The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster. """)
@pass_context
def GetLdapConfiguration(ctx):
    """The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetLdapConfigurationResult = ctx.element.get_ldap_configuration()
    cli_utils.print_result(GetLdapConfigurationResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('TestLdapAuthentication', short_help="""The TestLdapAuthentication is used to verify the currently enabled LDAP authentication configuration settings are correct. If the configuration settings are correct, the API call returns a list of the groups the tested user is a member of. """)
@click.option('--username',
              type=str,
              required=True,
              help="""The username to be tested. """)
@click.option('--password',
              type=str,
              required=True,
              help="""The password for the username to be tester. """)
@click.option('--ldap_configuration_auth_type',
              type=str,
              required=True,
              help="""Identifies which user authentcation method will be used. <br/> Valid values:<br/> <b>DirectBind</b><br/> <b>SearchAndBind</b> """)
@click.option('--ldap_configuration_enabled',
              type=bool,
              required=True,
              help="""Identifies whether or not the system is enabled for LDAP. <br/> Valid values:<br/> <b>true</b><br/> <b>false</b> """)
@click.option('--ldap_configuration_group_search_base_dn',
              type=str,
              required=True,
              help="""The base DN of the tree to start the group search (will do a subtree search from here). """)
@click.option('--ldap_configuration_group_search_custom_filter',
              type=str,
              required=True,
              help="""The custom search filter used. """)
@click.option('--ldap_configuration_group_search_type',
              type=str,
              required=True,
              help="""Controls the default group search filter used, can be one of the following:<br/> <b>NoGroups</b>: No group support.<br/> <b>ActiveDirectory</b>: Nested membership of all of a user's AD groups.<br/> <b>MemberDN</b>: MemberDN style groups (single-level). """)
@click.option('--ldap_configuration_search_bind_dn',
              type=str,
              required=True,
              help="""A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). """)
@click.option('--ldap_configuration_server_uris',
              type=str,
              required=True,
              help="""A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") """)
@click.option('--ldap_configuration_user_dntemplate',
              type=str,
              required=True,
              help="""A string that is used to form a fully qualified user DN. """)
@click.option('--ldap_configuration_user_search_base_dn',
              type=str,
              required=True,
              help="""The base DN of the tree used to start the search (will do a subtree search from here). """)
@click.option('--ldap_configuration_user_search_filter',
              type=str,
              required=True,
              help="""The LDAP filter used. """)
@pass_context
def TestLdapAuthentication(ctx,
           username,
           password,
           ldap_configuration_auth_type = None,
           ldap_configuration_enabled = None,
           ldap_configuration_group_search_base_dn = None,
           ldap_configuration_group_search_custom_filter = None,
           ldap_configuration_group_search_type = None,
           ldap_configuration_search_bind_dn = None,
           ldap_configuration_server_uris = None,
           ldap_configuration_user_dntemplate = None,
           ldap_configuration_user_search_base_dn = None,
           ldap_configuration_user_search_filter = None):
    """The TestLdapAuthentication is used to verify the currently enabled LDAP authentication configuration settings are correct. If the configuration settings are correct, the API call returns a list of the groups the tested user is a member of."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ldap_configuration = None
    if(username is not None or password is not None or ldap_configuration is not None or False):
        kwargsDict = dict()
        kwargsDict["auth_type"] = ldap_configuration_auth_type
        kwargsDict["enabled"] = ldap_configuration_enabled
        kwargsDict["group_search_base_dn"] = ldap_configuration_group_search_base_dn
        kwargsDict["group_search_custom_filter"] = ldap_configuration_group_search_custom_filter
        kwargsDict["group_search_type"] = ldap_configuration_group_search_type
        kwargsDict["search_bind_dn"] = ldap_configuration_search_bind_dn
        kwargsDict["server_uris"] = ldap_configuration_server_uris
        kwargsDict["user_dntemplate"] = ldap_configuration_user_dntemplate
        kwargsDict["user_search_base_dn"] = ldap_configuration_user_search_base_dn
        kwargsDict["user_search_filter"] = ldap_configuration_user_search_filter

        ldap_configuration = LdapConfiguration(**kwargsDict)

    TestLdapAuthenticationResult = ctx.element.test_ldap_authentication(username=username, password=password, ldap_configuration=ldap_configuration)
    cli_utils.print_result(TestLdapAuthenticationResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

