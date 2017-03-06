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
    """getefficiency liststatsbyaccount startbulkwrite updatebulkstatus startbulkread listdeleted purgedeleted liststatsby create cancelclone getdefaultqos getasyncresult listasyncresults liststatsbyaccessgroup listbulkjobs clone modify restoredeleted copy listactive list clonemultiple setdefaultqos getstats listforaccount getcount cancelgroupclone delete """

@cli.command('getefficiency', short_help="""GetVolumeEfficiency is used to retrieve information about a volume. Only the volume given as a parameter in this API method is used to compute the capacity. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""Specifies the volume for which capacity is computed. """)
@pass_context
def getefficiency(ctx,
           # Mandatory main parameter
           volumeid):
    """GetVolumeEfficiency is used to retrieve information about a volume."""
    """Only the volume given as a parameter in this API method is used to compute the capacity."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"")
    try:
        _GetVolumeEfficiencyResult = ctx.element.get_volume_efficiency(volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetVolumeEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('liststatsbyaccount', short_help="""ListVolumeStatsByAccount returns high-level activity measurements for every account. Values are summed from all the volumes owned by the account. """, cls=SolidFireCommand)
@pass_context
def liststatsbyaccount(ctx):
    """ListVolumeStatsByAccount returns high-level activity measurements for every account."""
    """Values are summed from all the volumes owned by the account."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListVolumeStatsByAccountResult = ctx.element.list_volume_stats_by_account()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumeStatsByAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('startbulkwrite', short_help="""StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When the session is initialized, data can be written to a SolidFire storage volume from an external backup source. The external data is accessed by a web server running on a SolidFire node. Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""ID of the volume to be written to. """)
@click.option('--format',
              type=str,
              required=True,
              help="""The format of the volume data. Can be either: uncompressed: every byte of the volume is returned without any compression. native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write """)
@click.option('--script',
              type=str,
              required=False,
              help="""Executable name of a script. If no script name is given then the key and URL are necessary to access SolidFire nodes. The script runs on the primary node and the key and URL is returned to the script so the local web server can be contacted. """)
@click.option('--scriptparameters',
              type=str,
              required=False,
              help="""JSON parameters to pass to the script.  Has the following subparameters: """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""JSON attributes for the bulk volume job.  Has the following subparameters: """)
