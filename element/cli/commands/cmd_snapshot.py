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
    """deletegroup listgroup modify listschedules rollbacktogroup getschedule rollbackto modifyschedule createschedule creategroup list modifygroup create delete """

@cli.command('deletegroup', short_help="""DeleteGroupSnapshot enables you to delete a group snapshot. You can use the saveMembers parameter to preserve all the snapshots that were made for the volumes in the group, but the group association is removed. """, cls=SolidFireCommand)
@click.option('--groupsnapshotid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the unique ID of the group snapshot. """)
@click.option('--savemembers',
              type=bool,
              required=True,
              prompt=True,
              help="""Specifies whether to preserve snapshots or delete them. Valid values are: true: Snapshots are preserved, but group association is removed. false: The group and snapshots are deleted. """)
@pass_context
def deletegroup(ctx,
           # Mandatory main parameter
           groupsnapshotid,
           # Mandatory main parameter
           savemembers):
    """DeleteGroupSnapshot enables you to delete a group snapshot. You can use the saveMembers parameter to preserve all the snapshots that were made for the volumes in the group, but the group association is removed."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""groupsnapshotid = """ + str(groupsnapshotid)+";"+"""savemembers = """ + str(savemembers)+""";"""+"")
    try:
        _DeleteGroupSnapshotResult = ctx.element.delete_group_snapshot(group_snapshot_id=groupsnapshotid, save_members=savemembers)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteGroupSnapshotResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteGroupSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listgroup', short_help="""ListGroupSnapshots enables you to get information about all group snapshots that have been created. """, cls=SolidFireCommand)
@click.option('--volumes',
              type=str,
              required=False,
              help="""An array of unique volume IDs to query. If you do not specify this parameter, all group snapshots on the cluster are included. """)
@click.option('--groupsnapshotid',
              type=int,
              required=False,
              help="""Retrieves information for a specific group snapshot ID. """)
@pass_context
def listgroup(ctx,
           # Optional main parameter
           volumes = None,
           # Optional main parameter
           groupsnapshotid = None):
    """ListGroupSnapshots enables you to get information about all group snapshots that have been created."""

    

    cli_utils.establish_connection(ctx)
    

    volumes = parser.parse_array(volumes)
    
    

    ctx.logger.info(""": """"""volumes = """+str(volumes)+";" + """groupsnapshotid = """+str(groupsnapshotid)+""";"""+"")
    try:
        _ListGroupSnapshotsResult = ctx.element.list_group_snapshots(volumes=volumes, group_snapshot_id=groupsnapshotid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListGroupSnapshotsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListGroupSnapshotsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""ModifySnapshot enables you to change the attributes currently assigned to a snapshot. You can use this method to enable snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system. """, cls=SolidFireCommand)
@click.option('--snapshotid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the ID of the snapshot. """)
@click.option('--expirationtime',
              type=str,
              required=False,
              help="""Sets the time when the snapshot should be removed. """)
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. """)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           snapshotid,
           # Optional main parameter
           expirationtime = None,
           # Optional main parameter
           enableremotereplication = None):
    """ModifySnapshot enables you to change the attributes currently assigned to a snapshot. You can use this method to enable snapshots created on"""
    """the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    ctx.logger.info(""": """"""snapshotid = """ + str(snapshotid)+";" + """expirationtime = """+str(expirationtime)+";" + """enableremotereplication = """+str(enableremotereplication)+""";"""+"")
    try:
        _ModifySnapshotResult = ctx.element.modify_snapshot(snapshot_id=snapshotid, expiration_time=expirationtime, enable_remote_replication=enableremotereplication)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifySnapshotResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifySnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listschedules', short_help="""ListSchedule enables you to retrieve information about all scheduled snapshots that have been created. """, cls=SolidFireCommand)
