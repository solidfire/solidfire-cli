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

@cli.command('remove', short_help="RemoveClusterPair")
@click.argument('cluster_pair_id', type=int, required=True)
@pass_context
def remove(ctx, cluster_pair_id):
    """You can use the RemoveClusterPair method to close the open connections between two paired clusters.&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the &quot;RemoveVolumePair&quot; API method."""
    RemoveClusterPairResult = ctx.element.remove_cluster_pair(cluster_pair_id=cluster_pair_id)
    print(json.dumps(json.loads(jsonpickle.encode(RemoveClusterPairResult)),indent=4))

