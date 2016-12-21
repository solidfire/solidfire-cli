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

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('set', short_help="SetSnmpInfo")
@click.argument('networks', type=SnmpNetwork, required=False)
@click.argument('enabled', type=bool, required=False)
@click.argument('snmp_v3_enabled', type=bool, required=False)
@click.argument('usm_users', type=SnmpV3UsmUser, required=False)
@pass_context
def set(ctx, networks = None, enabled = None, snmp_v3_enabled = None, usm_users = None):
    """SetSnmpInfo is used to configure SNMP v2 and v3 on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to SetSnmpInfo."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: EnableSnmp and SetSnmpACL methods can be used to accomplish the same results as SetSnmpInfo. SetSnmpInfo will no longer be available after the Element 8 release. Please use EnableSnmp and SetSnmpACL in the future."""
    SetSnmpInfoResult = ctx.element.set_snmp_info(networks=networks, enabled=enabled, snmp_v3_enabled=snmp_v3_enabled, usm_users=usm_users)
    print(SetSnmpInfoResult)

