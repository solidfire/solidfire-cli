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

@cli.command('remove', short_help="RemoveDrives")
@click.argument('drives', type=int, required=True)
@pass_context
def remove(ctx, drives):
    """You can use RemoveDrives to proactively remove drives that are part of the cluster."""
    """You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life."""
    """Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method."""
    """Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data."""
    """Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each."""
    """This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;."""
    """When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status."""
    """The drive is unavailable for use in the cluster."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove."""
    AsyncHandleResult = ctx.element.remove_drives(drives=drives)
    print(AsyncHandleResult)

