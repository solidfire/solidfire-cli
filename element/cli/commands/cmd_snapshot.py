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
    """listgroup modifygroup modify create list createschedule deletegroup getschedule rollbacktogroup rollbackto creategroup modifyschedule listschedules delete """

@cli.command('listgroup', short_help="""ListGroupSnapshots is used to return information about all group snapshots that have been created. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=False,
              help="""An array of unique volume IDs to query. If this parameter is not specified, all group snapshots on the cluster will be included. """)
@click.option('--groupsnapshotid',
              type=int,
              required=True,
              help="""Get info about individual snapshot """)
@pass_context
def listgroup(ctx,
           # Mandatory main parameter
           groupsnapshotid,
           # Optional main parameter
           volumeid = None):
    """ListGroupSnapshots is used to return information about all group snapshots that have been created."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

        
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""groupsnapshotid = """+str(groupsnapshotid)+""";"""+"")
    try:
        _ListGroupSnapshotsResult = ctx.element.list_group_snapshots(group_snapshot_id=groupsnapshotid, volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListGroupSnapshotsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifygroup', short_help="""ModifyGroupSnapshot is used to change the attributes currently assigned to a group snapshot. """, cls=SolidFireCommand)
@click.option('--groupsnapshotid',
              type=int,
              required=True,
              help="""ID of the snapshot. """)
@click.option('--expirationtime',
              type=str,
              required=False,
              help="""Use to set the time when the snapshot should be removed. """)
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Use to enable the snapshot created to be replicated to a remote SolidFire cluster. Possible values: true: the snapshot will be replicated to remote storage. false: Default. No replication. """)
@pass_context
def modifygroup(ctx,
           # Mandatory main parameter
           groupsnapshotid,
           # Optional main parameter
           expirationtime = None,
           # Optional main parameter
           enableremotereplication = None):
    """ModifyGroupSnapshot is used to change the attributes currently assigned to a group snapshot."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""groupsnapshotid = """+str(groupsnapshotid)+""";"""+"""expirationtime = """+str(expirationtime)+""";"""+"""enableremotereplication = """+str(enableremotereplication)+""";"""+"")
    try:
        _ModifyGroupSnapshotResult = ctx.element.modify_group_snapshot(group_snapshot_id=groupsnapshotid, expiration_time=expirationtime, enable_remote_replication=enableremotereplication)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyGroupSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""ModifySnapshot is used to change the attributes currently assigned to a snapshot. Use this API method to enable the snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system. """, cls=SolidFireCommand)
@click.option('--snapshotid',
              type=int,
              required=True,
              help="""ID of the snapshot. """)
@click.option('--expirationtime',
              type=str,
              required=False,
              help="""Use to set the time when the snapshot should be removed. """)
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Use to enable the snapshot created to be replicated to a remote SolidFire cluster. Possible values: true: the snapshot will be replicated to remote storage. false: Default. No replication. """)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           snapshotid,
           # Optional main parameter
           expirationtime = None,
           # Optional main parameter
           enableremotereplication = None):
    """ModifySnapshot is used to change the attributes currently assigned to a snapshot."""
    """Use this API method to enable the snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""snapshotid = """+str(snapshotid)+""";"""+"""expirationtime = """+str(expirationtime)+""";"""+"""enableremotereplication = """+str(enableremotereplication)+""";"""+"")
    try:
        _ModifySnapshotResult = ctx.element.modify_snapshot(snapshot_id=snapshotid, expiration_time=expirationtime, enable_remote_replication=enableremotereplication)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifySnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateSnapshot is used to create a point-in-time copy of a volume. A snapshot can be created from any volume or from an existing snapshot.  Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""ID of the volume image from which to copy. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""Unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. If a SnapshotID is not provided, a snapshot is created from the volume's active branch. """)
@click.option('--name',
              type=str,
              required=False,
              help="""A name for the snapshot. If no name is provided, the date and time the snapshot was taken is used. """)
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Identifies if snapshot is enabled for remote replication. """)
@click.option('--retention',
              type=str,
              required=False,
              help="""The amount of time the snapshot will be retained. Enter in HH:mm:ss """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of Name/Value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def create(ctx,
           # Mandatory main parameter
           volumeid,
           # Optional main parameter
           snapshotid = None,
           # Optional main parameter
           name = None,
           # Optional main parameter
           enableremotereplication = None,
           # Optional main parameter
           retention = None,
           # Optional main parameter
           attributes = None):
    """CreateSnapshot is used to create a point-in-time copy of a volume."""
    """A snapshot can be created from any volume or from an existing snapshot."""
    """"""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                        

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""snapshotid = """+str(snapshotid)+""";"""+"""name = """+str(name)+""";"""+"""enableremotereplication = """+str(enableremotereplication)+""";"""+"""retention = """+str(retention)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _CreateSnapshotResult = ctx.element.create_snapshot(volume_id=volumeid, snapshot_id=snapshotid, name=name, enable_remote_replication=enableremotereplication, retention=retention, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListSnapshots is used to return the attributes of each snapshot taken on the volume. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=False,
              help="""The volume to list snapshots for. If not provided, all snapshots for all volumes are returned. """)
