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

@cli.command('test', short_help="TestPing")
@click.argument('attempts', type=int, required=False)
@click.argument('hosts', type=str, required=False)
@click.argument('total_timeout_sec', type=int, required=False)
@click.argument('packet_size', type=int, required=False)
@click.argument('ping_timeout_msec', type=int, required=False)
@pass_context
def test(ctx, attempts = None, hosts = None, total_timeout_sec = None, packet_size = None, ping_timeout_msec = None):
    """The TestPing API method is used to validate the connection to all nodes in the cluster on both 1G and 10G interfaces using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration."""
    """&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    TestPingResult = ctx.element.test_ping(attempts=attempts, hosts=hosts, total_timeout_sec=total_timeout_sec, packet_size=packet_size, ping_timeout_msec=ping_timeout_msec)
    print(TestPingResult)

