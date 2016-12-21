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

@cli.command('test', short_help="TestConnectEnsemble")
@click.option('--ensemble',
              type=str,
              required=False,
              help="A comma-separated list of ensemble node CIPs for connectivity testing ")
@pass_context
def test(ctx, ensemble = None):
    """The TestConnectEnsemble API method is used to verify connectivity with a sepcified database ensemble. By default it uses the ensemble for the cluster the node is associated with. Alternatively you can provide a different ensemble to test connectivity with."""
    """&lt;br/&gt;&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""
    TestConnectEnsembleResult = ctx.element.test_connect_ensemble(ensemble=ensemble)
    print(json.dumps(json.loads(jsonpickle.encode(TestConnectEnsembleResult)),indent=4))

