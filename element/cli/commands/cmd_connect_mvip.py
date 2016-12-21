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

@cli.command('test', short_help="TestConnectMvip")
@click.option('--mvip',
              type=str,
              required=False,
              help="Optionally, use to test the management connection of a different MVIP. This is not needed to test the connection to the target cluster. ")
@pass_context
def test(ctx, mvip = None):
    """The TestConnectMvip API method is used to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity."""
    """&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    TestConnectMvipResult = ctx.element.test_connect_mvip(mvip=mvip)
    print(json.dumps(json.loads(jsonpickle.encode(TestConnectMvipResult)),indent=4))

