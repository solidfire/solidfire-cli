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

@cli.command('get', short_help="GetClusterState")
@click.argument('force', type=bool, required=True)
@pass_context
def get(ctx, force):
    """The GetClusterState method is used to indicate if a node is part of a cluster or not. The three states are: &lt;br&gt;&lt;strong&gt;Available:&lt;/strong&gt; Node has not been configured with a cluster name.&lt;br&gt;&lt;strong&gt;Pending:&lt;/strong&gt; Node is pending for a specific named cluster and can be added.&lt;br&gt;&lt;strong&gt;Active:&lt;/strong&gt; Node is active and a member of a cluster and may not be added to another cluster."""
    GetClusterStateResult = ctx.element.get_cluster_state(force=force)
    print(json.dumps(json.loads(jsonpickle.encode(GetClusterStateResult)),indent=4))