@pass_context
def list(ctx,
           # Optional main parameter
           volumeid = None):
    """ListSnapshots is used to return the attributes of each snapshot taken on the volume."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"")
    try:
        _ListSnapshotsResult = ctx.element.list_snapshots(volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListSnapshotsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createschedule', short_help="""CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.  The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created.   Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """)
@click.option('--minutes',
              type=int,
              required=False,
              default=0,
              help="""If provided with hours and days, it suggests (with hours and days) how much time is in between each snapshot. If it is provided with weekdays or monthdays, it suggests the time on which a snapshot will occur. If not provided, defaults to 0.""")
@click.option('--hours',
              type=int,
              required=False,
              default=0,
              help="""If provided with minutes and days, it suggests (with minutes and days) how much time is in between each snapshot. If it is provided with weekdays or monthdays, it suggests the time on which a snapshot will occur.""")
@click.option('--days',
              type=int,
              required=False,
              default=0,
              help="""Indicates the number of days in between each snapshot.""")
@click.option('--weekdays',
              type=str,
              required=False,
              help="""Indicates the weekday on which the snapshot will occur.""")
@click.option('--monthdays',
              type=str,
              required=False,
              help="""Indicates the monthdays on which snapshots will occur..""")
@click.option('--haserror',
              type=bool,
              required=False,
              help="""Indicates whether or not the schedule has errors.""")
@click.option('--paused',
              type=bool,
              required=False,
              help="""Indicates whether or not the schedule is paused.""")
@click.option('--recurring',
              type=bool,
              required=False,
              help="""Indicates whether or not the schedule is recurring.""")
@click.option('--runnextinterval',
              type=bool,
              required=False,
              help="""Indicates whether or not the schedule will run the next time the scheduler is active. When set to "true", the schedule will run the next time the scheduler is active and then reset back to "false".""")
@click.option('--volumeids',
              type=str,
              required=False,
              help="""A list of volume IDs to be included in the group snapshot.""")
@click.option('--snapshotname',
              type=str,
              required=False,
              help="""The snapshot name to be used.""")
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Indicates if the snapshot should be included in remote replication.""")
@click.option('--retention',
              type=str,
              required=False,
              help="""The amount of time the snapshot will be retained in HH:mm:ss.""")
@click.option('--name',
              type=str,
              required=True,
              help="""Unique name assigned to the schedule.""")
@click.option('--startingdate',
              type=str,
              required=False,
              help="""Indicates the date the first time the schedule began of will begin. Formatted in UTC time.""")
@pass_context
def CreateSchedule(ctx,
                   minutes,
                   hours,
                   weekdays,
                   days,
                   monthdays,
                   haserror,
                   paused,
                   recurring,
                   runnextinterval,
                   volumeids,
                   snapshotname,
                   enableremotereplication,
                   retention,
                   name,
                   startingdate):
    """CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval."""
    """"""
    """The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. """
    """"""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()
    if not (
            (minutes is not None and hours is not None and days is not None) or
            (minutes is not None and hours is not None and weekdays is not None) or
            (minutes is not None and hours is not None and monthdays is not None)
    ):
        ctx.logger.error("""You must provide one of the three possible frequency formats:
        Option 1: Provide minutes, hours, and days
        Option 2: Provide minutes, hours, and weekdays
        Option 3: Provide minutes, hours, and monthdays""")
        exit(1)

    # Mandatory parameters:
    if(minutes is not None and hours is not None and days is not None):
        freq = TimeIntervalFrequency(minutes=minutes, hours=hours, days=days)
    if(minutes is not None and hours is not None and weekdays is not None):
        freq = DaysOfWeekFrequency(minutes=minutes, hours=hours, weekdays=weekdays)
    if(minutes is not None and hours is not None and monthdays is not None):
        freq = DaysOfMonthFrequency(minutes=minutes, hours=hours, monthdays=parser.parse_array(monthdays))

    volumeids = parser.parse_array(volumeids)

    scheduleInfo = ScheduleInfo(volume_ids=volumeids, snapshot_name=snapshotname, enable_remote_replication=enableremotereplication, retention=retention)

    schedule = Schedule(frequency=freq, schedule_info=scheduleInfo, name=name, starting_date=startingdate)

    if haserror:
        schedule.has_error = haserror
    if paused:
        schedule.paused = paused
    if recurring:
        schedule.recurring = recurring
    if runnextinterval:
        schedule.run_next_interval = runnextinterval
    _CreateScheduleResult = ctx.element.create_schedule(schedule=schedule)

    ctx.logger.info("""schedule = """+str(schedule)+""";"""+"")
    try:
        _CreateScheduleResult = ctx.element.create_schedule(schedule=schedule)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateScheduleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


