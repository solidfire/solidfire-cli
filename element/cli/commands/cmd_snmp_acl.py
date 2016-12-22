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

@cli.command('set', short_help="SetSnmpACL")
@click.option('--networks',
              type=SnmpNetwork,
              required=True,
              help="List of networks and what type of access they have to the SNMP servers running on the cluster nodes. See SNMP Network Object for possible "networks" values. REQUIRED if SNMP v# is disabled. ")
@click.option('--usm_users',
              type=SnmpV3UsmUser,
              required=True,
              help="List of users and the type of access they have to the SNMP servers running on the cluster nodes. REQUIRED if SNMP v3 is enabled. ")
@pass_context
def set(ctx, networks, usm_users):
    """SetSnmpACL is used to configure SNMP access permissions on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpACL. Also note that the values set with this interface replace all &quot;network&quot; or &quot;usmUsers&quot; values set with the older SetSnmpInfo."""
    SetSnmpACLResult = ctx.element.set_snmp_acl(networks=networks, usm_users=usm_users)
    cli_utils.print_result(SetSnmpACLResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

