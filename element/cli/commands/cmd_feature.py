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

@cli.command('enable', short_help="EnableFeature")
@click.argument('feature', type=str, required=True)
@pass_context
def enable(ctx, feature):
    """EnableFeature allows you to enable cluster features that are disabled by default."""
    EnableFeatureResult = ctx.element.enable_feature(feature=feature)
    print(EnableFeatureResult)

