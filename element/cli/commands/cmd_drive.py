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
from element import utils
import jsonpickle
import simplejson
from solidfire.models import *
from solidfire.custom.models import *
from uuid import UUID
from element import exceptions
from solidfire import common
from element.cli.cli import SolidFireOption, SolidFireCommand

@click.group()
@pass_context
def cli(ctx):
    """reset secureerase list remove gethardwareinfo liststats add getstats getconfig test listhardware """

@cli.command('reset', short_help="""ResetDrives enables you to proactively initialize drives and remove all data currently residing on a drive. The drive can then be reused in an existing node or used in an upgraded node. This method requires the force parameter to be included in the method call. """, cls=SolidFireCommand)
@click.option('--drives',
              type=str,
              required=True,
              prompt=True,
              help="""List of device names (not driveIDs) to reset. """)
@click.option('--force',
              type=bool,
              required=True,
              prompt=True,
              help="""Required parameter to successfully reset a drive. """)
@pass_context
def reset(ctx,
           # Mandatory main parameter
           drives,
           # Mandatory main parameter
           force):
    """ResetDrives enables you to proactively initialize drives and remove all data currently residing on a drive. The drive can then be reused"""
    """in an existing node or used in an upgraded node. This method requires the force parameter to be included in the method call."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""drives = """ + str(drives)+";"+"""force = """ + str(force)+""";"""+"")
    try:
        _ResetDrivesResult = ctx.element.reset_drives(drives=drives, force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ResetDrivesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ResetDrivesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('secureerase', short_help="""SecureEraseDrives enables you to remove any residual data from drives that have a status of "available." You might want to use this method when replacing a drive nearing the end of its service life that contained sensitive data. This method uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. This asynchronous method might take up to two minutes to complete. You can use GetAsyncResult to check on the status of the secure erase operation. You can use the ListDrives method to obtain the driveIDs for the drives you want to secure erase. """, cls=SolidFireCommand)
@click.option('--drives',
              type=str,
              required=True,
              prompt=True,
              help="""List of driveIDs to be secure erased. """)
@pass_context
def secureerase(ctx,
           # Mandatory main parameter
           drives):
    """SecureEraseDrives enables you to remove any residual data from drives that have a status of "available." You might want to use this method when replacing a drive nearing the end of its service life that contained sensitive data. This method uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. This asynchronous method might take up to two minutes to complete. You can use GetAsyncResult to check on the status of the secure erase operation."""
    """You can use the ListDrives method to obtain the driveIDs for the drives you want to secure erase."""

    

    cli_utils.establish_connection(ctx)
    

    drives = parser.parse_array(drives)
    

    ctx.logger.info(""": """"""drives = """ + str(drives)+""";"""+"")
    try:
        _AsyncHandleResult = ctx.element.secure_erase_drives(drives=drives)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AsyncHandleResult), indent=4))
        return
    else:
        cli_utils.print_result(_AsyncHandleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListDrives enables you to retrieve the list of the drives that exist in the cluster's active nodes. This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available. """, cls=SolidFireCommand)
@pass_context
def list(ctx):
    """ListDrives enables you to retrieve the list of the drives that exist in the cluster's active nodes. This method returns drives that have"""
    """been added as volume metadata or block drives as well as drives that have not been added and are available."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListDrivesResult = ctx.element.list_drives()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListDrivesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListDrivesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""You can use RemoveDrives to proactively remove drives that are part of the cluster. You might want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life. Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method. Depending on the total capacity of the drives being removed, it might take several minutes to migrate all of the data. Use the GetAsyncResult method to check the status of the remove operation. When removing multiple drives, use a single RemoveDrives method call rather than multiple individual methods with a single drive each. This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster. You can also remove drives with a "failed" status using RemoveDrives. When you remove a drive with a "failed" status it is not returned to an "available" or active status. The drive is unavailable for use in the cluster. Use the ListDrives method to obtain the driveIDs for the drives you want to remove. """, cls=SolidFireCommand)
@click.option('--drives',
              type=str,
              required=True,
              prompt=True,
              help="""List of driveIDs to remove from the cluster. """)
@click.option('--forceduringupgrade',
              type=bool,
              required=False,
              help="""If you want to remove a drive during upgrade, this must be set to true. """)