@pass_context
def startbulkwrite(ctx,
           # Mandatory main parameter
           volumeid,
           # Mandatory main parameter
           format,
           # Optional main parameter
           script = None,
           # Optional main parameter
           scriptparameters = None,
           # Optional main parameter
           attributes = None):
    """StartBulkVolumeWrite allows you to initialize a bulk volume write session on a specified volume."""
    """Only two bulk volume processes can run simultaneously on a volume."""
    """When the session is initialized, data can be written to a SolidFire storage volume from an external backup source."""
    """The external data is accessed by a web server running on a SolidFire node."""
    """Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                

    kwargsDict = None

    if(scriptparameters is not None):
        try:
            kwargsDict = simplejson.loads(scriptparameters)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)    

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""format = """+str(format)+""";"""+"""script = """+str(script)+""";"""+"""scriptparameters = """+str(scriptparameters)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _StartBulkVolumeWriteResult = ctx.element.start_bulk_volume_write(volume_id=volumeid, format=format, script=script, script_parameters=kwargsDict, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_StartBulkVolumeWriteResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('updatebulkstatus', short_help="""You can use UpdateBulkVolumeStatus in a script to return to the SolidFire system the status of a bulk volume job that you have started with the "StartBulkVolumeRead" or "StartBulkVolumeWrite" methods. """, cls=SolidFireCommand)
@click.option('--key',
              type=str,
              required=True,
              help="""The key assigned during initialization of a "StartBulkVolumeRead" or "StartBulkVolumeWrite" session. """)
@click.option('--status',
              type=str,
              required=True,
              help="""The SolidFire system sets the status of the given bulk volume job. Possible values: running: jobs that are still active. complete: jobs that are done. failed - jobs that have failed. failed: jobs that have failed. """)
@click.option('--percentcomplete',
              type=str,
              required=False,
              help="""The completed progress of the bulk volume job as a percentage. """)
@click.option('--message',
              type=str,
              required=False,
              help="""Returns the status of the bulk volume job when the job has completed. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""JSON attributes  updates what is on the bulk volume job.  Has the following subparameters: """)
@pass_context
def updatebulkstatus(ctx,
           # Mandatory main parameter
           key,
           # Mandatory main parameter
           status,
           # Optional main parameter
           percentcomplete = None,
           # Optional main parameter
           message = None,
           # Optional main parameter
           attributes = None):
    """You can use UpdateBulkVolumeStatus in a script to return to the SolidFire system the status of a bulk volume job that you have started with the &quot;StartBulkVolumeRead&quot; or &quot;StartBulkVolumeWrite&quot; methods."""
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
    

    ctx.logger.info("""key = """+str(key)+""";"""+"""status = """+str(status)+""";"""+"""percentcomplete = """+str(percentcomplete)+""";"""+"""message = """+str(message)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _UpdateBulkVolumeStatusResult = ctx.element.update_bulk_volume_status(key=key, status=status, percent_complete=percentcomplete, message=message, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_UpdateBulkVolumeStatusResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('startbulkread', short_help="""StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source. The external data is accessed by a web server running on a SolidFire node. Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system.  At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed. You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter. Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes.  Note: This process creates a new snapshot if the ID of an existing snapshot is not provided. Snapshots can be created if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""ID of the volume to be read. """)
@click.option('--format',
              type=str,
              required=True,
              help="""The format of the volume data. Can be either: uncompressed: every byte of the volume is returned without any compression. native: opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. """)
@click.option('--script',
              type=str,
              required=False,
              help="""Executable name of a script. If no script name is given then the key and URL is necessary to access SolidFire nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. """)
@click.option('--scriptparameters',
              type=str,
              required=False,
              help="""JSON parameters to pass to the script.  Has the following subparameters: """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""JSON attributes for the bulk volume job.  Has the following subparameters: """)
@pass_context
def startbulkread(ctx,
           # Mandatory main parameter
           volumeid,
           # Mandatory main parameter
           format,
           # Optional main parameter
           snapshotid = None,
           # Optional main parameter
           script = None,
           # Optional main parameter
           scriptparameters = None,
           # Optional main parameter
           attributes = None):
    """StartBulkVolumeRead allows you to initialize a bulk volume read session on a specified volume."""
    """Only two bulk volume processes can run simultaneously on a volume."""
    """When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source."""
    """The external data is accessed by a web server running on a SolidFire node."""
    """Communications and server interaction information for external data access is passed by a script running on the SolidFire storage system."""
    """"""
    """At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read has completed."""
    """You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter."""
    """Reading a previous snapshot does not create a new snapshot of the volume, nor does the previous snapshot be deleted when the read completes."""
    """"""
    """Note: This process creates a new snapshot if the ID of an existing snapshot is not provided."""
    """Snapshots can be created if cluster fullness is at stage 2 or 3."""
    """Snapshots are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                    

    kwargsDict = None

    if(scriptparameters is not None):
        try:
            kwargsDict = simplejson.loads(scriptparameters)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)    

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""format = """+str(format)+""";"""+"""snapshotid = """+str(snapshotid)+""";"""+"""script = """+str(script)+""";"""+"""scriptparameters = """+str(scriptparameters)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _StartBulkVolumeReadResult = ctx.element.start_bulk_volume_read(volume_id=volumeid, format=format, snapshot_id=snapshotid, script=script, script_parameters=kwargsDict, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_StartBulkVolumeReadResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listdeleted', short_help="""ListDeletedVolumes is used to return the entire list of volumes that have been marked for deletion and is purged from the system. """, cls=SolidFireCommand)
@pass_context
def listdeleted(ctx):
    """ListDeletedVolumes is used to return the entire list of volumes that have been marked for deletion and is purged from the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListDeletedVolumesResult = ctx.element.list_deleted_volumes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListDeletedVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('purgedeleted', short_help="""PurgeDeletedVolume immediately and permanently purges a volume which has been deleted. A volume must be deleted using DeleteVolume before it can be purged. Volumes are purged automatically after a period of time, so usage of this method is not typically required. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""The ID of the volume to purge. """)
@pass_context
def purgedeleted(ctx,
           # Mandatory main parameter
           volumeid):
    """PurgeDeletedVolume immediately and permanently purges a volume which has been deleted."""
    """A volume must be deleted using DeleteVolume before it can be purged."""
    """Volumes are purged automatically after a period of time, so usage of this method is not typically required."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"")
    try:
        _PurgeDeletedVolumeResult = ctx.element.purge_deleted_volume(volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_PurgeDeletedVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('liststatsby', short_help="""ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume. Values are cumulative from the creation of the volume. """, cls=SolidFireCommand)
@pass_context
def liststatsby(ctx):
    """ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume."""
    """Values are cumulative from the creation of the volume."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListVolumeStatsByVolumeResult = ctx.element.list_volume_stats_by_volume()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumeStatsByVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateVolume is used to create a new (empty) volume on the cluster. When the volume is created successfully it is available for connection via iSCSI. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              help="""Name of the volume. Not required to be unique, but it is recommended. May be 1 to 64 characters in length. """)
@click.option('--accountid',
              type=int,
              required=True,
              help="""AccountID for the owner of this volume. """)
@click.option('--totalsize',
              type=int,
              required=True,
              help="""Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. """)
@click.option('--enable512e',
              type=bool,
              required=True,
              help="""Should the volume provides 512-byte sector emulation? """)

@click.option('--volumeqosminiops',
              type=int,
              required=False,
              help="""Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their min IOPS value and there is still insufficient performance capacity. """)

@click.option('--volumeqosmaxiops',
              type=int,
              required=False,
              help="""Desired maximum 4KB IOPS allowed over an extended period of time. """)

@click.option('--volumeqosburstiops',
              type=int,
              required=False,
              help="""Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. """)

@click.option('--volumeqosbursttime',
              type=int,
              required=False,
              help="""The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. """)

@click.option('--volumeqoscurve',
              type=int,
              required=False,
              help="""The curve is a set of key-value pairs. The keys are I/O sizes in bytes. The values represent the cost performing an IOP at a specific I/O size. The curve is calculated relative to a 4096 byte operation set at 100 IOPS. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of Name/Value pairs in JSON object format.  Has the following subparameters: """)
@click.option('--slicecount',
              type=int,
              required=False,
              help="""""")
@pass_context
def create(ctx,
           # Mandatory main parameter
           name,
           # Mandatory main parameter
           accountid,
           # Mandatory main parameter
           totalsize,
           # Mandatory main parameter
           enable512e,
           # Optional subparameter of optional main parameter.
           volumeqosminiops = None,
           # Optional subparameter of optional main parameter.
           volumeqosmaxiops = None,
           # Optional subparameter of optional main parameter.
           volumeqosburstiops = None,
           # Optional subparameter of optional main parameter.
           volumeqosbursttime = None,
           # Optional subparameter of optional main parameter.
           volumeqoscurve = None,
           # Optional main parameter
           attributes = None,
           # Optional main parameter
           slicecount = None):
    """CreateVolume is used to create a new (empty) volume on the cluster."""
    """When the volume is created successfully it is available for connection via iSCSI."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                    

    qos = None
    if(volumeqosminiops is not None or
       volumeqosmaxiops is not None or
       volumeqosburstiops is not None or
       volumeqosbursttime is not None or
       volumeqoscurve is not None or
       False):
        if not (volumeqos and volumeqos and volumeqos and volumeqos and volumeqos and  True):
            ctx.logger.error("""If you choose to provide volumeqos, you must include all of the following parameters:
volumeqosminiops
volumeqosmaxiops
volumeqosburstiops
volumeqosbursttime
volumeqoscurve
""")
        kwargsDict = dict()
        kwargsDict["min_iops"] = volumeqosminiops
        kwargsDict["max_iops"] = volumeqosmaxiops
        kwargsDict["burst_iops"] = volumeqosburstiops
        kwargsDict["burst_time"] = volumeqosbursttime
        kwargsDict["curve"] = volumeqoscurve

        qos = VolumeQOS(**kwargsDict)    

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)    
    

    ctx.logger.info("""name = """+str(name)+""";"""+"""accountid = """+str(accountid)+""";"""+"""totalsize = """+str(totalsize)+""";"""+"""enable512e = """+str(enable512e)+""";"""+"""qos = """+str(qos)+""";"""+"""attributes = """+str(attributes)+""";"""+"""slicecount = """+str(slicecount)+""";"""+"")
    try:
        _CreateVolumeResult = ctx.element.create_volume(name=name, account_id=accountid, total_size=totalsize, enable512e=enable512e, qos=qos, attributes=kwargsDict, slice_count=slicecount)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('cancelclone', short_help="""Cancels a currently running clone operation. This method does not return anything. """, cls=SolidFireCommand)
@click.option('--cloneid',
              type=int,
              required=True,
              help="""""")
@pass_context
def cancelclone(ctx,
           # Mandatory main parameter
           cloneid):
    """Cancels a currently running clone operation. This method does not return anything."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""cloneid = """+str(cloneid)+""";"""+"")
    try:
        _CancelCloneResult = ctx.element.cancel_clone(clone_id=cloneid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CancelCloneResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getdefaultqos', short_help="""GetDefaultQoS is used to retrieve the default QoS values that are set for a volume if QoS is not supplied. """, cls=SolidFireCommand)
@pass_context
def getdefaultqos(ctx):
    """GetDefaultQoS is used to retrieve the default QoS values that are set for a volume if QoS is not supplied."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _VolumeQOS = ctx.element.get_default_qos()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VolumeQOS, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getasyncresult', short_help="""Used to retrieve the result of asynchronous method calls. Some method calls are long running and do not complete when the initial response is sent. To obtain the result of the method call, polling with GetAsyncResult is required.  GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual data returned for the operation depends on the original method call and the return data is documented with each method.  The result for a completed asynchronous method call can only be retrieved once. Once the final result has been returned, later attempts returns an error. """, cls=SolidFireCommand)
@click.option('--asynchandle',
              type=int,
              required=True,
              help="""A value that was returned from the original asynchronous method call. """)
@click.option('--keepresult',
              type=bool,
              required=False,
              help="""Should the result be kept after? """)
@pass_context
def getasyncresult(ctx,
           # Mandatory main parameter
           asynchandle,
           # Optional main parameter
           keepresult = None):
    """Used to retrieve the result of asynchronous method calls."""
    """Some method calls are long running and do not complete when the initial response is sent."""
    """To obtain the result of the method call, polling with GetAsyncResult is required."""
    """"""
    """GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion,"""
    """but the actual data returned for the operation depends on the original method call and the return data is documented with each method."""
    """"""
    """The result for a completed asynchronous method call can only be retrieved once."""
    """Once the final result has been returned, later attempts returns an error."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

        
    

    ctx.logger.info("""asynchandle = """+str(asynchandle)+""";"""+"""keepresult = """+str(keepresult)+""";"""+"")
    try:
        _dict = ctx.element.get_async_result(async_handle=asynchandle, keep_result=keepresult)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_dict, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listasyncresults', short_help="""You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system. Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult to query any of the asyncHandles returned by ListAsyncResults. """, cls=SolidFireCommand)
@click.option('--asyncresulttypes',
              type=str,
              required=False,
              help="""An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values:BulkVolume: Copy operations between volumes, such as backups or restores.Clone: Volume cloning operations.DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster.RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster. """)
@pass_context
def listasyncresults(ctx,
           # Optional main parameter
           asyncresulttypes = None):
    """You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system. Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult to query any of the asyncHandles returned by ListAsyncResults."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    asyncresulttypes = parser.parse_array(asyncresulttypes)
    

    ctx.logger.info("""asyncresulttypes = """+str(asyncresulttypes)+""";"""+"")
    try:
        _ListAsyncResultsResult = ctx.element.list_async_results(async_result_types=asyncresulttypes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListAsyncResultsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('liststatsbyaccessgroup', short_help="""ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s). """, cls=SolidFireCommand)
@click.option('--volumeaccessgroups',
              type=str,
              required=False,
              help="""An array of VolumeAccessGroupIDs for which volume activity is returned. If no VolumeAccessGroupID is specified, stats for all volume access groups is returned. """)
@pass_context
def liststatsbyaccessgroup(ctx,
           # Optional main parameter
           volumeaccessgroups = None):
    """ListVolumeStatsByVolumeAccessGroup is used to get total activity measurements for all of the volumes that are a member of the specified volume access group(s)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    volumeaccessgroups = parser.parse_array(volumeaccessgroups)
    

    ctx.logger.info("""volumeaccessgroups = """+str(volumeaccessgroups)+""";"""+"")
    try:
        _ListVolumeStatsByVolumeAccessGroupResult = ctx.element.list_volume_stats_by_volume_access_group(volume_access_groups=volumeaccessgroups)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumeStatsByVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listbulkjobs', short_help="""ListBulkVolumeJobs is used to return information about each bulk volume read or write operation that is occurring in the system. """, cls=SolidFireCommand)
@pass_context
def listbulkjobs(ctx):
    """ListBulkVolumeJobs is used to return information about each bulk volume read or write operation that is occurring in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListBulkVolumeJobsResult = ctx.element.list_bulk_volume_jobs()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListBulkVolumeJobsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('clone', short_help="""CloneVolume is used to create a copy of the volume. This method is asynchronous and may take a variable amount of time to complete. The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued. GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections. ListSyncJobs can be used to see the progress of creating the clone.  Note: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned. If different settings are required, they can be changed via ModifyVolume.  Note: Cloned volumes do not inherit volume access group memberships from the source volume. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""The ID of the volume to clone. """)
@click.option('--name',
              type=str,
              required=True,
              help="""The name for the newly-created volume. """)
@click.option('--newaccountid',
              type=int,
              required=False,
              help="""AccountID for the owner of the new volume. If unspecified, the AccountID of the owner of the volume being cloned is used. """)
@click.option('--newsize',
              type=int,
              required=False,
              help="""New size of the volume, in bytes. May be greater or less than the size of the volume being cloned. If unspecified, the clone's volume size will be the same as the source volume. Size is rounded up to the nearest 1 MiB. """)
@click.option('--access',
              type=str,
              required=False,
              help="""Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""ID of the snapshot to use as the source of the clone. If unspecified, the clone will be created with a snapshot of the active volume. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of Name/Value pairs in JSON object format.  Has the following subparameters: """)
@click.option('--enable512e',
              type=bool,
              required=False,
              help="""Should the volume provide 512-byte sector emulation? """)
@pass_context
def clone(ctx,
           # Mandatory main parameter
           volumeid,
           # Mandatory main parameter
           name,
           # Optional main parameter
           newaccountid = None,
           # Optional main parameter
           newsize = None,
           # Optional main parameter
           access = None,
           # Optional main parameter
           snapshotid = None,
           # Optional main parameter
           attributes = None,
           # Optional main parameter
           enable512e = None):
    """CloneVolume is used to create a copy of the volume."""
    """This method is asynchronous and may take a variable amount of time to complete."""
    """The cloning process begins immediately when the CloneVolume request is made and is representative of the state of the volume when the API method is issued."""
    """GetAsyncResults can be used to determine when the cloning process is complete and the new volume is available for connections."""
    """ListSyncJobs can be used to see the progress of creating the clone."""
    """"""
    """Note: The initial attributes and quality of service settings for the volume are inherited from the volume being cloned."""
    """If different settings are required, they can be changed via ModifyVolume."""
    """"""
    """Note: Cloned volumes do not inherit volume access group memberships from the source volume."""
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
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""name = """+str(name)+""";"""+"""newaccountid = """+str(newaccountid)+""";"""+"""newsize = """+str(newsize)+""";"""+"""access = """+str(access)+""";"""+"""snapshotid = """+str(snapshotid)+""";"""+"""attributes = """+str(attributes)+""";"""+"""enable512e = """+str(enable512e)+""";"""+"")
    try:
        _CloneVolumeResult = ctx.element.clone_volume(volume_id=volumeid, name=name, new_account_id=newaccountid, new_size=newsize, access=access, snapshot_id=snapshotid, attributes=kwargsDict, enable512e=enable512e)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CloneVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""ModifyVolume is used to modify settings on an existing volume. Modifications can be made to one volume at a time and changes take place immediately. If an optional parameter is left unspecified, the value will not be changed.  Extending the size of a volume that is being replicated should be done in an order. The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized. It is recommended that both the target and the source volumes be the same size.  Note: If you change access status to locked or target all existing iSCSI connections are terminated. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""VolumeID for the volume to be modified. """)
