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

@cli.command('remove', short_help="RemoveClusterAdmin")
@click.option('--cluster_admin_id',
              type=int,
              required=True,
              help="ClusterAdminID for the Cluster Admin to remove. ")
@pass_context
def remove(ctx, cluster_admin_id):
    """RemoveClusterAdmin is used to remove a Cluster Admin. The &quot;admin&quot; Cluster Admin cannot be removed."""
    RemoveClusterAdminResult = ctx.element.remove_cluster_admin(cluster_admin_id=cluster_admin_id)
    print(json.dumps(json.loads(jsonpickle.encode(RemoveClusterAdminResult)),indent=4))

