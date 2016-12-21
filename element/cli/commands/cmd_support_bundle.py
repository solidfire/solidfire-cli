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

@cli.command('create', short_help="CreateSupportBundle")
@click.argument('bundle_name', type=str, required=False)
@click.argument('extra_args', type=str, required=False)
@click.argument('timeout_sec', type=int, required=False)
@pass_context
def create(ctx, bundle_name = None, extra_args = None, timeout_sec = None):
    """CreateSupportBundle is used to create a support bundle file under the node's directory. When the bundle has been successfully created, the bundle is stored on the node as a tar.gz file."""
    CreateSupportBundleResult = ctx.element.create_support_bundle(bundle_name=bundle_name, extra_args=extra_args, timeout_sec=timeout_sec)
    print(CreateSupportBundleResult)