@pass_context
def listschedules(ctx):
    """ListSchedule enables you to retrieve information about all scheduled snapshots that have been created."""

    
    if ctx.json is True:
        ctx.logger.error("This command does not support the -j field. If you really need it, use sfapi invoke.")
        exit(1)

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListSchedulesResult = ctx.element.list_schedules()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSchedulesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSchedulesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('rollbacktogroup', short_help="""RollbackToGroupSnapshot enables you to roll back all individual volumes in a snapshot group to each volume's individual snapshot. Note: Rolling back to a group snapshot creates a temporary snapshot of each volume within the group snapshot. Snapshots are allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--groupsnapshotid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the unique ID of the group snapshot. """)
@click.option('--savecurrentstate',
              type=bool,
              required=True,
              prompt=True,
              help="""Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the group snapshot of the volume's current state that is created if "saveCurrentState" is set to true. If you do not give a name, the name of the snapshots (group and individual volume) are set to a timestamp of the time that the rollback occurred. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
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
    """RollbackToGroupSnapshot enables you to roll back all individual volumes in a snapshot group to each volume's individual snapshot."""
    """Note: Rolling back to a group snapshot creates a temporary snapshot of each volume within the group snapshot."""
    """Snapshots are allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""groupsnapshotid = """ + str(groupsnapshotid)+";"+"""savecurrentstate = """ + str(savecurrentstate)+";" + """name = """+str(name)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _RollbackToGroupSnapshotResult = ctx.element.rollback_to_group_snapshot(group_snapshot_id=groupsnapshotid, save_current_state=savecurrentstate, name=name, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RollbackToGroupSnapshotResult), indent=4))
        return
    else:
        cli_utils.print_result(_RollbackToGroupSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getschedule', short_help="""You can use the GetSchedule method to retrieve information about a scheduled snapshot. You can see information about a specific schedule if there are many snapshot schedules in the system. You also retrieve information about more than one schedule with this method by specifying additional scheduleIDs in the parameter. """, cls=SolidFireCommand)
@click.option('--scheduleid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the unique ID of the schedule or multiple schedules to display. """)
@pass_context
def getschedule(ctx,
           # Mandatory main parameter
           scheduleid):
    """You can use the GetSchedule method to retrieve information about a scheduled snapshot. You can see information about a specific"""
    """schedule if there are many snapshot schedules in the system. You also retrieve information about more than one schedule with this"""
    """method by specifying additional scheduleIDs in the parameter."""

    
    if ctx.json is True:
        ctx.logger.error("This command does not support the -j field. If you really need it, use sfapi invoke.")
        exit(1)

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""scheduleid = """ + str(scheduleid)+""";"""+"")
    try:
        _GetScheduleResult = ctx.element.get_schedule(schedule_id=scheduleid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetScheduleResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetScheduleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('rollbackto', short_help="""RollbackToSnapshot enables you to make an existing snapshot of the "active" volume image. This method creates a new snapshot from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until you delete it. The previously "active" snapshot is deleted unless you set the parameter saveCurrentState to true. Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""VolumeID for the volume. """)
@click.option('--snapshotid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of a previously created snapshot on the given volume. """)
@click.option('--savecurrentstate',
              type=bool,
              required=True,
              prompt=True,
              help="""Specifies whether to save an active volume image or delete it. Values are: true: The previous active volume image is kept. false: (default) The previous active volume image is deleted. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the snapshot. If unspecified, the name of the snapshot being rolled back to is used with "- copy" appended to the end of the name. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
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
    """RollbackToSnapshot enables you to make an existing snapshot of the "active" volume image. This method creates a new snapshot"""
    """from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until you delete it."""
    """The previously "active" snapshot is deleted unless you set the parameter saveCurrentState to true."""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is"""
    """at stage 4 or 5."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""volumeid = """ + str(volumeid)+";"+"""snapshotid = """ + str(snapshotid)+";"+"""savecurrentstate = """ + str(savecurrentstate)+";" + """name = """+str(name)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _RollbackToSnapshotResult = ctx.element.rollback_to_snapshot(volume_id=volumeid, snapshot_id=snapshotid, save_current_state=savecurrentstate, name=name, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RollbackToSnapshotResult), indent=4))
        return
    else:
        cli_utils.print_result(_RollbackToSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)


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
    cli_utils.establish_connection(ctx)

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
    try:
        _GetScheduleResult = ctx.element.get_schedule(schedule_id=scheduleid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    if _GetScheduleResult.schedule == None:
        ctx.logger.error("The schedule specified by schedule_id does not exist.")
    schedule = _GetScheduleResult.schedule

    # Mandatory parameters:
    freq = None
    weekdayStringArray = parser.parse_array(weekdays)

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
            weekdays=[Weekday.from_name(name) for name in weekdayStringArray]
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
        schedule.schedule_info.volume_ids = parser.parse_array(volumeids)
    if snapshotname:
        schedule.schedule_info.snapshot_name = snapshotname
    if enableremotereplication:
        schedule.schedule_info.enable_remote_replication = enableremotereplication
    if retention:
        schedule.schedule_info.retention = retention
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
    cli_utils.establish_connection(ctx)

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
    weekdayStringArray = parser.parse_array(weekdays)
    if(minutes is not None and hours is not None and days is not None):
        freq = TimeIntervalFrequency(minutes=minutes, hours=hours, days=days)
    if(minutes is not None and hours is not None and weekdays is not None):
        freq = DaysOfWeekFrequency(minutes=minutes, hours=hours, weekdays=[Weekday.from_name(name) for name in weekdayStringArray])
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


@cli.command('creategroup', short_help="""CreateGroupSnapshot enables you to create a point-in-time copy of a group of volumes. You can use this snapshot later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time that you created the snapshot. Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumes',
              type=str,
              required=True,
              prompt=True,
              help="""Unique ID of the volume image from which to copy. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the group snapshot. If unspecified, the date and time the group snapshot was taken is used. """)
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Replicates the snapshot created to remote storage. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. """)
@click.option('--retention',
              type=str,
              required=False,
              help="""Specifies the amount of time for which the snapshots are retained. The format is HH:mm:ss. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
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
    """CreateGroupSnapshot enables you to create a point-in-time copy of a group of volumes. You can use this snapshot later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time that you created the snapshot."""
    """Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5."""

    

    cli_utils.establish_connection(ctx)
    

    volumes = parser.parse_array(volumes)
    
    
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""volumes = """ + str(volumes)+";" + """name = """+str(name)+";" + """enableremotereplication = """+str(enableremotereplication)+";" + """retention = """+str(retention)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _CreateGroupSnapshotResult = ctx.element.create_group_snapshot(volumes=volumes, name=name, enable_remote_replication=enableremotereplication, retention=retention, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateGroupSnapshotResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateGroupSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListSnapshots enables you to return the attributes of each snapshot taken on the volume. Information about snapshots that reside on the target cluster is displayed on the source cluster when this method is called from the source cluster. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=False,
              help="""Retrieves snapshots for a volume. If volumeID is not provided, all snapshots for all volumes are returned. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""Retrieves information for a specific snapshot ID. """)
@pass_context
def list(ctx,
           # Optional main parameter
           volumeid = None,
           # Optional main parameter
           snapshotid = None):
    """ListSnapshots enables you to return the attributes of each snapshot taken on the volume. Information about snapshots that reside on the target cluster is displayed on the source cluster when this method is called from the source cluster."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""volumeid = """+str(volumeid)+";" + """snapshotid = """+str(snapshotid)+""";"""+"")
    try:
        _ListSnapshotsResult = ctx.element.list_snapshots(volume_id=volumeid, snapshot_id=snapshotid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapshotsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapshotsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifygroup', short_help="""ModifyGroupSnapshot enables you to change the attributes of a group of snapshots. You can also use this method to enable snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system. """, cls=SolidFireCommand)
@click.option('--groupsnapshotid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the ID of the group of snapshots. """)
@click.option('--expirationtime',
              type=str,
              required=False,
              help="""Sets the time when the snapshot should be removed. If unspecified, the current time is used. """)
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. """)
@pass_context
def modifygroup(ctx,
           # Mandatory main parameter
           groupsnapshotid,
           # Optional main parameter
           expirationtime = None,
           # Optional main parameter
           enableremotereplication = None):
    """ModifyGroupSnapshot enables you to change the attributes of a group of snapshots. You can also use this method to enable snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    ctx.logger.info(""": """"""groupsnapshotid = """ + str(groupsnapshotid)+";" + """expirationtime = """+str(expirationtime)+";" + """enableremotereplication = """+str(enableremotereplication)+""";"""+"")
    try:
        _ModifyGroupSnapshotResult = ctx.element.modify_group_snapshot(group_snapshot_id=groupsnapshotid, expiration_time=expirationtime, enable_remote_replication=enableremotereplication)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyGroupSnapshotResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyGroupSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateSnapshot enables you to create a point-in-time copy of a volume. You can create a snapshot from any volume or from an existing snapshot. If you do not provide a SnapshotID with this API method, a snapshot is created from the volume's active branch. If the volume from which the snapshot is created is being replicated to a remote cluster, the snapshot can also be replicated to the same target. Use the enableRemoteReplication parameter to enable snapshot replication. Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the unique ID of the volume image from which to copy. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""Specifies the unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Specifies a name for the snapshot. If unspecified, the date and time the snapshot was taken is used. """)
@click.option('--enableremotereplication',
              type=bool,
              required=False,
              help="""Replicates the snapshot created to a remote cluster. Possible values are: true: The snapshot is replicated to remote storage. false: Default. The snapshot is not replicated. """)
@click.option('--retention',
              type=str,
              required=False,
              help="""Specifies the amount of time for which the snapshot is retained. The format is HH:mm:ss. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
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
    """CreateSnapshot enables you to create a point-in-time copy of a volume. You can create a snapshot from any volume or from an existing snapshot. If you do not provide a SnapshotID with this API method, a snapshot is created from the volume's active branch."""
    """If the volume from which the snapshot is created is being replicated to a remote cluster, the snapshot can also be replicated to the same target. Use the enableRemoteReplication parameter to enable snapshot replication."""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""volumeid = """ + str(volumeid)+";" + """snapshotid = """+str(snapshotid)+";" + """name = """+str(name)+";" + """enableremotereplication = """+str(enableremotereplication)+";" + """retention = """+str(retention)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _CreateSnapshotResult = ctx.element.create_snapshot(volume_id=volumeid, snapshot_id=snapshotid, name=name, enable_remote_replication=enableremotereplication, retention=retention, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateSnapshotResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""DeleteSnapshot enables you to delete a snapshot. A snapshot that is currently the "active" snapshot cannot be deleted. You must rollback and make another snapshot "active" before the current snapshot can be deleted. For more details on rolling back snapshots, see RollbackToSnapshot. """, cls=SolidFireCommand)
@click.option('--snapshotid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the snapshot to be deleted. """)
@pass_context
def delete(ctx,
           # Mandatory main parameter
           snapshotid):
    """DeleteSnapshot enables you to delete a snapshot. A snapshot that is currently the "active" snapshot cannot be deleted. You must"""
    """rollback and make another snapshot "active" before the current snapshot can be deleted. For more details on rolling back snapshots, see RollbackToSnapshot."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""snapshotid = """ + str(snapshotid)+""";"""+"")
    try:
        _DeleteSnapshotResult = ctx.element.delete_snapshot(snapshot_id=snapshotid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteSnapshotResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

