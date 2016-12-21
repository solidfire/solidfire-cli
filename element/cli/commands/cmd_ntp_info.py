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

@cli.command('set', short_help="SetNtpInfo")
@click.argument('servers', type=str, required=True)
@click.argument('broadcastclient', type=bool, required=False)
@pass_context
def set(ctx, servers, broadcastclient = None):
    """SetNtpInfo is used to configure the NTP on cluster nodes. The values set with this interface apply to all nodes in the cluster. The nodes can only be configured as a server where a host is selected to administrate the networking and/or a broadcast client where each host sends each message to each peer."""
    SetNtpInfoResult = ctx.element.set_ntp_info(servers=servers, broadcastclient=broadcastclient)
    print(json.dumps(json.loads(jsonpickle.encode(SetNtpInfoResult)),indent=4))

