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
from uuid import UUID
from element import exceptions
from solidfire import common


@click.group()
@pass_context
def cli(ctx):
<<<<<<< HEAD
    """AddLdapClusterAdmin DisableLdapAuthentication TestLdapAuthentication EnableLdapAuthentication GetLdapConfiguration """
=======
    """GetLdapConfiguration AddLdapClusterAdmin EnableLdapAuthentication DisableLdapAuthentication TestLdapAuthentication """
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.

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
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    access = parser.parse_array(access)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""username = """+str(username)+""";"""+"""access = """+str(access)+""";"""+"""accept_eula = """+str(accept_eula)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        AddLdapClusterAdminResult = ctx.element.add_ldap_cluster_admin(username=username, access=access, accept_eula=accept_eula, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(AddLdapClusterAdminResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('DisableLdapAuthentication', short_help="""The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in. """)
@pass_context
def DisableLdapAuthentication(ctx):
    """The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        DisableLdapAuthenticationResult = ctx.element.disable_ldap_authentication()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(DisableLdapAuthenticationResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



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
              help="""Identifies which user authentcation method will be used.  Valid values: DirectBind SearchAndBind """)
@click.option('--ldap_configuration_enabled',
              type=bool,
              required=True,
              help="""Identifies whether or not the system is enabled for LDAP.  Valid values: true false """)
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
              help="""Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). """)
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
=======
    cli_utils.print_result(GetLdapConfigurationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



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
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
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

    ctx.logger.info("""username = """+str(username)+""";"""+"""password = """+str(password)+""";"""+"""ldap_configuration = """+str(ldap_configuration)+""";"""+"")
    try:
        TestLdapAuthenticationResult = ctx.element.test_ldap_authentication(username=username, password=password, ldap_configuration=ldap_configuration)
=======
    access = parser.parse_array(access)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""username = """+str(username)+""";"""+"""access = """+str(access)+""";"""+"""accept_eula = """+str(accept_eula)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        AddLdapClusterAdminResult = ctx.element.add_ldap_cluster_admin(username=username, access=access, accept_eula=accept_eula, attributes=attributes)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(TestLdapAuthenticationResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(AddLdapClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.



@cli.command('EnableLdapAuthentication', short_help="""The EnableLdapAuthentication method is used to configure an LDAP server connection to use for LDAP authentication to a SolidFire cluster. Users that are members on the LDAP server can then log in to a SolidFire storage system using their LDAP authentication userid and password. """)
@click.option('--auth_type',
              type=str,
              required=False,
              help="""Identifies which user authentcation method will be used.  Must be one of the following: DirectBind SearchAndBind (default) """)
@click.option('--group_search_base_dn',
              type=str,
              required=False,
              help="""The base DN of the tree to start the group search (will do a subtree search from here). """)
@click.option('--group_search_custom_filter',
              type=str,
              required=False,
              help="""REQUIRED for CustomFilter For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user's groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. """)
@click.option('--group_search_type',
              type=str,
              required=False,
              help="""Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: (default) Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). """)
@click.option('--search_bind_dn',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). """)
@click.option('--search_bind_password',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind The password for the searchBindDN account used for searching. """)
@click.option('--server_uris',
              type=str,
              required=True,
              help="""A list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") """)
@click.option('--user_dntemplate',
              type=str,
              required=False,
              help="""REQUIRED for DirectBind A string that is used to form a fully qualified user DN. The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user. """)
@click.option('--user_search_base_dn',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind The base DN of the tree used to start the search (will do a subtree search from here). """)
@click.option('--user_search_filter',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind. The LDAP filter to use. The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user. Example: (&(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login. """)
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
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    server_uris = parser.parse_array(server_uris)

    ctx.logger.info("""auth_type = """+str(auth_type)+""";"""+"""group_search_base_dn = """+str(group_search_base_dn)+""";"""+"""group_search_custom_filter = """+str(group_search_custom_filter)+""";"""+"""group_search_type = """+str(group_search_type)+""";"""+"""search_bind_dn = """+str(search_bind_dn)+""";"""+"""search_bind_password = """+str(search_bind_password)+""";"""+"""server_uris = """+str(server_uris)+""";"""+"""user_dntemplate = """+str(user_dntemplate)+""";"""+"""user_search_base_dn = """+str(user_search_base_dn)+""";"""+"""user_search_filter = """+str(user_search_filter)+""";"""+"")
    try:
        EnableLdapAuthenticationResult = ctx.element.enable_ldap_authentication(server_uris=server_uris, auth_type=auth_type, group_search_base_dn=group_search_base_dn, group_search_custom_filter=group_search_custom_filter, group_search_type=group_search_type, search_bind_dn=search_bind_dn, search_bind_password=search_bind_password, user_dntemplate=user_dntemplate, user_search_base_dn=user_search_base_dn, user_search_filter=user_search_filter)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(EnableLdapAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('DisableLdapAuthentication', short_help="""The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in. """)
@pass_context
def DisableLdapAuthentication(ctx):
    """The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        DisableLdapAuthenticationResult = ctx.element.disable_ldap_authentication()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(DisableLdapAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



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
              help="""Identifies which user authentcation method will be used.  Valid values: DirectBind SearchAndBind """)
@click.option('--ldap_configuration_enabled',
              type=bool,
              required=True,
              help="""Identifies whether or not the system is enabled for LDAP.  Valid values: true false """)
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
              help="""Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). """)
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
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



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

    ctx.logger.info("""username = """+str(username)+""";"""+"""password = """+str(password)+""";"""+"""ldap_configuration = """+str(ldap_configuration)+""";"""+"")
    try:
        TestLdapAuthenticationResult = ctx.element.test_ldap_authentication(username=username, password=password, ldap_configuration=ldap_configuration)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(TestLdapAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetLdapConfiguration', short_help="""The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster. """)
@pass_context
def GetLdapConfiguration(ctx):
    """The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        GetLdapConfigurationResult = ctx.element.get_ldap_configuration()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetLdapConfigurationResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

