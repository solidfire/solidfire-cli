#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import json

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('add', short_help="AddLdapClusterAdmin")
@click.option('--username',
              type=str,
              required=True,
              help="The distinguished user name for the new LDAP cluster admin. ")
@click.option('--access',
              type=str,
              required=True,
              help="Controls which methods this Cluster Admin can use. For more details on the levels of access, see the Access Control appendix in the SolidFire API Reference. ")
@click.option('--accept_eula',
              type=bool,
              required=False,
              help="Indicate your acceptance of the End User License Agreement when creating this cluster admin. To accept the EULA, set this parameter to true. ")
@click.option('--attributes',
              type=dict,
              required=False,
              help="List of Name/Value pairs in JSON object format. ")
@pass_context
def add(ctx, username, access, accept_eula = None, attributes = None):
    """AddLdapClusterAdmin is used to add a new LDAP Cluster Admin. An LDAP Cluster Admin can be used to manage the cluster via the API and management tools. LDAP Cluster Admins are completely separate and unrelated to standard tenant accounts."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """An LDAP group that has been defined in Active Directory can also be added using this API method. The access level that is given to the group will be passed to the individual users in the LDAP group."""
    AddLdapClusterAdminResult = ctx.element.add_ldap_cluster_admin(username=username, access=access, accept_eula=accept_eula, attributes=attributes)
    cli_utils.print_result(AddLdapClusterAdminResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

