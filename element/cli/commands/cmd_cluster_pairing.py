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

@cli.command('complete', short_help="CompleteClusterPairing")
@click.argument('cluster_pairing_key', type=str, required=True)
@pass_context
def complete(ctx, cluster_pairing_key):
    """The CompleteClusterPairing method is the second step in the cluster pairing process."""
    """Use this method with the encoded key received from the &quot;StartClusterPairing&quot; API method to complete the cluster pairing process."""
    CompleteClusterPairingResult = ctx.element.complete_cluster_pairing(cluster_pairing_key=cluster_pairing_key)
    print(CompleteClusterPairingResult)

