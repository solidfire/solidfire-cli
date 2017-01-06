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
from solidfire.models import *
from uuid import UUID
from element import exceptions


@click.group()
@pass_context
def cli(ctx):
    """ListGroup ModifyGroup Modify Create List CreateSchedule DeleteGroup GetSchedule RollbackToGroup RollbackTo CreateGroup ModifySchedule ListSchedules Delete """

@cli.command('ListGroup', short_help="""ListGroupSnapshots is used to return information about all group snapshots that have been created. """)
@click.option('--volume_id',
              type=int,
              required=False,
              help="""An array of unique volume IDs to query. If this parameter is not specified, all group snapshots on the cluster will be included. """)
@pass_context
def ListGroup(ctx,
           volume_id = None):
    """ListGroupSnapshots is used to return information about all group snapshots that have been created."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListGroupSnapshotsResult = ctx.element.list_group_snapshots(volume_id=volume_id)
    cli_utils.print_result(ListGroupSnapshotsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ModifyGroup', short_help="""ModifyGroupSnapshot is used to change the attributes currently assigned to a group snapshot. """)
@click.option('--group_snapshot_id',
              type=int,
              required=True,
              help="""ID of the snapshot. """)
@click.option('--expiration_time',
              type=str,
              required=False,
              help="""Use to set the time when the snapshot should be removed. """)
@click.option('--enable_remote_replication',
              type=bool,
              required=False,
              help="""Use to enable the snapshot created to be replicated to a remote SolidFire cluster. Possible values: <br/><b>true</b>: the snapshot will be replicated to remote storage. <br/><b>false</b>: Default. No replication. """)
@pass_context
def ModifyGroup(ctx,
           group_snapshot_id,
           expiration_time = None,
           enable_remote_replication = None):
    """ModifyGroupSnapshot is used to change the attributes currently assigned to a group snapshot."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ModifyGroupSnapshotResult = ctx.element.modify_group_snapshot(group_snapshot_id=group_snapshot_id, expiration_time=expiration_time, enable_remote_replication=enable_remote_replication)
    cli_utils.print_result(ModifyGroupSnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Modify', short_help="""ModifySnapshot is used to change the attributes currently assigned to a snapshot. Use this API method to enable the snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system. """)
@click.option('--snapshot_id',
              type=int,
              required=True,
              help="""ID of the snapshot. """)
@click.option('--expiration_time',
              type=str,
              required=False,
              help="""Use to set the time when the snapshot should be removed. """)
@click.option('--enable_remote_replication',
              type=bool,
              required=False,
              help="""Use to enable the snapshot created to be replicated to a remote SolidFire cluster. Possible values: <br/><b>true</b>: the snapshot will be replicated to remote storage. <br/><b>false</b>: Default. No replication. """)
@pass_context
def Modify(ctx,
           snapshot_id,
           expiration_time = None,
           enable_remote_replication = None):
    """ModifySnapshot is used to change the attributes currently assigned to a snapshot."""
    """Use this API method to enable the snapshots created on the Read/Write (source) volume to be remotely replicated to a target SolidFire storage system."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ModifySnapshotResult = ctx.element.modify_snapshot(snapshot_id=snapshot_id, expiration_time=expiration_time, enable_remote_replication=enable_remote_replication)
    cli_utils.print_result(ModifySnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Create', short_help="""CreateSnapshot is used to create a point-in-time copy of a volume. A snapshot can be created from any volume or from an existing snapshot.  Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""ID of the volume image from which to copy. """)
@click.option('--snapshot_id',
              type=int,
              required=False,
              help="""Unique ID of a snapshot from which the new snapshot is made. The snapshotID passed must be a snapshot on the given volume. If a SnapshotID is not provided, a snapshot is created from the volume's active branch. """)
@click.option('--name',
              type=str,
              required=False,
              help="""A name for the snapshot. If no name is provided, the date and time the snapshot was taken is used. """)
@click.option('--enable_remote_replication',
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
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Create(ctx,
           volume_id,
           snapshot_id = None,
           name = None,
           enable_remote_replication = None,
           retention = None,
           attributes = None):
    """CreateSnapshot is used to create a point-in-time copy of a volume."""
    """A snapshot can be created from any volume or from an existing snapshot."""
    """"""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    CreateSnapshotResult = ctx.element.create_snapshot(volume_id=volume_id, snapshot_id=snapshot_id, name=name, enable_remote_replication=enable_remote_replication, retention=retention, attributes=attributes)
    cli_utils.print_result(CreateSnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""ListSnapshots is used to return the attributes of each snapshot taken on the volume. """)
@click.option('--volume_id',
              type=int,
              required=False,
              help="""The volume to list snapshots for. If not provided, all snapshots for all volumes are returned. """)
@pass_context
def List(ctx,
           volume_id = None):
    """ListSnapshots is used to return the attributes of each snapshot taken on the volume."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListSnapshotsResult = ctx.element.list_snapshots(volume_id=volume_id)
    cli_utils.print_result(ListSnapshotsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CreateSchedule', short_help="""CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval.  The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created.   Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """)
@click.option('--schedule',
              type=str,
              required=True,
              help="""Provide in json format: The "Schedule" object will be used to create a new schedule.<br/> Do not set ScheduleID property, it will be ignored.<br/> Frequency property must be of type that inherits from Frequency. Valid types are:<br/> DaysOfMonthFrequency<br/> DaysOrWeekFrequency<br/> TimeIntervalFrequency """)
@pass_context
def CreateSchedule(ctx,
           schedule):
    """CreateSchedule is used to create a schedule that will autonomously make a snapshot of a volume at a defined interval."""
    """"""
    """The snapshot created can be used later as a backup or rollback to ensure the data on a volume or group of volumes is consistent for the point in time in which the snapshot was created. """
    """"""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(schedule is not None):
        kwargsDict = simplejson.loads(schedule)
        schedule = Schedule(**kwargsDict)

    CreateScheduleResult = ctx.element.create_schedule(schedule=schedule)
    cli_utils.print_result(CreateScheduleResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('DeleteGroup', short_help="""DeleteGroupSnapshot is used to delete a group snapshot. The saveMembers parameter can be used to preserve all the snapshots that were made for the volumes in the group but the group association will be removed. """)
@click.option('--group_snapshot_id',
              type=int,
              required=True,
              help="""Unique ID of the group snapshot. """)
@click.option('--save_members',
              type=bool,
              required=True,
              help="""<br/><b>true</b>: Snapshots are kept, but group association is removed. <br/><b>false</b>: The group and snapshots are deleted. """)
@pass_context
def DeleteGroup(ctx,
           group_snapshot_id,
           save_members):
    """DeleteGroupSnapshot is used to delete a group snapshot."""
    """The saveMembers parameter can be used to preserve all the snapshots that"""
    """were made for the volumes in the group but the group association will be removed."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    DeleteGroupSnapshotResult = ctx.element.delete_group_snapshot(group_snapshot_id=group_snapshot_id, save_members=save_members)
    cli_utils.print_result(DeleteGroupSnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetSchedule', short_help="""GetSchedule is used to return information about a scheduled snapshot that has been created. You can see information about a specified schedule if there are many snapshot schedules in the system. You can include more than one schedule with this method by specifying additional scheduleIDs to the parameter. """)
@click.option('--schedule_id',
              type=int,
              required=True,
              help="""Unique ID of the schedule or multiple schedules to display """)
@pass_context
def GetSchedule(ctx,
           schedule_id):
    """GetSchedule is used to return information about a scheduled snapshot that has been created. You can see information about a specified schedule if there are many snapshot schedules in the system. You can include more than one schedule with this method by specifying additional scheduleIDs to the parameter."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetScheduleResult = ctx.element.get_schedule(schedule_id=schedule_id)
    cli_utils.print_result(GetScheduleResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RollbackToGroup', short_help="""RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots.  Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """)
@click.option('--group_snapshot_id',
              type=int,
              required=True,
              help="""Unique ID of the group snapshot. """)
@click.option('--save_current_state',
              type=bool,
              required=True,
              help="""<br/><b>true</b>: The previous active volume image is kept. <br/><b>false</b>: (default) The previous active volume image is deleted. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with  "-copy" appended to the end of the name. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format """)
@pass_context
def RollbackToGroup(ctx,
           group_snapshot_id,
           save_current_state,
           name = None,
           attributes = None):
    """RollbackToGroupSnapshot is used to roll back each individual volume in a snapshot group to a copy of their individual snapshots."""
    """"""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    CreateGroupSnapshotResult = ctx.element.rollback_to_group_snapshot(group_snapshot_id=group_snapshot_id, save_current_state=save_current_state, name=name, attributes=attributes)
    cli_utils.print_result(CreateGroupSnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RollbackTo', short_help="""RollbackToSnapshot is used to make an existing snapshot the "active" volume image. This method creates a new  snapshot from an existing snapshot. The new snapshot becomes "active" and the existing snapshot is preserved until  it is manually deleted. The previously "active" snapshot is deleted unless the parameter saveCurrentState is set with  a value of "true." Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""VolumeID for the volume. """)
@click.option('--snapshot_id',
              type=int,
              required=True,
              help="""ID of a previously created snapshot on the given volume. """)
@click.option('--save_current_state',
              type=bool,
              required=True,
              help="""<br/><b>true</b>: The previous active volume image is kept. <br/><b>false</b>: (default) The previous active volume image is deleted. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the snapshot. If no name is given, then the name of the snapshot being rolled back to is used with  "-copy" appended to the end of the name. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format """)
@pass_context
def RollbackTo(ctx,
           volume_id,
           snapshot_id,
           save_current_state,
           name = None,
           attributes = None):
    """RollbackToSnapshot is used to make an existing snapshot the &quot;active&quot; volume image. This method creates a new """
    """snapshot from an existing snapshot. The new snapshot becomes &quot;active&quot; and the existing snapshot is preserved until """
    """it is manually deleted. The previously &quot;active&quot; snapshot is deleted unless the parameter saveCurrentState is set with """
    """a value of &quot;true.&quot;"""
    """Note: Creating a snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    CreateSnapshotResult = ctx.element.rollback_to_snapshot(volume_id=volume_id, snapshot_id=snapshot_id, save_current_state=save_current_state, name=name, attributes=attributes)
    cli_utils.print_result(CreateSnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CreateGroup', short_help="""CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes. The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created.  Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """)
@click.option('--volumes',
              type=str,
              required=True,
              help="""Unique ID of the volume image from which to copy. """)
@click.option('--name',
              type=str,
              required=False,
              help="""A name for the snapshot. If no name is provided, the date and time the snapshot was taken is used. """)
@click.option('--enable_remote_replication',
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
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def CreateGroup(ctx,
           volumes,
           name = None,
           enable_remote_replication = None,
           retention = None,
           attributes = None):
    """CreateGroupSnapshot is used to create a point-in-time copy of a group of volumes."""
    """The snapshot created can then be used later as a backup or rollback to ensure the data on the group of volumes is consistent for the point in time in which the snapshot was created."""
    """"""
    """Note: Creating a group snapshot is allowed if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    volumes = parser.parse_array(volumes)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    CreateGroupSnapshotResult = ctx.element.create_group_snapshot(volumes=volumes, name=name, enable_remote_replication=enable_remote_replication, retention=retention, attributes=attributes)
    cli_utils.print_result(CreateGroupSnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ModifySchedule', short_help="""ModifySchedule is used to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention. """)
@click.option('--schedule',
              type=str,
              required=True,
              help="""Provide in json format: The "Schedule" object will be used to modify an existing schedule.<br/> The ScheduleID property is required.<br/> Frequency property must be of type that inherits from Frequency. Valid types are:<br/> DaysOfMonthFrequency<br/> DaysOrWeekFrequency<br/> TimeIntervalFrequency """)
@pass_context
def ModifySchedule(ctx,
           schedule):
    """ModifySchedule is used to change the intervals at which a scheduled snapshot occurs. This allows for adjustment to the snapshot frequency and retention."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(schedule is not None):
        kwargsDict = simplejson.loads(schedule)
        schedule = Schedule(**kwargsDict)

    ModifyScheduleResult = ctx.element.modify_schedule(schedule=schedule)
    cli_utils.print_result(ModifyScheduleResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListSchedules', short_help="""ListSchedule is used to return information about all scheduled snapshots that have been created. """)
@pass_context
def ListSchedules(ctx):
    """ListSchedule is used to return information about all scheduled snapshots that have been created."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListSchedulesResult = ctx.element.list_schedules()
    cli_utils.print_result(ListSchedulesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Delete', short_help="""DeleteSnapshot is used to delete a snapshot. A snapshot that is currently the "active" snapshot cannot be deleted. You must rollback and make another snapshot "active" before the current snapshot can be deleted. To rollback a snapshot, use RollbackToSnapshot. """)
@click.option('--snapshot_id',
              type=int,
              required=True,
              help="""The ID of the snapshot to delete. """)
@pass_context
def Delete(ctx,
           snapshot_id):
    """DeleteSnapshot is used to delete a snapshot."""
    """A snapshot that is currently the &quot;active&quot; snapshot cannot be deleted."""
    """You must rollback and make another snapshot &quot;active&quot; before the current snapshot can be deleted."""
    """To rollback a snapshot, use RollbackToSnapshot."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    DeleteSnapshotResult = ctx.element.delete_snapshot(snapshot_id=snapshot_id)
    cli_utils.print_result(DeleteSnapshotResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

