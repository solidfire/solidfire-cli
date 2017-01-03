#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli import parser
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import simplejson
from solidfire.models import NewDrive
from uuid import UUID


@click.group()
@pass_context
def cli(ctx):
    """AddDrives GetDriveConfig GetDriveHardwareInfo GetDriveStats ListDriveHardware ListDrives RemoveDrives ResetDrives SecureEraseDrives TestDrives """
    ctx.sfapi = ctx.client

@cli.command('AddDrives', short_help="AddDrives")
@click.option('--new_drive_drive_id',
              type=int,
              required=True,
              help="""A unique identifier for this drive. """)
@pass_context
def AddDrives(ctx,
           new_drive_drive_id):
    """AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster's data."""
    """When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized."""
    """Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added."""
    """When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each."""
    """This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives."""
    """As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive."""



    kwargsDict = dict()
    kwargsDict["drive_id"] = new_drive_drive_id

    drives = NewDrive(**kwargsDict)

    drives = parser.parse_array(drives)

    AddDrivesResult = ctx.element.add_drives(drives=drives)
    cli_utils.print_result(AddDrivesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetDriveConfig', short_help="GetDriveConfig")
@pass_context
def GetDriveConfig(ctx):
    """GetDriveConfig is used to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""



    GetDriveConfigResult = ctx.element.get_drive_config()
    cli_utils.print_result(GetDriveConfigResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetDriveHardwareInfo', short_help="GetDriveHardwareInfo")
@click.option('--drive_id',
              type=int,
              required=True,
              help="""DriveID for the drive information requested. DriveIDs can be obtained via the "ListDrives" method. """)
@pass_context
def GetDriveHardwareInfo(ctx,
           drive_id):
    """GetDriveHardwareInfo returns all the hardware info for the given drive. This generally includes manufacturers, vendors, versions, and other associated hardware identification information."""



    GetDriveHardwareInfoResult = ctx.element.get_drive_hardware_info(drive_id=drive_id)
    cli_utils.print_result(GetDriveHardwareInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetDriveStats', short_help="GetDriveStats")
@click.option('--drive_id',
              type=int,
              required=True,
              help="""Specifies the drive for which statistics are gathered. """)
@pass_context
def GetDriveStats(ctx,
           drive_id):
    """GetDriveStats return high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the cluster. Some values are specific to Block Drives. Statistical data may not be returned for both block and metadata drives when running this method."""
    """For more information on which drive type returns which data, see Response Example (Block Drive) and Response Example (Volume Metadata Drive) in the SolidFire API guide."""



    GetDriveStatsResult = ctx.element.get_drive_stats(drive_id=drive_id)
    cli_utils.print_result(GetDriveStatsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListDriveHardware', short_help="ListDriveHardware")
@click.option('--force',
              type=bool,
              required=True,
              help="""To run this command, the force parameter must be set to true. """)
@pass_context
def ListDriveHardware(ctx,
           force):
    """ListDriveHardware returns all the drives connected to a node. Use this method on the cluster to return drive hardware information for all the drives on all nodes."""



    ListDriveHardwareResult = ctx.element.list_drive_hardware(force=force)
    cli_utils.print_result(ListDriveHardwareResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListDrives', short_help="ListDrives")
@pass_context
def ListDrives(ctx):
    """ListDrives allows you to retrieve the list of the drives that exist in the cluster's active nodes."""
    """This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available."""



    ListDrivesResult = ctx.element.list_drives()
    cli_utils.print_result(ListDrivesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveDrives', short_help="RemoveDrives")
@click.option('--drives',
              type=str,
              required=True,
              help="""List of driveIDs to remove from the cluster. """)
@pass_context
def RemoveDrives(ctx,
           drives):
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



    drives = parser.parse_array(drives)

    AsyncHandleResult = ctx.element.remove_drives(drives=drives)
    cli_utils.print_result(AsyncHandleResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ResetDrives', short_help="ResetDrives")
@click.option('--drives',
              type=str,
              required=True,
              help="""List of device names (not driveIDs) to reset. """)
@click.option('--force',
              type=bool,
              required=True,
              help="""The "force" parameter must be included on this method to successfully reset a drive. """)
@pass_context
def ResetDrives(ctx,
           drives,
           force):
    """ResetDrives is used to pro-actively initialize drives and remove all data currently residing on the drive. The drive can then be reused in an existing node or used in an upgraded SolidFire node. This method requires the force=true parameter to be included in the method call."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""



    ResetDrivesResult = ctx.element.reset_drives(drives=drives, force=force)
    cli_utils.print_result(ResetDrivesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SecureEraseDrives', short_help="SecureEraseDrives")
@click.option('--drives',
              type=str,
              required=True,
              help="""List of driveIDs to secure erase. """)
@pass_context
def SecureEraseDrives(ctx,
           drives):
    """SecureEraseDrives is used to remove any residual data from drives that have a status of &quot;available.&quot; For example, when replacing a drive at its end-of-life that contained sensitive data."""
    """It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method."""
    """The GetAsyncResult method can be used to check on the status of the secure erase operation."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to secure erase."""



    drives = parser.parse_array(drives)

    AsyncHandleResult = ctx.element.secure_erase_drives(drives=drives)
    cli_utils.print_result(AsyncHandleResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('TestDrives', short_help="TestDrives")
@click.option('--minutes',
              type=int,
              required=False,
              help="""The number of minutes to run the test can be specified. """)
@pass_context
def TestDrives(ctx,
           minutes = None):
    """The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This test takes approximately 10 minutes."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: This method is available only through the per-node API endpoint 5.0 or later."""



    TestDrivesResult = ctx.element.test_drives(minutes=minutes)
    cli_utils.print_result(TestDrivesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

