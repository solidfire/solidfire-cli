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
    """reset secureerase list remove gethardwareinfo add getstats getconfig test listhardware """

@cli.command('reset', short_help="""ResetDrives is used to pro-actively initialize drives and remove all data currently residing on the drive. The drive can then be reused in an existing node or used in an upgraded SolidFire node. This method requires the force=true parameter to be included in the method call.  Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--drives',
              type=str,
              required=True,
              help="""List of device names (not driveIDs) to reset. """)
@click.option('--force',
              type=bool,
              required=True,
              help="""The "force" parameter must be included on this method to successfully reset a drive. """)
@pass_context
def reset(ctx,
           # Mandatory main parameter
           drives,
           # Mandatory main parameter
           force):
    """ResetDrives is used to pro-actively initialize drives and remove all data currently residing on the drive. The drive can then be reused in an existing node or used in an upgraded SolidFire node. This method requires the force=true parameter to be included in the method call."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

        
    

    ctx.logger.info("""drives = """+str(drives)+""";"""+"""force = """+str(force)+""";"""+"")
    try:
        _ResetDrivesResult = ctx.element.(drives=drives, force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ResetDrivesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('secureerase', short_help="""SecureEraseDrives is used to remove any residual data from drives that have a status of "available." For example, when replacing a drive at its end-of-life that contained sensitive data. It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method. The GetAsyncResult method can be used to check on the status of the secure erase operation.  Use the "ListDrives" method to obtain the driveIDs for the drives you want to secure erase. """, cls=SolidFireCommand)
@click.option('--drives',
              type=str,
              required=True,
              help="""List of driveIDs to secure erase. """)
@pass_context
def secureerase(ctx,
           # Mandatory main parameter
           drives):
    """SecureEraseDrives is used to remove any residual data from drives that have a status of &quot;available.&quot; For example, when replacing a drive at its end-of-life that contained sensitive data."""
    """It uses a Security Erase Unit command to write a predetermined pattern to the drive and resets the encryption key on the drive. The method may take up to two minutes to complete, so it is an asynchronous method."""
    """The GetAsyncResult method can be used to check on the status of the secure erase operation."""
    """"""
    """Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to secure erase."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    drives = parser.parse_array(drives)
    

    ctx.logger.info("""drives = """+str(drives)+""";"""+"")
    try:
        _AsyncHandleResult = ctx.element.(drives=drives)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_AsyncHandleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListDrives allows you to retrieve the list of the drives that exist in the cluster's active nodes. This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available. """, cls=SolidFireCommand)
@pass_context
def list(ctx):
    """ListDrives allows you to retrieve the list of the drives that exist in the cluster&#x27;s active nodes."""
    """This method returns drives that have been added as volume metadata or block drives as well as drives that have not been added and are available."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListDrivesResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListDrivesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""You can use RemoveDrives to proactively remove drives that are part of the cluster. You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life. Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method. Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data. Use the "GetAsyncResult" method to check the status of the remove operation.  When removing multiple drives, use a single "RemoveDrives" method call rather than multiple individual methods with a single drive each. This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster.  You can also remove drives with a "failed" status using "RemoveDrives". When you remove a drive with a "failed" status it is not returned to an "available" or "active" status. The drive is unavailable for use in the cluster.  Use the "ListDrives" method to obtain the driveIDs for the drives you want to remove. """, cls=SolidFireCommand)
