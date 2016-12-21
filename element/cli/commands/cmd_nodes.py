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

@cli.command('remove', short_help="RemoveNodes")
@click.argument('nodes', type=int, required=True)
@pass_context
def remove(ctx, nodes):
    """RemoveNodes is used to remove one or more nodes that should no longer participate in the cluster. Before removing a node, all drives it contains must first be removed with &quot;RemoveDrives&quot; method. A node cannot be removed until the RemoveDrives process has completed and all data has been migrated away from the node."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """Once removed, a node registers itself as a pending node and can be added again, or shut down which removes it from the &quot;Pending Node&quot; list."""
    RemoveNodesResult = ctx.element.remove_nodes(nodes=nodes)
    print(json.dumps(json.loads(jsonpickle.encode(RemoveNodesResult)),indent=4))

