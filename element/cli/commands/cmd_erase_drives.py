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

@cli.command('secure', short_help="SecureEraseDrives")
@click.argument('drives', type=int, required=True)
@pass_context
def secure(ctx, drives):
    """SecureEraseDrives is used to remove any residual data from drives that have a status of &quot;available.&quot; For example, when replacing a drive at its end-of-life that contained sensitive data."""
    """It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method."""
    """The GetAsyncResult method can be used to check on the status of the secure erase operation."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to secure erase."""
    AsyncHandleResult = ctx.element.secure_erase_drives(drives=drives)
    print(AsyncHandleResult)

