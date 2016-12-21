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

@cli.command('list', short_help="ListNetworkInterfaces")
@pass_context
def list(ctx):
    """The ListNetworkInterfaces API method is used to return information about each network interface on a node. The API method is intended for use on individual nodes. """
    ListNetworkInterfacesResult = ctx.element.list_network_interfaces()
    print(json.dumps(json.loads(jsonpickle.encode(ListNetworkInterfacesResult)),indent=4))

