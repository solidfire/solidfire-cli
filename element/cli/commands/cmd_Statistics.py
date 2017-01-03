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
from uuid import UUID


@click.group()
@pass_context
def cli(ctx):
    """GetCompleteStats GetHardwareInfo GetRawStats ListDriveStats ListVolumeStats ListVolumeStatsByVirtualVolume """
    ctx.sfapi = ctx.client

@cli.command('GetCompleteStats', short_help="GetCompleteStats")
@pass_context
def GetCompleteStats(ctx):
    """The GetCompleteStats API method is used by SolidFire engineering to troubleshoot new features. The data returned from GetCompleteStats is not documented, changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster."""
    """The data returned from GetCompleteStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetCompleteStats for collecting performance data or any other management integration with a SolidFire cluster."""



    str = ctx.element.get_complete_stats()
    cli_utils.print_result(str, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetHardwareInfo', short_help="GetHardwareInfo")
@pass_context
def GetHardwareInfo(ctx):
    """GetHardwareInfo allows you to return hardware information and status for a single node. This generally includes manufacturers, vendors, versions, drives, and other associated hardware identification information."""



    GetHardwareInfoResult = ctx.element.get_hardware_info()
    cli_utils.print_result(GetHardwareInfoResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetRawStats', short_help="GetRawStats")
@pass_context
def GetRawStats(ctx):
    """The GetRawStats call is used by SolidFire engineering to troubleshoot new features. The data returned from GetRawStats is not documented, it changes frequently, and is not guaranteed to be accurate. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster."""
    """The data returned from GetRawStats changes frequently, and is not guaranteed to accurately show performance from the system. It is not recommended to ever use GetRawStats for collecting performance data or any other management integration with a SolidFire cluster."""



    str = ctx.element.get_raw_stats()
    cli_utils.print_result(str, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListDriveStats', short_help="ListDriveStats")
@click.option('--drives',
              type=str,
              required=False,
              help="""Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned. """)
@pass_context
def ListDriveStats(ctx,
           drives = None):
    """ListDriveStats enables you to retrieve  high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives. For more information on what data each drive type returns, see the response examples for the GetDriveStats method."""



    drives = parser.parse_array(drives)

    ListDriveStatsResult = ctx.element.list_drive_stats(drives=drives)
    cli_utils.print_result(ListDriveStatsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListVolumeStats', short_help="ListVolumeStats")
@click.option('--volume_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListVolumeStats(ctx,
           volume_ids = None):



    volume_ids = parser.parse_array(volume_ids)

    ListVolumeStatsResult = ctx.element.list_volume_stats(volume_ids=volume_ids)
    cli_utils.print_result(ListVolumeStatsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListVolumeStatsByVirtualVolume', short_help="ListVolumeStatsByVirtualVolume")
@click.option('--virtual_volume_ids',
              type=str,
              required=False,
              help="""A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
def ListVolumeStatsByVirtualVolume(ctx,
           virtual_volume_ids = None):
    """ListVolumeStatsByVirtualVolume enables you to list statistics for volumes, sorted by virtual volumes."""



    virtual_volume_ids = parser.parse_array(virtual_volume_ids)

    ListVolumeStatsByVirtualVolumeResult = ctx.element.list_volume_stats_by_virtual_volume(virtual_volume_ids=virtual_volume_ids)
    cli_utils.print_result(ListVolumeStatsByVirtualVolumeResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

