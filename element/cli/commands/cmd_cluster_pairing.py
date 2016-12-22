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

@cli.command('start', short_help="StartClusterPairing")
@pass_context
def start(ctx):
    """StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster."""
    """The key created from this API method is used in the &quot;CompleteClusterPairing&quot; API method to establish a cluster pairing."""
    """You can pair a cluster with a maximum of four other SolidFire clusters."""
    StartClusterPairingResult = ctx.element.start_cluster_pairing()
    cli_utils.print_result(StartClusterPairingResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

