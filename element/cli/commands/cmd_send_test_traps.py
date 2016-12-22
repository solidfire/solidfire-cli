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

@cli.command('snmp', short_help="SnmpSendTestTraps")
@pass_context
def snmp(ctx):
    """SnmpSendTestTraps enables you to test SNMP functionality for a cluster. This method instructs the cluster to send test SNMP traps to the currently configured SNMP manager."""
    SnmpSendTestTrapsResult = ctx.element.snmp_send_test_traps()
    cli_utils.print_result(SnmpSendTestTrapsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

