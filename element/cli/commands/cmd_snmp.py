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

@cli.command('enable', short_help="EnableSnmp")
@click.argument('snmp_v3_enabled', type=bool, required=True)
@pass_context
def enable(ctx, snmp_v3_enabled):
    """EnableSnmp is used to enable SNMP on the cluster nodes. The values set with this interface apply to all nodes in the cluster, and the values that are passed replace, in whole, all values set in any previous call to EnableSnmp."""
    EnableSnmpResult = ctx.element.enable_snmp(snmp_v3_enabled=snmp_v3_enabled)
    print(json.dumps(json.loads(jsonpickle.encode(EnableSnmpResult)),indent=4))

