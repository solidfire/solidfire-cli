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


@click.group()
@pass_context
def cli(ctx):
    """disableldapauthentication getldapconfiguration enableldapauthentication testldapauthentication addldapclusteradmin """

@cli.command('disableldapauthentication', short_help="""The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in. """)
@pass_context
def disableldapauthentication(ctx):
    """The DisableLdapAuthentication method is used disable LDAP authentication and remove all LDAP configuration settings. This call will not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _DisableLdapAuthenticationResult = ctx.element.disable_ldap_authentication()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DisableLdapAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getldapconfiguration', short_help="""The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster. """)
@pass_context
def getldapconfiguration(ctx):
    """The GetLdapConfiguration is used to get the LDAP configuration currently active on the cluster."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetLdapConfigurationResult = ctx.element.get_ldap_configuration()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetLdapConfigurationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enableldapauthentication', short_help="""The EnableLdapAuthentication method is used to configure an LDAP server connection to use for LDAP authentication to a SolidFire cluster. Users that are members on the LDAP server can then log in to a SolidFire storage system using their LDAP authentication userid and password. """)
@click.option('--authtype',
              type=str,
              required=False,
              help="""Identifies which user authentcation method will be used.  Must be one of the following: DirectBind SearchAndBind (default) """)
@click.option('--groupsearchbasedn',
              type=str,
              required=False,
              help="""The base DN of the tree to start the group search (will do a subtree search from here). """)
@click.option('--groupsearchcustomfilter',
              type=str,
              required=False,
              help="""REQUIRED for CustomFilter For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a user's groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. """)
@click.option('--groupsearchtype',
              type=str,
              required=False,
              help="""Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: (default) Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). """)
@click.option('--searchbinddn',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). """)
@click.option('--searchbindpassword',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind The password for the searchBindDN account used for searching. """)
@click.option('--serveruris',
              type=str,
              required=True,
              help="""A list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") """)
@click.option('--userdntemplate',
              type=str,
              required=False,
              help="""REQUIRED for DirectBind A string that is used to form a fully qualified user DN. The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user. """)
