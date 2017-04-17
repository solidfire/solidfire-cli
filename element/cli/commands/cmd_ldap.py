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
    """disableauthentication addclusteradmin testauthentication enableauthentication getconfiguration """

@cli.command('disableauthentication', short_help="""The DisableLdapAuthentication method enables you to disable LDAP authentication and remove all LDAP configuration settings. This method does not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in. """, cls=SolidFireCommand)
@pass_context
def disableauthentication(ctx):
    """The DisableLdapAuthentication method enables you to disable LDAP authentication and remove all LDAP configuration settings. This method does not remove any configured cluster admin accounts (user or group). However, those cluster admin accounts will no longer be able to log in."""

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info("")
    try:
        _DisableLdapAuthenticationResult = ctx.element.disable_ldap_authentication()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DisableLdapAuthenticationResult), indent=4))
        return
    else:
        cli_utils.print_result(_DisableLdapAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('addclusteradmin', short_help="""AddLdapClusterAdmin enables you to add a new LDAP cluster administrator user. An LDAP cluster administrator can manage the cluster via the API and management tools. LDAP cluster admin accounts are completely separate and unrelated to standard tenant accounts. You can also use this method to add an LDAP group that has been defined in Active Directory. The access level that is given to the group is passed to the individual users in the LDAP group. """, cls=SolidFireCommand)
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
              help="""Accept the End User License Agreement. Set to true to add a cluster administrator account to the system. If omitted or set to false, the method call fails. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def addclusteradmin(ctx,
           # Mandatory main parameter
           username,
           # Mandatory main parameter
           access,
           # Optional main parameter
           accepteula = None,
           # Optional main parameter
           attributes = None):
    """AddLdapClusterAdmin enables you to add a new LDAP cluster administrator user. An LDAP cluster administrator can manage the"""
    """cluster via the API and management tools. LDAP cluster admin accounts are completely separate and unrelated to standard tenant"""
    """accounts."""
    """You can also use this method to add an LDAP group that has been defined in Active Directory. The access level that is given to the group is passed to the individual users in the LDAP group."""

    cli_utils.establish_connection(ctx)
    
    

    access = parser.parse_array(access)
    
    

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""username = """+str(username)+""";"""+"""access = """+str(access)+""";"""+"""accepteula = """+str(accepteula)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _AddLdapClusterAdminResult = ctx.element.add_ldap_cluster_admin(username=username, access=access, accept_eula=accepteula, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AddLdapClusterAdminResult), indent=4))
        return
    else:
        cli_utils.print_result(_AddLdapClusterAdminResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('testauthentication', short_help="""The TestLdapAuthentication method enables you to validate the currently enabled LDAP authentication settings. If the configuration is correct, the API call returns the group membership of the tested user. """, cls=SolidFireCommand)
@click.option('--username',
              type=str,
              required=True,
              help="""The username to be tested. """)
@click.option('--password',
              type=str,
              required=True,
              help="""The password for the username to be tested. """)

@click.option('--ldapconfigurationauthtype',
              type=str,
              required=False,
              help="""Identifies which user authentcation method will be used.  Valid values: DirectBind SearchAndBind """)

@click.option('--ldapconfigurationenabled',
              type=bool,
              required=False,
              help="""Identifies whether or not the system is enabled for LDAP.  Valid values: true false """)

@click.option('--ldapconfigurationgroupsearchbasedn',
              type=str,
              required=False,
              help="""The base DN of the tree to start the group search (will do a subtree search from here). """)

@click.option('--ldapconfigurationgroupsearchcustomfilter',
              type=str,
              required=False,
              help="""The custom search filter used. """)

@click.option('--ldapconfigurationgroupsearchtype',
              type=str,
              required=False,
              help="""Controls the default group search filter used, can be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a user's AD groups. MemberDN: MemberDN style groups (single-level). """)

@click.option('--ldapconfigurationsearchbinddn',
              type=str,
              required=False,
              help="""A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). """)

@click.option('--ldapconfigurationserveruris',
              type=str,
              required=False,
              help="""A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") """)

@click.option('--ldapconfigurationuserdntemplate',
              type=str,
              required=False,
              help="""A string that is used to form a fully qualified user DN. """)

@click.option('--ldapconfigurationusersearchbasedn',
              type=str,
              required=False,
              help="""The base DN of the tree used to start the search (will do a subtree search from here). """)

@click.option('--ldapconfigurationusersearchfilter',
              type=str,
              required=False,
              help="""The LDAP filter used. """)
@pass_context
def testauthentication(ctx,
           # Mandatory main parameter
           username,
           # Mandatory main parameter
           password,
           # Optional subparameter of optional main parameter.
           ldapconfigurationauthtype = None,
           # Optional subparameter of optional main parameter.
           ldapconfigurationenabled = None,
           # Optional subparameter of optional main parameter.
           ldapconfigurationgroupsearchbasedn = None,
           # Optional subparameter of optional main parameter.
           ldapconfigurationgroupsearchcustomfilter = None,
           # Optional subparameter of optional main parameter.
           ldapconfigurationgroupsearchtype = None,
           # Optional subparameter of optional main parameter.
           ldapconfigurationsearchbinddn = None,
           # Optional subparameter of optional main parameter.
           ldapconfigurationserveruris = None,
           # Optional subparameter of optional main parameter.
           ldapconfigurationuserdntemplate = None,
           # Optional subparameter of optional main parameter.
           ldapconfigurationusersearchbasedn = None,
           # Optional subparameter of optional main parameter.
           ldapconfigurationusersearchfilter = None):
    """The TestLdapAuthentication method enables you to validate the currently enabled LDAP authentication settings. If the configuration is"""
    """correct, the API call returns the group membership of the tested user."""

    cli_utils.establish_connection(ctx)
    
    
    

    ldapconfiguration = None
    if(ldapconfigurationauthtype is not None or
       ldapconfigurationenabled is not None or
       ldapconfigurationgroupsearchbasedn is not None or
       ldapconfigurationgroupsearchcustomfilter is not None or
       ldapconfigurationgroupsearchtype is not None or
       ldapconfigurationsearchbinddn is not None or
       ldapconfigurationserveruris is not None or
       ldapconfigurationuserdntemplate is not None or
       ldapconfigurationusersearchbasedn is not None or
       ldapconfigurationusersearchfilter is not None or
       False):
        if not (ldapconfiguration and ldapconfiguration and ldapconfiguration and ldapconfiguration and ldapconfiguration and ldapconfiguration and ldapconfiguration and ldapconfiguration and ldapconfiguration and ldapconfiguration and  True):
            ctx.logger.error("""If you choose to provide ldapconfiguration, you must include all of the following parameters:
ldapconfigurationauthtype
ldapconfigurationenabled
ldapconfigurationgroupsearchbasedn
ldapconfigurationgroupsearchcustomfilter
ldapconfigurationgroupsearchtype
ldapconfigurationsearchbinddn
ldapconfigurationserveruris
ldapconfigurationuserdntemplate
ldapconfigurationusersearchbasedn
ldapconfigurationusersearchfilter
""")
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
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestLdapAuthenticationResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestLdapAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enableauthentication', short_help="""The EnableLdapAuthentication method enables you to configure an LDAP directory connection to use for LDAP authentication to a cluster. Users that are members of the LDAP directory can then log in to the storage system using their LDAP credentials. """, cls=SolidFireCommand)
@click.option('--authtype',
              type=str,
              required=False,
              help="""Identifies which user authentication method to use. Must be one of the following: DirectBind SearchAndBind """)
@click.option('--groupsearchbasedn',
              type=str,
              required=False,
              help="""The base DN of the tree to start the group search (will do a subtree search from here). """)
@click.option('--groupsearchcustomfilter',
              type=str,
              required=False,
              help="""For use with the CustomFilter search type, an LDAP filter to use to return the DNs of a users groups. The string can have placeholder text of %USERNAME% and %USERDN% to be replaced with their username and full userDN as needed. """)
@click.option('--groupsearchtype',
              type=str,
              required=False,
              help="""Controls the default group search filter used, and must be one of the following: NoGroups: No group support. ActiveDirectory: Nested membership of all of a users AD groups. MemberDN: MemberDN style groups (single level). """)
@click.option('--searchbinddn',
              type=str,
              required=False,
              help="""A fully qualified DN to log in with to perform an LDAP search for the user (needs read access to the LDAP directory). """)
@click.option('--searchbindpassword',
              type=str,
              required=False,
              help="""The password for the searchBindDN account used for searching. """)
@click.option('--serveruris',
              type=str,
              required=True,
              help="""A comma-separated list of LDAP server URIs (examples: "ldap://1.2.3.4" and ldaps://1.2.3.4:123") """)
@click.option('--userdntemplate',
              type=str,
              required=False,
              help="""A string that is used to form a fully qualified user DN. The string should have the placeholder text %USERNAME%, which is replaced with the username of the authenticating user. """)
@click.option('--usersearchbasedn',
              type=str,
              required=False,
              help="""The base DN of the tree to start the search (will do a subtree search from here). """)
@click.option('--usersearchfilter',
              type=str,
              required=False,
              help="""The LDAP filter to use. The string should have the placeholder text %USERNAME% which is replaced with the username of the authenticating user. Example: (&(objectClass=person)(sAMAccountName=%USERNAME%)) will use the sAMAccountName field in Active Directory to match the username entered at cluster login. """)
@pass_context
def enableauthentication(ctx,
           # Mandatory main parameter
           serveruris,
           # Optional main parameter
           authtype = None,
           # Optional main parameter
           groupsearchbasedn = None,
           # Optional main parameter
           groupsearchcustomfilter = None,
           # Optional main parameter
           groupsearchtype = None,
           # Optional main parameter
           searchbinddn = None,
           # Optional main parameter
           searchbindpassword = None,
           # Optional main parameter
           userdntemplate = None,
           # Optional main parameter
           usersearchbasedn = None,
           # Optional main parameter
           usersearchfilter = None):
    """The EnableLdapAuthentication method enables you to configure an LDAP directory connection to use for LDAP authentication to a cluster. Users that are members of the LDAP directory can then log in to the storage system using their LDAP credentials."""

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    
    

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
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_EnableLdapAuthenticationResult), indent=4))
        return
    else:
        cli_utils.print_result(_EnableLdapAuthenticationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getconfiguration', short_help="""The GetLdapConfiguration method enables you to get the currently active LDAP configuration on the cluster. """, cls=SolidFireCommand)
@pass_context
def getconfiguration(ctx):
    """The GetLdapConfiguration method enables you to get the currently active LDAP configuration on the cluster."""

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info("")
    try:
        _GetLdapConfigurationResult = ctx.element.get_ldap_configuration()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetLdapConfigurationResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetLdapConfigurationResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