@click.option('--accountid',
              type=int,
              required=False,
              help="""AccountID to which the volume is reassigned. If none is specified, the previous account name is used. """)
@click.option('--access',
              type=str,
              required=False,
              help="""Access allowed for the volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. """)

@click.option('--qosminiops',
              type=int,
              required=False,
              help="""Desired minimum 4KB IOPS to guarantee. The allowed IOPS will only drop below this level if all volumes have been capped at their minimum IOPS value and there is still insufficient performance capacity. """)

@click.option('--qosmaxiops',
              type=int,
              required=False,
              help="""Desired maximum 4KB IOPS allowed over an extended period of time. """)

@click.option('--qosburstiops',
              type=int,
              required=False,
              help="""Maximum "peak" 4KB IOPS allowed for short periods of time. Allows for bursts of I/O activity over the normal max IOPS value. """)

@click.option('--qosbursttime',
              type=int,
              required=False,
              help="""The length of time burst IOPS is allowed. The value returned is represented in time units of seconds. Note: this value is calculated by the system based on IOPS set for QoS. """)
@click.option('--totalsize',
              type=int,
              required=False,
              help="""New size of the volume in bytes. Size is rounded up to the nearest 1MiB size. This parameter can only be used to *increase* the size of a volume. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of Name/Value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           volumeid,
           # Optional main parameter
           accountid = None,
           # Optional main parameter
           access = None,
           # Optional subparameter of optional main parameter.
           qosminiops = None,
           # Optional subparameter of optional main parameter.
           qosmaxiops = None,
           # Optional subparameter of optional main parameter.
           qosburstiops = None,
           # Optional subparameter of optional main parameter.
           qosbursttime = None,
           # Optional main parameter
           totalsize = None,
           # Optional main parameter
           attributes = None):
    """ModifyVolume is used to modify settings on an existing volume."""
    """Modifications can be made to one volume at a time and changes take place immediately."""
    """If an optional parameter is left unspecified, the value will not be changed."""
    """"""
    """Extending the size of a volume that is being replicated should be done in an order."""
    """The target (Replication Target) volume should first be increased in size, then the source (Read/Write) volume can be resized."""
    """It is recommended that both the target and the source volumes be the same size."""
    """"""
    """Note: If you change access status to locked or target all existing iSCSI connections are terminated."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                

    qos = None
    if(qosminiops is not None or
       qosmaxiops is not None or
       qosburstiops is not None or
       qosbursttime is not None or
       False):
        if not ( True):
            ctx.logger.error("""If you choose to provide qos, you must include all of the following parameters:
""")
        kwargsDict = dict()
        kwargsDict["min_iops"] = qosminiops
        kwargsDict["max_iops"] = qosmaxiops
        kwargsDict["burst_iops"] = qosburstiops
        kwargsDict["burst_time"] = qosbursttime

        qos = QoS(**kwargsDict)        

    kwargsDict = None

    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""accountid = """+str(accountid)+""";"""+"""access = """+str(access)+""";"""+"""qos = """+str(qos)+""";"""+"""totalsize = """+str(totalsize)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _ModifyVolumeResult = ctx.element.modify_volume(volume_id=volumeid, account_id=accountid, access=access, qos=qos, total_size=totalsize, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('restoredeleted', short_help="""RestoreDeletedVolume marks a deleted volume as active again. This action makes the volume immediately available for iSCSI connection. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""VolumeID for the deleted volume to restore. """)
@pass_context
def restoredeleted(ctx,
           # Mandatory main parameter
           volumeid):
    """RestoreDeletedVolume marks a deleted volume as active again."""
    """This action makes the volume immediately available for iSCSI connection."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"")
    try:
        _RestoreDeletedVolumeResult = ctx.element.restore_deleted_volume(volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_RestoreDeletedVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('copy', short_help="""Copies one volume to another. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""Source volume to copy. """)
@click.option('--dstvolumeid',
              type=int,
              required=True,
              help="""Destination volume for the copy. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""Snapshot ID of the source volume to create the copy from. """)
@pass_context
def copy(ctx,
           # Mandatory main parameter
           volumeid,
           # Mandatory main parameter
           dstvolumeid,
           # Optional main parameter
           snapshotid = None):
    """Copies one volume to another."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""dstvolumeid = """+str(dstvolumeid)+""";"""+"""snapshotid = """+str(snapshotid)+""";"""+"")
    try:
        _CopyVolumeResult = ctx.element.copy_volume(volume_id=volumeid, dst_volume_id=dstvolumeid, snapshot_id=snapshotid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CopyVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listactive', short_help="""ListActiveVolumes is used to return the list of active volumes currently in the system. The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages). """, cls=SolidFireCommand)
@click.option('--startvolumeid',
              type=int,
              required=False,
              help="""The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of volumes to return from the API. """)
@pass_context
def listactive(ctx,
           # Optional main parameter
           startvolumeid = None,
           # Optional main parameter
           limit = None):
    """ListActiveVolumes is used to return the list of active volumes currently in the system."""
    """The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

        
    

    ctx.logger.info("""startvolumeid = """+str(startvolumeid)+""";"""+"""limit = """+str(limit)+""";"""+"")
    try:
        _ListActiveVolumesResult = ctx.element.list_active_volumes(start_volume_id=startvolumeid, limit=limit)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListActiveVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""The ListVolumes method is used to return a list of volumes that are in a cluster. You can specify the volumes you want to return in the list by using the available parameters. """, cls=SolidFireCommand)
@click.option('--startvolumeid',
              type=int,
              required=False,
              help="""The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of volumes to return from the API. """)
@click.option('--volumestatus',
              type=str,
              required=False,
              help="""If specified, filter to only volumes with the provided status. By default, list all volumes. """)
@click.option('--accounts',
              type=str,
              required=False,
              help="""If specified, only fetch volumes which belong to the provided accounts. By default, list volumes for all accounts. """)
@click.option('--ispaired',
              type=bool,
              required=False,
              help="""If specified, only fetch volumes which are paired (if true) or non-paired (if false). By default, list all volumes regardless of their pairing status. """)
@click.option('--volumeids',
              type=str,
              required=False,
              help="""If specified, only fetch volumes specified in this list. This option cannot be specified if startVolumeID, limit, or accounts option is specified. """)
@pass_context
def list(ctx,
           # Optional main parameter
           startvolumeid = None,
           # Optional main parameter
           limit = None,
           # Optional main parameter
           volumestatus = None,
           # Optional main parameter
           accounts = None,
           # Optional main parameter
           ispaired = None,
           # Optional main parameter
           volumeids = None):
    """The ListVolumes method is used to return a list of volumes that are in a cluster."""
    """You can specify the volumes you want to return in the list by using the available parameters."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                

    accounts = parser.parse_array(accounts)        

    volumeids = parser.parse_array(volumeids)
    

    ctx.logger.info("""startvolumeid = """+str(startvolumeid)+""";"""+"""limit = """+str(limit)+""";"""+"""volumestatus = """+str(volumestatus)+""";"""+"""accounts = """+str(accounts)+""";"""+"""ispaired = """+str(ispaired)+""";"""+"""volumeids = """+str(volumeids)+""";"""+"")
    try:
        _ListVolumesResult = ctx.element.list_volumes(start_volume_id=startvolumeid, limit=limit, volume_status=volumestatus, accounts=accounts, is_paired=ispaired, volume_ids=volumeids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('clonemultiple', short_help="""CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together. If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes.  Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumes',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["volumeid", "accessvolumes", "name", "newaccountidvolumes", "newsize", "attributes", ],
              required=True,
              help="""Array of Unique ID for each volume to include in the clone with optional parameters. If optional parameters are not specified, the values will be inherited from the source volumes.  Has the following subparameters: --volumeid --accessvolumes --name --newaccountidvolumes --newsize --attributes """)