@cli.command('deletegroup', short_help="""DeleteGroupSnapshot is used to delete a group snapshot. The saveMembers parameter can be used to preserve all the snapshots that were made for the volumes in the group but the group association will be removed. """, cls=SolidFireCommand)
@click.option('--groupsnapshotid',
              type=int,
              required=True,
              help="""Unique ID of the group snapshot. """)
@click.option('--savemembers',
              type=bool,
              required=True,
              help="""true: Snapshots are kept, but group association is removed. false: The group and snapshots are deleted. """)
@pass_context
def deletegroup(ctx,
           # Mandatory main parameter
           groupsnapshotid,
           # Mandatory main parameter
           savemembers):
    """DeleteGroupSnapshot is used to delete a group snapshot."""
    """The saveMembers parameter can be used to preserve all the snapshots that"""
    """were made for the volumes in the group but the group association will be removed."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

        
    

    ctx.logger.info("""groupsnapshotid = """+str(groupsnapshotid)+""";"""+"""savemembers = """+str(savemembers)+""";"""+"")
    try:
        _DeleteGroupSnapshotResult = ctx.element.delete_group_snapshot(group_snapshot_id=groupsnapshotid, save_members=savemembers)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DeleteGroupSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getschedule', short_help="""GetSchedule is used to return information about a scheduled snapshot that has been created. You can see information about a specified schedule if there are many snapshot schedules in the system. You can include more than one schedule with this method by specifying additional scheduleIDs to the parameter. """, cls=SolidFireCommand)
@click.option('--scheduleid',
              type=int,
              required=True,
              help="""Unique ID of the schedule or multiple schedules to display """)
@pass_context
def getschedule(ctx,
           # Mandatory main parameter
           scheduleid):
    """GetSchedule is used to return information about a scheduled snapshot that has been created. You can see information about a specified schedule if there are many snapshot schedules in the system. You can include more than one schedule with this method by specifying additional scheduleIDs to the parameter."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""scheduleid = """+str(scheduleid)+""";"""+"")
    try:
        _GetScheduleResult = ctx.element.get_schedule(schedule_id=scheduleid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetScheduleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('rollbacktogroup', short_help="""RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots.  Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--groupsnapshotid',
              type=int,
              required=True,
              help="""Unique ID of the group snapshot. """)
@click.option('--savecurrentstate',
              type=bool,
              required=True,
              help="""true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with  "-copy" appended to the end of the name. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of Name/Value pairs in JSON object format  Has the following subparameters: """)
@pass_context
def rollbacktogroup(ctx,
           # Mandatory main parameter
           groupsnapshotid,
           # Mandatory main parameter
           savecurrentstate,
           # Optional main parameter
           name = None,
           # Optional main parameter
           attributes = None):
    """RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots."""
    """"""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""groupsnapshotid = """+str(groupsnapshotid)+""";"""+"""savecurrentstate = """+str(savecurrentstate)+""";"""+"""name = """+str(name)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _CreateGroupSnapshotResult = ctx.element.rollback_to_group_snapshot(group_snapshot_id=groupsnapshotid, save_current_state=savecurrentstate, name=name, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateGroupSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('rollbackto', short_help="""RollbackToSnapshot is used to make an existing snapshot the "active" volume image. This method creates a new  snapshot from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until  it is manually deleted. The previously "active" snapshot is deleted unless the parameter saveCurrentState is set with  a value of "true." Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""VolumeID for the volume. """)
@click.option('--snapshotid',
              type=int,
              required=True,
              help="""ID of a previously created snapshot on the given volume. """)
@click.option('--savecurrentstate',
              type=bool,
              required=True,
              help="""true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with  "-copy" appended to the end of the name. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of Name/Value pairs in JSON object format  Has the following subparameters: """)
@pass_context
def rollbackto(ctx,
           # Mandatory main parameter
           volumeid,
           # Mandatory main parameter
           snapshotid,
           # Mandatory main parameter
           savecurrentstate,
           # Optional main parameter
           name = None,
           # Optional main parameter
           attributes = None):
    """RollbackToSnapshot is used to make an existing snapshot the &quot;active&quot; volume image. This method creates a new """
    """snapshot from an existing snapshot. The new snapshot becomes &quot;active&quot; and the existing snapshot is preserved until """
    """it is manually deleted. The previously &quot;active&quot; snapshot is deleted unless the parameter saveCurrentState is set with """
    """a value of &quot;true.&quot;"""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                    

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""snapshotid = """+str(snapshotid)+""";"""+"""savecurrentstate = """+str(savecurrentstate)+""";"""+"""name = """+str(name)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _CreateSnapshotResult = ctx.element.rollback_to_snapshot(volume_id=volumeid, snapshot_id=snapshotid, save_current_state=savecurrentstate, name=name, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('creategroup', short_help="""CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes. The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created.  Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumes',
              type=str,
              required=True,
              help="""Unique ID of the volume image from which to copy. """)
@click.option('--name',
              type=str,
              required=False,
              help="""A name for the snapshot. If no name is provided, the date and time the snapshot was taken is used. """)
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Identifies if snapshot is enabled for remote replication. """)
@click.option('--retention',
              type=str,
              required=False,
              help="""The amount of time the snapshot will be retained. Enter in HH:mm:ss """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of Name/Value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def creategroup(ctx,
           # Mandatory main parameter
           volumes,
           # Optional main parameter
           name = None,
           # Optional main parameter
           enableremotereplication = None,
           # Optional main parameter
           retention = None,
           # Optional main parameter
           attributes = None):
    """CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes."""
    """The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created."""
    """"""
    """Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    volumes = parser.parse_array(volumes)                

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""volumes = """+str(volumes)+""";"""+"""name = """+str(name)+""";"""+"""enableremotereplication = """+str(enableremotereplication)+""";"""+"""retention = """+str(retention)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _CreateGroupSnapshotResult = ctx.element.create_group_snapshot(volumes=volumes, name=name, enable_remote_replication=enableremotereplication, retention=retention, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateGroupSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


@cli.command('modifyschedule', short_help="""ModifySchedule is used to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention. """)
@click.option('--scheduleid',
              type=int,
              required=True,
              help="""Unique ID of the schedule""")
@click.option('--minutes',
              type=int,
              required=False,
              help="""If provided with hours and days, it suggests (with hours and days) how much time is in between each snapshot. If it is provided with weekdays or monthdays, it suggests the time on which a snapshot will occur.""")
@click.option('--hours',
              type=int,
              required=False,
              help="""If provided with minutes and days, it suggests (with minutes and days) how much time is in between each snapshot. If it is provided with weekdays or monthdays, it suggests the time on which a snapshot will occur.""")
@click.option('--days',
              type=int,
              required=False,
              help="""Indicates the number of days in between each snapshot.""")
@click.option('--weekdays',
              type=str,
              required=False,
              help="""Indicates the weekday on which the snapshot will occur.""")
@click.option('--monthdays',
              type=str,
              required=False,
              help="""Indicates the monthdays on which snapshots will occur..""")
@click.option('--paused',
              type=bool,
              required=False,
              help="""Indicates whether or not the schedule is paused.""")
@click.option('--recurring',
              type=bool,
              required=False,
              help="""Indicates whether or not the schedule is recurring.""")
@click.option('--runnextinterval',
              type=bool,
              required=False,
              help="""Indicates whether or not the schedule will run the next time the scheduler is active. When set to "true", the schedule will run the next time the scheduler is active and then reset back to "false".""")
@click.option('--volumeids',
              type=str,
              required=False,
              help="""A list of volume IDs to be included in the group snapshot.""")
@click.option('--snapshotname',
              type=str,
              required=False,
              help="""The snapshot name to be used.""")
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Indicates if the snapshot should be included in remote replication.""")
@click.option('--retention',
              type=str,
              required=False,
              help="""The amount of time the snapshot will be retained in HH:mm:ss.""")
@click.option('--name',
              type=str,
              required=False,
              help="""Unique name assigned to the schedule.""")
@click.option('--startingdate',
              type=str,
              required=False,
              help="""Indicates the date the first time the schedule began of will begin. Formatted in UTC time.""")
@click.option('--tobedeleted',
              type=bool,
              required=False,
              help="""Indicates if the schedule is marked for deletion.""")
@pass_context
def ModifySchedule(ctx,
                   scheduleid,
                   minutes,
                   hours,
                   weekdays,
                   days,
                   monthdays,
                   paused,
                   recurring,
                   runnextinterval,
                   volumeids,
                   snapshotname,
                   enableremotereplication,
                   retention,
                   name,
                   startingdate,
                   tobedeleted):
    """ModifySchedule is used to modify a schedule that will autonomously make a snapshot of a volume at a defined interval."""
    """"""
    """The snapshot can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. """
    """"""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()
    if (minutes is not None or hours is not None or days is not None or weekdays is not None or monthdays is not None) and not (
            (minutes is not None and hours is not None and days is not None) or
            (minutes is not None and hours is not None and weekdays is not None) or
            (minutes is not None and hours is not None and monthdays is not None)
    ):
        ctx.logger.error("""You must provide one of the three possible frequency formats:
        Option 1: Provide minutes, hours, and days - specifies time in between snapshots
        Option 2: Provide minutes, hours, and weekdays - specifies time to take snapshots
        Option 3: Provide minutes, hours, and monthdays - specifies time to take snapshots""")
        exit(1)

    # Now that we've done our checks, get the specific schedule:
    _GetScheduleResult = ctx.element.get_schedule(schedule_id=scheduleid)
    if _GetScheduleResult.schedule == None:
        ctx.logger.error("The schedule specified by schedule_id does not exist.")
    schedule = _GetScheduleResult.schedule

    # Mandatory parameters:
    freq = None
    if(minutes is not None and hours is not None and days is not None):
        freq = TimeIntervalFrequency(
            minutes=minutes,
            hours=hours,
            days=days
        )
    if(minutes is not None and hours is not None and weekdays is not None):
        freq = DaysOfWeekFrequency(
            minutes=minutes,
            hours=hours,
            weekdays=weekdays
        )
    if(minutes is not None and hours is not None and monthdays is not None):
        freq = DaysOfMonthFrequency(
            minutes=minutes,
            hours=hours,
            monthdays=parser.parse_array(monthdays)
        )
    if freq:
        schedule.frequency = freq
    if volumeids:
        schedule.scheduleInfo.volume_ids = volumeids
    if snapshotname:
        schedule.scheduleInfo.snapshot_name = snapshotname
    if enableremotereplication:
        schedule.scheduleInfo.enable_remote_replication = enableremotereplication
    if retention:
        schedule.scheduleInfo.retention = retention
    if name:
        schedule.name = name
    if startingdate:
        schedule.starting_date = startingdate
    if paused:
        schedule.paused = paused
    if recurring:
        schedule.recurring = recurring
    if runnextinterval:
        schedule.run_next_interval = runnextinterval
    if scheduleid:
        schedule.schedule_id = scheduleid
    if tobedeleted:
        schedule.to_be_deleted = tobedeleted

    ctx.logger.info("""schedule = """+str(schedule)+""";"""+"")
    try:
        _ModifyScheduleResult = ctx.element.modify_schedule(schedule=schedule)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyScheduleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


@cli.command('listschedules', short_help="""ListSchedule is used to return information about all scheduled snapshots that have been created. """, cls=SolidFireCommand)
@pass_context
def listschedules(ctx):
    """ListSchedule is used to return information about all scheduled snapshots that have been created."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListSchedulesResult = ctx.element.list_schedules()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListSchedulesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""DeleteSnapshot is used to delete a snapshot. A snapshot that is currently the "active" snapshot cannot be deleted. You must rollback and make another snapshot "active" before the current snapshot can be deleted. To rollback a snapshot, use RollbackToSnapshot. """, cls=SolidFireCommand)
@click.option('--snapshotid',
              type=int,
              required=True,
              help="""The ID of the snapshot to delete. """)
@pass_context
def delete(ctx,
           # Mandatory main parameter
           snapshotid):
    """DeleteSnapshot is used to delete a snapshot."""
    """A snapshot that is currently the &quot;active&quot; snapshot cannot be deleted."""
    """You must rollback and make another snapshot &quot;active&quot; before the current snapshot can be deleted."""
    """To rollback a snapshot, use RollbackToSnapshot."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""snapshotid = """+str(snapshotid)+""";"""+"")
    try:
        _DeleteSnapshotResult = ctx.element.delete_snapshot(snapshot_id=snapshotid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DeleteSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

