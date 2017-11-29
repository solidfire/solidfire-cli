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
    """getcurrent modify remove list add setloginbanner getloginbanner """

@cli.command('getcurrent', short_help="""GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was created when the cluster was created. """, cls=SolidFireCommand)
@pass_context
def getcurrent(ctx):
    """GetCurrentClusterAdmin returns information for the current primary cluster administrator. The primary Cluster Admin was created when the cluster was created."""

    

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



@cli.command('modify', short_help="""You can use ModifyClusterAdmin to change the settings for a cluster admin or LDAP cluster admin. You cannot change access for the administrator cluster admin account. """, cls=SolidFireCommand)
@click.option('--clusteradminid',
              type=int,
              required=True,
              prompt=True,
              help="""ClusterAdminID for the cluster admin or LDAP cluster admin to modify. """)
@click.option('--password',
              type=str,
              required=False,
              help="""Password used to authenticate this cluster admin. """)
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
    """You can use ModifyClusterAdmin to change the settings for a cluster admin or LDAP cluster admin. You cannot change access for the administrator cluster admin account."""

    

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



@cli.command('remove', short_help="""You can use RemoveClusterAdmin to remove a Cluster Admin. You cannot remove the administrator cluster admin account. """, cls=SolidFireCommand)
@click.option('--clusteradminid',
              type=int,
              required=True,
              prompt=True,
              help="""ClusterAdminID for the cluster admin to remove. """)
@pass_context
def remove(ctx,
           # Mandatory main parameter
           clusteradminid):
    """You can use RemoveClusterAdmin to remove a Cluster Admin. You cannot remove the administrator cluster admin account."""

    

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



@cli.command('list', short_help="""ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrator accounts with different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. You can also create LDAP administrators when setting up an LDAP system on the cluster. """, cls=SolidFireCommand)
@pass_context
def list(ctx):
    """ListClusterAdmins returns the list of all cluster administrators for the cluster. There can be several cluster administrator accounts with different levels of permissions. There can be only one primary cluster administrator in the system. The primary Cluster Admin is the administrator that was created when the cluster was created. You can also create LDAP administrators when setting up an LDAP system on the cluster."""

    

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
              required=False,
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
           # Optional main parameter
           accepteula = None,
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
    

    ctx.logger.info(""": """"""username = """ + str(username)+";"+"""password = """ + str(password)+";"+"""access = """ + str(access)+";" + """accepteula = """+str(accepteula)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
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