@click.option('--volumeid',
              required=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Required parameter for "volumes" array: volumeID. """,
              cls=SolidFireOption)
@click.option('--accessvolumes',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Access settings for the new volume. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. """,
              cls=SolidFireOption)
@click.option('--name',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] New name for the clone. """,
              cls=SolidFireOption)
@click.option('--newaccountidvolumes',
              required=False,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Account ID for the new volume. """,
              cls=SolidFireOption)
@click.option('--newsize',
              required=False,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. """,
              cls=SolidFireOption)
@click.option('--attributes',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] List of Name/Value pairs in JSON object format. """,
              cls=SolidFireOption)
@click.option('--access',
              type=str,
              required=False,
              help="""New default access method for the new volumes if not overridden by information passed in the volumes array. readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked.  If unspecified, the access settings of the clone will be the same as the source. """)
@click.option('--groupsnapshotid',
              type=int,
              required=False,
              help="""ID of the group snapshot to use as a basis for the clone. """)
@click.option('--newaccountid',
              type=int,
              required=False,
              help="""New account ID for the volumes if not overridden by information passed in the volumes array. """)
@pass_context
def clonemultiple(ctx,
           # Mandatory main parameter
           volumes,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           accessvolumes = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           name = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           newaccountidvolumes = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           newsize = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           attributes = None,
           # Optional main parameter
           access = None,
           # Optional main parameter
           groupsnapshotid = None,
           # Optional main parameter
           newaccountid = None):
    """CloneMultipleVolumes is used to create a clone of a group of specified volumes. A consistent set of characteristics can be assigned to a group of multiple volume when they are cloned together."""
    """If groupSnapshotID is going to be used to clone the volumes in a group snapshot, the group snapshot must be created first using the CreateGroupSnapshot API method or the SolidFire Element WebUI. Using groupSnapshotID is optional when cloning multiple volumes."""
    """"""
    """Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    volumesArray = []
    if(volumes is not None):
        try:
            for i, _volumes in enumerate(volumes):
                attributes_json = None
                if attributes[i] != None:
                    attributes_json = simplejson.loads(attributes[i])
                volumesArray.append(CloneMultipleVolumeParams(volume_id=volumeid[i], access=accessvolumes[i], name=name[i], new_account_id=newaccountidvolumes[i], new_size=newsize[i], attributes=attributes_json, ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)            
    

    ctx.logger.info("""volumes = """+str(volumes)+""";"""+"""access = """+str(access)+""";"""+"""groupsnapshotid = """+str(groupsnapshotid)+""";"""+"""newaccountid = """+str(newaccountid)+""";"""+"")
    try:
        _CloneMultipleVolumesResult = ctx.element.clone_multiple_volumes(volumes=volumesArray, access=access, group_snapshot_id=groupsnapshotid, new_account_id=newaccountid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CloneMultipleVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('setdefaultqos', short_help="""SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or IOPS) for all volumes not yet created. """, cls=SolidFireCommand)
@click.option('--miniops',
              type=int,
              required=False,
              help="""The minimum number of sustained IOPS that are provided by the cluster to a volume. """)
@click.option('--maxiops',
              type=int,
              required=False,
              help="""The maximum number of sustained IOPS that are provided by the cluster to a volume. """)
@click.option('--burstiops',
              type=int,
              required=False,
              help="""The maximum number of IOPS allowed in a short burst scenario. """)
@pass_context
def setdefaultqos(ctx,
           # Optional main parameter
           miniops = None,
           # Optional main parameter
           maxiops = None,
           # Optional main parameter
           burstiops = None):
    """SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or IOPS) for all volumes not yet created."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""miniops = """+str(miniops)+""";"""+"""maxiops = """+str(maxiops)+""";"""+"""burstiops = """+str(burstiops)+""";"""+"")
    try:
        _SetDefaultQoSResult = ctx.element.set_default_qos(min_iops=miniops, max_iops=maxiops, burst_iops=burstiops)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SetDefaultQoSResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstats', short_help="""GetVolumeStats is used to retrieve high-level activity measurements for a single volume. Values are cumulative from the creation of the volume. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""Specifies the volume for which statistics is gathered. """)
