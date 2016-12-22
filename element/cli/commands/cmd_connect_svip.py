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

@cli.command('test', short_help="TestConnectSvip")
@click.option('--svip',
              type=str,
              required=False,
              help="Optionally, use to test the storage connection of a different SVIP. This is not needed to test the connection to the target cluster. ")
@pass_context
def test(ctx, svip = None):
    """The TestConnectSvip API method is used to test the storage connection to the cluster. The test pings the SVIP using ICMP packets and when successful connects as an iSCSI initiator."""
    """&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    TestConnectSvipResult = ctx.element.test_connect_svip(svip=svip)
    cli_utils.print_result(TestConnectSvipResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

