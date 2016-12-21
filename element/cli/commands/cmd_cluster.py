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

@cli.command('create', short_help="CreateCluster")
@click.option('--accept_eula',
              type=bool,
              required=False,
              help="Indicate your acceptance of the End User License Agreement when creating this cluster. To accept the EULA, set this parameter to true. ")
@click.option('--mvip',
              type=str,
              required=True,
              help="Floating (virtual) IP address for the cluster on the management network. ")
@click.option('--svip',
              type=str,
              required=True,
              help="Floating (virtual) IP address for the cluster on the storage (iSCSI) network. ")
@click.option('--rep_count',
              type=int,
              required=True,
              help="Number of replicas of each piece of data to store in the cluster. Valid value is "2". ")
@click.option('--username',
              type=str,
              required=True,
              help="User name for the cluster admin. ")
@click.option('--password',
              type=str,
              required=True,
              help="Initial password for the cluster admin account. ")
@click.option('--nodes',
              type=str,
              required=True,
              help="CIP/SIP addresses of the initial set of nodes making up the cluster. This node's IP must be in the list. ")
@click.option('--attributes',
              type=dict,
              required=False,
              help="List of Name/Value pairs in JSON object format. ")
@pass_context
def create(ctx, mvip, svip, rep_count, username, password, nodes, accept_eula = None, attributes = None):
    """The CreateCluster method is used to initialize the node in a cluster that has ownership of the &quot;mvip&quot; and &quot;svip&quot; addresses. Each new cluster is initialized using the MIP of the first node in the cluster. This method also automatically adds all the nodes being configured into the cluster. The method is used only once each time a new cluster is initialized."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: You need to log into the node that is used as the master node for the cluster. Once logged in, run the GetBootstrapConfig method on the node to get the IP addresses for the rest of the nodes that you want to include in the cluster. Then run the CreateCluster method."""
    CreateClusterResult = ctx.element.create_cluster(mvip=mvip, svip=svip, rep_count=rep_count, username=username, password=password, nodes=nodes, accept_eula=accept_eula, attributes=attributes)
    print(json.dumps(json.loads(jsonpickle.encode(CreateClusterResult)),indent=4))