@pass_context
def remove(ctx,
           # Mandatory main parameter
           drives,
           # Optional main parameter
           forceduringupgrade = None):
    """You can use RemoveDrives to proactively remove drives that are part of the cluster. You might want to use this method when"""
    """reducing cluster capacity or preparing to replace drives nearing the end of their service life. Any data on the drives is removed and"""
    """migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method. Depending on"""
    """the total capacity of the drives being removed, it might take several minutes to migrate all of the data. Use the GetAsyncResult"""
    """method to check the status of the remove operation."""
    """When removing multiple drives, use a single RemoveDrives method call rather than multiple individual methods with a single drive"""
    """each. This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster."""
    """You can also remove drives with a "failed" status using RemoveDrives. When you remove a drive with a "failed" status it is not"""
    """returned to an "available" or active status. The drive is unavailable for use in the cluster."""
    """Use the ListDrives method to obtain the driveIDs for the drives you want to remove."""

    

    cli_utils.establish_connection(ctx)
    

    drives = parser.parse_array(drives)
    
    

    ctx.logger.info(""": """"""drives = """ + str(drives)+";" + """forceduringupgrade = """+str(forceduringupgrade)+""";"""+"")
    try:
        _AsyncHandleResult = ctx.element.remove_drives(drives=drives, force_during_upgrade=forceduringupgrade)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AsyncHandleResult), indent=4))
        return
    else:
        cli_utils.print_result(_AsyncHandleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('gethardwareinfo', short_help="""GetDriveHardwareInfo returns all the hardware information for the given drive. This generally includes details about manufacturers, vendors, versions, and other associated hardware identification information. """, cls=SolidFireCommand)
@click.option('--driveid',
              type=int,
              required=True,
              prompt=True,
              help="""DriveID for the drive information requested. You can get DriveIDs by using the ListDrives method. """)
@pass_context
def gethardwareinfo(ctx,
           # Mandatory main parameter
           driveid):
    """GetDriveHardwareInfo returns all the hardware information for the given drive. This generally includes details about manufacturers, vendors, versions, and"""
    """other associated hardware identification information."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""driveid = """ + str(driveid)+""";"""+"")
    try:
        _GetDriveHardwareInfoResult = ctx.element.get_drive_hardware_info(drive_id=driveid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetDriveHardwareInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetDriveHardwareInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('liststats', short_help="""ListDriveStats enables you to retrieve high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives. """, cls=SolidFireCommand)
@click.option('--drives',
              type=str,
              required=False,
              help="""Optional list of DriveIDs for which to return drive statistics. If you omit this parameter, measurements for all drives are returned. """)
@pass_context
def liststats(ctx,
           # Optional main parameter
           drives = None):
    """ListDriveStats enables you to retrieve high-level activity measurements for multiple drives in the cluster. By default, this method returns statistics for all drives in the cluster, and these measurements are cumulative from the addition of the drive to the cluster. Some values this method returns are specific to block drives, and some are specific to metadata drives."""

    

    cli_utils.establish_connection(ctx)
    

    drives = parser.parse_array(drives)
    

    ctx.logger.info(""": """"""drives = """+str(drives)+""";"""+"")
    try:
        _ListDriveStatsResult = ctx.element.list_drive_stats(drives=drives)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListDriveStatsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListDriveStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('add', short_help="""AddDrives enables you to add one or more available drives to the cluster, enabling the drives to host a portion of the cluster's data. When you add a node to the cluster or install new drives in an existing node, the new drives are marked as "available" and must be added via AddDrives before they can be utilized. Use the ListDrives method to display drives that are "available" to be added. When you add multiple drives, it is more efficient to add them in a single AddDrives method call rather than multiple individual methods with a single drive each. This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster. When you add a drive, the system automatically determines the "type" of drive it should be. The method is asynchronous and returns immediately. However, it can take some time for the data in the cluster to be rebalanced using the newly added drives. As the new drives are syncing on the system, you can use the ListSyncJobs method to see how the drives are being rebalanced and the progress of adding the new drive. You can also use the GetAsyncResult method to query the method's returned asyncHandle. """, cls=SolidFireCommand)
@click.option('--drives',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["driveid", "type", ],
              required=True,
              help="""Returns information about each drive to be added to the cluster. Possible values are: driveID: The ID of the drive to add. (Integer) type: (Optional) The type of drive to add. Valid values are "slice" or "block". If omitted, the system assigns the correct type. (String)  Has the following subparameters: --driveid --type """)
@click.option('--driveid',
              required=True,
              prompt=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] A unique identifier for this drive. """,
              cls=SolidFireOption)
@click.option('--type',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] block or slice """,
              cls=SolidFireOption)
@click.option('--forceduringupgrade',
              type=bool,
              required=False,
              help="""Allows the user to force the addition of drives during an upgrade. """)
@click.option('--forceduringbinsync',
              type=bool,
              required=False,
              help="""Allows the user to force the addition of drives during a bin sync operation. """)
