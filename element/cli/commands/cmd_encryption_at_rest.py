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

@cli.command('disable', short_help="DisableEncryptionAtRest")
@pass_context
def disable(ctx):
    """The DisableEncryptionAtRest method enables you to remove the encryption that was previously applied to the cluster using the EnableEncryptionAtRest method."""
    """This disable method is asynchronous and returns a response before encryption is disabled."""
    """You can use the GetClusterInfo method to poll the system to see when the process has completed."""
    DisableEncryptionAtRestResult = ctx.element.disable_encryption_at_rest()
    print(DisableEncryptionAtRestResult)