@click.option('--drives',
              type=str,
              required=True,
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
    """You can use RemoveDrives to proactively remove drives that are part of the cluster."""
    """You may want to use this method when reducing cluster capacity or preparing to replace drives nearing the end of their service life."""
    """Any data on the drives is removed and migrated to other drives in the cluster before the drive is removed from the cluster. This is an asynchronous method."""
    """Depending on the total capacity of the drives being removed, it may take several minutes to migrate all of the data."""
    """Use the &quot;GetAsyncResult&quot; method to check the status of the remove operation."""
    """"""
    """When removing multiple drives, use a single &quot;RemoveDrives&quot; method call rather than multiple individual methods with a single drive each."""
    """This reduces the amount of data balancing that must occur to even stabilize the storage load on the cluster."""
    """"""
    """You can also remove drives with a &quot;failed&quot; status using &quot;RemoveDrives&quot;."""
    """When you remove a drive with a &quot;failed&quot; status it is not returned to an &quot;available&quot; or &quot;active&quot; status."""
    """The drive is unavailable for use in the cluster."""
    """"""
    """Use the &quot;ListDrives&quot; method to obtain the driveIDs for the drives you want to remove."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    drives = parser.parse_array(drives)    
    

    ctx.logger.info("""drives = """+str(drives)+""";"""+"""forceduringupgrade = """+str(forceduringupgrade)+""";"""+"")
    try:
        _AsyncHandleResult = ctx.element.(drives=drives, force_during_upgrade=forceduringupgrade)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_AsyncHandleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('gethardwareinfo', short_help="""GetDriveHardwareInfo returns all the hardware info for the given drive. This generally includes manufacturers, vendors, versions, and other associated hardware identification information. """, cls=SolidFireCommand)
@click.option('--driveid',
              type=int,
              required=True,
              help="""DriveID for the drive information requested. DriveIDs can be obtained via the "ListDrives" method. """)
@pass_context
def gethardwareinfo(ctx,
           # Mandatory main parameter
           driveid):
    """GetDriveHardwareInfo returns all the hardware info for the given drive. This generally includes manufacturers, vendors, versions, and other associated hardware identification information."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""driveid = """+str(driveid)+""";"""+"")
    try:
        _GetDriveHardwareInfoResult = ctx.element.(drive_id=driveid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetDriveHardwareInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('add', short_help="""AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster's data. When you add a node to the cluster or install new drives in an existing node, the new drives are marked as "available" and must be added via AddDrives before they can be utilized. Use the "ListDrives" method to display drives that are "available" to be added. When you add multiple drives, it is more efficient to add them in a single "AddDrives" method call rather than multiple individual methods with a single drive each. This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster.  When you add a drive, the system automatically determines the "type" of drive it should be.  The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives. As the new drive(s) are syncing on the system, you can use the "ListSyncJobs" method to see how the drive(s) are being rebalanced and the progress of adding the new drive. """, cls=SolidFireCommand)
@click.option('--drives',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["driveid", "type", ],
              required=True,
              help="""List of drives to add to the cluster.  Has the following subparameters: --driveid --type """)
@click.option('--driveid',
              required=True,
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
@pass_context
def add(ctx,
           # Mandatory main parameter
           drives,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           driveid,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           type = None,
           # Optional main parameter
           forceduringupgrade = None):
    """AddDrives is used to add one or more available drives to the cluster enabling the drives to host a portion of the cluster&#x27;s data."""
    """When you add a node to the cluster or install new drives in an existing node, the new drives are marked as &quot;available&quot; and must be added via AddDrives before they can be utilized."""
    """Use the &quot;ListDrives&quot; method to display drives that are &quot;available&quot; to be added."""
    """When you add multiple drives, it is more efficient to add them in a single &quot;AddDrives&quot; method call rather than multiple individual methods with a single drive each."""
    """This reduces the amount of data balancing that must occur to stabilize the storage load on the cluster."""
    """"""
    """When you add a drive, the system automatically determines the &quot;type&quot; of drive it should be."""
    """"""
    """The method returns immediately. However, it may take some time for the data in the cluster to be rebalanced using the newly added drives."""
    """As the new drive(s) are syncing on the system, you can use the &quot;ListSyncJobs&quot; method to see how the drive(s) are being rebalanced and the progress of adding the new drive."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    drivesArray = []
    if(drives is not None):
        try:
            for i, _drives in enumerate(drives):
                drivesArray.append(NewDrive(drive_id=driveid[i], type=type[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)    
    

    ctx.logger.info("""drives = """+str(drives)+""";"""+"""forceduringupgrade = """+str(forceduringupgrade)+""";"""+"")
    try:
        _AddDrivesResult = ctx.element.(drives=drivesArray, force_during_upgrade=forceduringupgrade)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_AddDrivesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstats', short_help="""GetDriveStats return high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the cluster. Some values are specific to Block Drives. Statistical data may not be returned for both block and metadata drives when running this method. For more information on which drive type returns which data, see Response Example (Block Drive) and Response Example (Volume Metadata Drive) in the SolidFire API guide. """, cls=SolidFireCommand)
@click.option('--driveid',
              type=int,
              required=True,
              help="""Specifies the drive for which statistics are gathered. """)
@pass_context
def getstats(ctx,
           # Mandatory main parameter
           driveid):
    """GetDriveStats return high-level activity measurements for a single drive. Values are cumulative from the addition of the drive to the cluster. Some values are specific to Block Drives. Statistical data may not be returned for both block and metadata drives when running this method."""
    """For more information on which drive type returns which data, see Response Example (Block Drive) and Response Example (Volume Metadata Drive) in the SolidFire API guide."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""driveid = """+str(driveid)+""";"""+"")
    try:
        _GetDriveStatsResult = ctx.element.(drive_id=driveid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetDriveStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getconfig', short_help="""GetDriveConfig is used to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node.  Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def getconfig(ctx):
    """GetDriveConfig is used to display drive information for expected slice and block drive counts as well as the number of slices and block drives that are currently connected to the node."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetDriveConfigResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetDriveConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('test', short_help="""The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests.  Note: This test takes approximately 10 minutes.  Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--minutes',
              type=int,
              required=False,
              help="""The number of minutes to run the test can be specified. """)
@pass_context
def test(ctx,
           # Optional main parameter
           minutes = None):
    """The TestDrives API method is used to run a hardware validation on all the drives on the node. Hardware failures on the drives are detected if present and they are reported in the results of the validation tests."""
    """"""
    """Note: This test takes approximately 10 minutes."""
    """"""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""minutes = """+str(minutes)+""";"""+"")
    try:
        _TestDrivesResult = ctx.element.(minutes=minutes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_TestDrivesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listhardware', short_help="""ListDriveHardware returns all the drives connected to a node. Use this method on the cluster to return drive hardware information for all the drives on all nodes. """, cls=SolidFireCommand)
@click.option('--force',
              type=bool,
              required=True,
              help="""To run this command, the force parameter must be set to true. """)
@pass_context
def listhardware(ctx,
           # Mandatory main parameter
           force):
    """ListDriveHardware returns all the drives connected to a node. Use this method on the cluster to return drive hardware information for all the drives on all nodes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""force = """+str(force)+""";"""+"")
    try:
        _ListDriveHardwareResult = ctx.element.(force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListDriveHardwareResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