@pass_context
def add(ctx,
           # Mandatory main parameter
           drives,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           driveid,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           type = None,
           # Optional main parameter
           forceduringupgrade = None,
           # Optional main parameter
           forceduringbinsync = None):
    """AddDrives enables you to add one or more available drives to the cluster, enabling the drives to host a portion of the cluster's data."""
    """When you add a node to the cluster or install new drives in an existing node, the new drives are marked as "available" and must be"""
    """added via AddDrives before they can be utilized. Use the ListDrives method to display drives that are "available" to be added. When"""
    """you add multiple drives, it is more efficient to add them in a single AddDrives method call rather than multiple individual methods"""
    """with a single drive each. This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster."""
    """When you add a drive, the system automatically determines the "type" of drive it should be."""
    """The method is asynchronous and returns immediately. However, it can take some time for the data in the cluster to be rebalanced"""
    """using the newly added drives. As the new drives are syncing on the system, you can use the ListSyncJobs method to see how the"""
    """drives are being rebalanced and the progress of adding the new drive. You can also use the GetAsyncResult method to query the"""
    """method's returned asyncHandle."""

    

    cli_utils.establish_connection(ctx)
    

    drivesArray = None
    if len(drives) == 1 and driveid[0] is None and type[0] is None:
        drivesArray = []
    elif(drives is not None and drives != ()):
        drivesArray = []
        try:
            for i, _drives in enumerate(drives):
                drivesArray.append(NewDrive(drive_id=driveid[i], type=type[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    
    
    

    ctx.logger.info(""": """"""drives = """ + str(drivesArray)+";" + """forceduringupgrade = """+str(forceduringupgrade)+";" + """forceduringbinsync = """+str(forceduringbinsync)+""";"""+"")
    try:
        _AddDrivesResult = ctx.element.add_drives(drives=drivesArray, force_during_upgrade=forceduringupgrade, force_during_bin_sync=forceduringbinsync)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AddDrivesResult), indent=4))
        return
    else:
        cli_utils.print_result(_AddDrivesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstats', short_help="""GetDriveStats returns high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the cluster. Some values are specific to block drives. You might not obtain statistical data for both block and metadata drives when you run this method.  """, cls=SolidFireCommand)
@click.option('--driveid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the drive for which statistics are gathered. """)
@pass_context
def getstats(ctx,
           # Mandatory main parameter
           driveid):
    """GetDriveStats returns high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the"""
    """cluster. Some values are specific to block drives. You might not obtain statistical data for both block and metadata drives when you"""
    """run this method. """

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""driveid = """ + str(driveid)+""";"""+"")
    try:
        _GetDriveStatsResult = ctx.element.get_drive_stats(drive_id=driveid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetDriveStatsResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetDriveStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getconfig', short_help="""GetDriveConfig enables you to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def getconfig(ctx):
    """GetDriveConfig enables you to display drive information for expected slice and block drive counts as well as the number of slices"""
    """and block drives that are currently connected to the node."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetDriveConfigResult = ctx.element.get_drive_config()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetDriveConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetDriveConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('test', short_help="""You can use the TestDrives API method to run a hardware validation on all drives on the node. This method detects hardware failures on the drives (if present) and reports them in the results of the validation tests. You can only use the TestDrives method on nodes that are not "active" in a cluster. Note: This test takes approximately 10 minutes. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--minutes',
              type=int,
              required=False,
              help="""Specifies the number of minutes to run the test. """)
@click.option('--force',
              type=bool,
              required=False,
              help="""Required parameter to successfully test the drives on the node. """)
@pass_context
def test(ctx,
           # Optional main parameter
           minutes = None,
           # Optional main parameter
           force = None):
    """You can use the TestDrives API method to run a hardware validation on all drives on the node. This method detects hardware"""
    """failures on the drives (if present) and reports them in the results of the validation tests."""
    """You can only use the TestDrives method on nodes that are not "active" in a cluster."""
    """Note: This test takes approximately 10 minutes."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""minutes = """+str(minutes)+";" + """force = """+str(force)+""";"""+"")
    try:
        _TestDrivesResult = ctx.element.test_drives(minutes=minutes, force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestDrivesResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestDrivesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listhardware', short_help="""ListDriveHardware returns all the drives connected to a node. Use this method on individual nodes to return drive hardware information or use this method on the cluster master node MVIP to see information for all the drives on all nodes. Note: The "securitySupported": true line of the method response does not imply that the drives are capable of encryption; only that the security status can be queried. If you have a node type with a model number ending in "-NE", commands to enable security features on these drives will fail. See the EnableEncryptionAtRest method for more information. """, cls=SolidFireCommand)
@click.option('--force',
              type=bool,
              required=True,
              prompt=True,
              help="""To run this command, the force parameter must be set to true. """)
@pass_context
def listhardware(ctx,
           # Mandatory main parameter
           force):
    """ListDriveHardware returns all the drives connected to a node. Use this method on individual nodes to return drive hardware"""
    """information or use this method on the cluster master node MVIP to see information for all the drives on all nodes."""
    """Note: The "securitySupported": true line of the method response does not imply that the drives are capable of"""
    """encryption; only that the security status can be queried. If you have a node type with a model number ending in "-NE","""
    """commands to enable security features on these drives will fail. See the EnableEncryptionAtRest method for more information."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""force = """ + str(force)+""";"""+"")
    try:
        _ListDriveHardwareResult = ctx.element.list_drive_hardware(force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListDriveHardwareResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListDriveHardwareResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