@pass_context
def getstats(ctx,
           # Mandatory main parameter
           volumeid):
    """GetVolumeStats is used to retrieve high-level activity measurements for a single volume."""
    """Values are cumulative from the creation of the volume."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"")
    try:
        _GetVolumeStatsResult = ctx.element.get_volume_stats(volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetVolumeStatsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listforaccount', short_help="""ListVolumesForAccount returns the list of active AND (pending) deleted volumes for an account. """, cls=SolidFireCommand)
@click.option('--accountid',
              type=int,
              required=True,
              help="""The ID of the account to list the volumes for. """)
@click.option('--startvolumeid',
              type=int,
              required=False,
              help="""The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of volumes to return from the API. """)
@pass_context
def listforaccount(ctx,
           # Mandatory main parameter
           accountid,
           # Optional main parameter
           startvolumeid = None,
           # Optional main parameter
           limit = None):
    """ListVolumesForAccount returns the list of active AND (pending) deleted volumes for an account."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""accountid = """+str(accountid)+""";"""+"""startvolumeid = """+str(startvolumeid)+""";"""+"""limit = """+str(limit)+""";"""+"")
    try:
        _ListVolumesForAccountResult = ctx.element.list_volumes_for_account(account_id=accountid, start_volume_id=startvolumeid, limit=limit)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumesForAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getcount', short_help="""GetVolumeCount enables you to retrieve the number of volumes currently in the system. """, cls=SolidFireCommand)