@click.option('--usersearchbasedn',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind The base DN of the tree used to start the search (will do a subtree search from here). """)
@click.option('--usersearchfilter',
              type=str,
              required=False,
              help="""REQUIRED for SearchAndBind. The LDAP filter to use. The string should have the placeholder text "%USERNAME%" which will be replaced with the username of the authenticating user. Example: (&(objectClass=person) (sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the nusername entered at cluster login. """)
@pass_context
def enableldapauthentication(ctx,
           serveruris,
           authtype = None,
           groupsearchbasedn = None,
           groupsearchcustomfilter = None,
           groupsearchtype = None,
           searchbinddn = None,
           searchbindpassword = None,
           userdntemplate = None,
           usersearchbasedn = None,
           usersearchfilter = None):
    """The EnableLdapAuthentication method is used to configure an LDAP server connection to use for LDAP authentication to a SolidFire cluster. Users that are members on the LDAP server can then log in to a SolidFire storage system using their LDAP authentication userid and password."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    serveruris = parser.parse_array(serveruris)
    

    ctx.logger.info("""authtype = """+str(authtype)+""";"""+"""groupsearchbasedn = """+str(groupsearchbasedn)+""";"""+"""groupsearchcustomfilter = """+str(groupsearchcustomfilter)+""";"""+"""groupsearchtype = """+str(groupsearchtype)+""";"""+"""searchbinddn = """+str(searchbinddn)+""";"""+"""searchbindpassword = """+str(searchbindpassword)+""";"""+"""serveruris = """+str(serveruris)+""";"""+"""userdntemplate = """+str(userdntemplate)+""";"""+"""usersearchbasedn = """+str(usersearchbasedn)+""";"""+"""usersearchfilter = """+str(usersearchfilter)+""";"""+"")
    try:
        _EnableLdapAuthenticationResult = ctx.element.enable_ldap_authentication(server_uris=serveruris, auth_type=authtype, group_search_base_dn=groupsearchbasedn, group_search_custom_filter=groupsearchcustomfilter, group_search_type=groupsearchtype, search_bind_dn=searchbinddn, search_bind_password=searchbindpassword, user_dntemplate=userdntemplate, user_search_base_dn=usersearchbasedn, user_search_filter=usersearchfilter)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_EnableLdapAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('testldapauthentication', short_help="""The TestLdapAuthentication is used to verify the currently enabled LDAP authentication configuration settings are correct. If the configuration settings are correct, the API call returns a list of the groups the tested user is a member of. """)
@click.option('--username',
              type=str,
              required=True,
              help="""The username to be tested. """)
@click.option('--password',
              type=str,
              required=True,
              help="""The password for the username to be tester. """)
@click.option('--ldapconfigurationauthtype',
              type=str,
              required=True,
              help="""Identifies which user authentcation method will be used.  Valid values: DirectBind SearchAndBind """)
@click.option('--ldapconfigurationenabled',
              type=bool,
              required=True,
              help="""Identifies whether or not the system is enabled for LDAP.  Valid values: true false """)
@click.option('--ldapconfigurationgroupsearchbasedn',
              type=str,
              required=True,
              help="""The base DN of the tree to start the group search (will do a subtree search from here). """)
@click.option('--ldapconfigurationgroupsearchcustomfilter',
              type=str,
              required=True,
              help="""The custom search filter used. """)
@click.option('--ldapconfigurationgroupsearchtype',
              type=str,
              required=True,
              help="""Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). """)
@click.option('--ldapconfigurationsearchbinddn',
              type=str,
              required=True,
              help="""A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). """)
@click.option('--ldapconfigurationserveruris',
              type=str,
              required=True,
              help="""A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") """)
@click.option('--ldapconfigurationuserdntemplate',
              type=str,
              required=True,
              help="""A string that is used to form a fully qualified user DN. """)
@click.option('--ldapconfigurationusersearchbasedn',
              type=str,
              required=True,
              help="""The base DN of the tree used to start the search (will do a subtree search from here). """)
@click.option('--ldapconfigurationusersearchfilter',
              type=str,
              required=True,
              help="""The LDAP filter used. """)
@pass_context
def testldapauthentication(ctx,
           username,
           password,
           ldapconfigurationauthtype = None,
           ldapconfigurationenabled = None,
           ldapconfigurationgroupsearchbasedn = None,
           ldapconfigurationgroupsearchcustomfilter = None,
           ldapconfigurationgroupsearchtype = None,
           ldapconfigurationsearchbinddn = None,
           ldapconfigurationserveruris = None,
           ldapconfigurationuserdntemplate = None,
           ldapconfigurationusersearchbasedn = None,
           ldapconfigurationusersearchfilter = None):
    """The TestLdapAuthentication is used to verify the currently enabled LDAP authentication configuration settings are correct. If the configuration settings are correct, the API call returns a list of the groups the tested user is a member of."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ldapconfiguration = None
    if(username is not None or password is not None or ldapconfiguration is not None or False):
        kwargsDict = dict()
        kwargsDict["auth_type"] = ldapconfigurationauthtype
        kwargsDict["enabled"] = ldapconfigurationenabled
        kwargsDict["group_search_base_dn"] = ldapconfigurationgroupsearchbasedn
        kwargsDict["group_search_custom_filter"] = ldapconfigurationgroupsearchcustomfilter
        kwargsDict["group_search_type"] = ldapconfigurationgroupsearchtype
        kwargsDict["search_bind_dn"] = ldapconfigurationsearchbinddn
        kwargsDict["server_uris"] = ldapconfigurationserveruris
        kwargsDict["user_dntemplate"] = ldapconfigurationuserdntemplate
        kwargsDict["user_search_base_dn"] = ldapconfigurationusersearchbasedn
        kwargsDict["user_search_filter"] = ldapconfigurationusersearchfilter

        ldapconfiguration = LdapConfiguration(**kwargsDict)
    

    ctx.logger.info("""username = """+str(username)+""";"""+"""password = """+str(password)+""";"""+"""ldapconfiguration = """+str(ldapconfiguration)+""";"""+"")
    try:
        _TestLdapAuthenticationResult = ctx.element.test_ldap_authentication(username=username, password=password, ldap_configuration=ldapconfiguration)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_TestLdapAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('addldapclusteradmin', short_help="""AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts.  An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group. """)
@click.option('--username',
              type=str,
              required=True,
              help="""The distinguished user name for the new LDAP cluster admin. """)
@click.option('--access',
              type=str,
              required=True,
              help="""Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. """)
@click.option('--accepteula',
              type=bool,
              required=False,
              help="""Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def addldapclusteradmin(ctx,
           username,
           access,
           accepteula = None,
           attributes = None):
    """AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts."""
    """"""
    """An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    access = parser.parse_array(access)
    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
        attributes = dict(**kwargsDict)
    

    ctx.logger.info("""username = """+str(username)+""";"""+"""access = """+str(access)+""";"""+"""accepteula = """+str(accepteula)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _AddLdapClusterAdminResult = ctx.element.add_ldap_cluster_admin(username=username, access=access, accept_eula=accepteula, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_AddLdapClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

