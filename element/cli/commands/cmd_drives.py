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

@cli.command('test', short_help="TestDrives")
@click.option('--minutes',
              type=int,
              required=False,
              help="The number of minutes to run the test can be specified. ")
@pass_context
def test(ctx, minutes = None):
    """The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This test takes approximately 10 minutes."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    TestDrivesResult = ctx.element.test_drives(minutes=minutes)
    cli_utils.print_result(TestDrivesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

