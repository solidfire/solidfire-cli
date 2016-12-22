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

@cli.command('get', short_help="GetSnmpState")
@pass_context
def get(ctx):
    """GetSnmpState is used to return the current state of the SNMP feature."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: GetSnmpState is new for Element OS 8. Please use this method and SetSnmpACL to migrate your SNMP functionality in the future."""
    GetSnmpStateResult = ctx.element.get_snmp_state()
    cli_utils.print_result(GetSnmpStateResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