@pass_context
def getcount(ctx):
    """GetVolumeCount enables you to retrieve the number of volumes currently in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetVolumeCountResult = ctx.element.get_volume_count()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetVolumeCountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('cancelgroupclone', short_help="""CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process for a group of clones. When you cancel a group clone operation, the system completes and removes the operation's associated asyncHandle. This method does not return anything. """, cls=SolidFireCommand)
@click.option('--groupcloneid',
              type=int,
              required=True,
              help="""cloneID for the ongoing clone process. """)
@pass_context
def cancelgroupclone(ctx,
           # Mandatory main parameter
           groupcloneid):
    """CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process for a group of clones. When you cancel a group clone operation, the system completes and removes the operation&#x27;s associated asyncHandle. This method does not return anything."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""groupcloneid = """+str(groupcloneid)+""";"""+"")
    try:
        _CancelGroupCloneResult = ctx.element.cancel_group_clone(group_clone_id=groupcloneid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CancelGroupCloneResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""DeleteVolume marks an active volume for deletion. It is purged (permanently deleted) after the cleanup interval elapses. After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state. It is not returned in target discovery requests.  Any snapshots of a volume that has been marked to delete are not affected. Snapshots are kept until the volume is purged from the system.  If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.  If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state. The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume. Until the deleted volume is purged, it can be restored and data transfers resumes. If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed. The purged volume becomes permanently unavailable. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""The ID of the volume to delete. """)
@pass_context
def delete(ctx,
           # Mandatory main parameter
           volumeid):
    """DeleteVolume marks an active volume for deletion."""
    """It is purged (permanently deleted) after the cleanup interval elapses."""
    """After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state."""
    """It is not returned in target discovery requests."""
    """"""
    """Any snapshots of a volume that has been marked to delete are not affected."""
    """Snapshots are kept until the volume is purged from the system."""
    """"""
    """If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped."""
    """"""
    """If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state."""
    """The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume."""
    """Until the deleted volume is purged, it can be restored and data transfers resumes."""
    """If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed."""
    """The purged volume becomes permanently unavailable."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"")
    try:
        _DeleteVolumeResult = ctx.element.delete_volume(volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DeleteVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

