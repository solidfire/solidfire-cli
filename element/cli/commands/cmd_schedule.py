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
    """modify create list get """
@cli.command('modify', short_help="""ModifySchedule is used to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention. """)
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
def modify(ctx,
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

    if ctx.json is True:
        ctx.logger.error("This command does not support the -j field. If you really need it, use sfapi invoke.")
        exit(1)

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
    if enableremotereplication is not None:
        schedule.schedule_info.enable_remote_replication = enableremotereplication
    if retention:
        schedule.schedule_info.retention = retention
    if name:
        schedule.name = name
    if startingdate:
        schedule.starting_date = startingdate
    if paused is not None:
        schedule.paused = paused
    if recurring is not None:
        schedule.recurring = recurring
    if runnextinterval is not None:
        schedule.run_next_interval = runnextinterval
    if scheduleid:
        schedule.schedule_id = scheduleid
    if tobedeleted is not None:
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


@cli.command('create', short_help="""CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.  The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created.   Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """)
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
def create(ctx,
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

    if paused is not None:
        schedule.paused = paused
    if recurring is not None:
        schedule.recurring = recurring
    if runnextinterval is not None:
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


@cli.command('list', short_help="""ListSchedule enables you to retrieve information about all scheduled snapshots that have been created. """, cls=SolidFireCommand)
@pass_context
def list(ctx):
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



@cli.command('get', short_help="""You can use the GetSchedule method to retrieve information about a scheduled snapshot. You can see information about a specific schedule if there are many snapshot schedules in the system. You also retrieve information about more than one schedule with this method by specifying additional scheduleIDs in the parameter. """, cls=SolidFireCommand)
@click.option('--scheduleid',
              type=int,
              required=True,
              prompt=True,
              help="""Specifies the unique ID of the schedule or multiple schedules to display. """)
@pass_context
def get(ctx,
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

