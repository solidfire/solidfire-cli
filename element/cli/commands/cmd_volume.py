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

@cli.command('getefficiency', short_help="""GetVolumeEfficiency enables you to retrieve information about a volume. Only the volume you give as a parameter in this API method is used to compute the capacity. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""Specifies the volume for which capacity is computed. """)
@pass_context
def getefficiency(ctx,
           # Mandatory main parameter
           volumeid):
    """GetVolumeEfficiency enables you to retrieve information about a volume. Only the volume you give as a parameter in this API method is used to compute the capacity."""
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
@click.option('--accounts',
              type=str,
              required=False,
              help="""One or more account ids by which to filter the result. """)
@click.option('--includevirtualvolumes',
              type=bool,
              required=False,
              help="""Includes virtual volumes in the response by default. To exclude virtual volumes, set to false. """)
@pass_context
def liststatsbyaccount(ctx,
           # Optional main parameter
           accounts = None,
           # Optional main parameter
           includevirtualvolumes = None):
    """ListVolumeStatsByAccount returns high-level activity measurements for every account. Values are summed from all the volumes owned by the account."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    accounts = parser.parse_array(accounts)    
    

    ctx.logger.info("""accounts = """+str(accounts)+""";"""+"""includevirtualvolumes = """+str(includevirtualvolumes)+""";"""+"")
    try:
        _ListVolumeStatsByAccountResult = ctx.element.list_volume_stats_by_account(accounts=accounts, include_virtual_volumes=includevirtualvolumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumeStatsByAccountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('startbulkwrite', short_help="""StartBulkVolumeWrite enables you to initialize a bulk volume write session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the write session, data is written to a SolidFire storage volume from an external backup source. The external data is accessed by a web server running on an SF-series node. Communications and server interaction information for external data access is passed by a script running on the storage system. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""The ID of the volume to be written to. """)
@click.option('--format',
              type=str,
              required=True,
              help="""The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. """)
@click.option('--script',
              type=str,
              required=False,
              help="""The executable name of a script. If unspecified, the key and URL are necessary to access SF-series nodes. The script runs on the primary node and the key and URL is returned to the script, so the local web server can be contacted. """)
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
    """StartBulkVolumeWrite enables you to initialize a bulk volume write session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the write session, data is written to a SolidFire storage volume from an external backup source. The external data is accessed by a web server running on an SF-series node. Communications and server"""
    """interaction information for external data access is passed by a script running on the storage system."""
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



@cli.command('updatebulkstatus', short_help="""You can use UpdateBulkVolumeStatus in a script to update the status of a bulk volume job that you started with the StartBulkVolumeRead or StartBulkVolumeWrite methods. """, cls=SolidFireCommand)
@click.option('--key',
              type=str,
              required=True,
              help="""The key assigned during initialization of a StartBulkVolumeRead or StartBulkVolumeWrite session. """)
@click.option('--status',
              type=str,
              required=True,
              help="""The status of the given bulk volume job. The system sets the status. Possible values are:  running: Jobs that are still active. complete: Jobs that are done. failed: Jobs that failed. """)
@click.option('--percentcomplete',
              type=str,
              required=False,
              help="""The completed progress of the bulk volume job as a percentage value. """)
@click.option('--message',
              type=str,
              required=False,
              help="""The message returned indicating the status of the bulk volume job after the job is complete. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""JSON attributes; updates what is on the bulk volume job.  Has the following subparameters: """)
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
    """You can use UpdateBulkVolumeStatus in a script to update the status of a bulk volume job that you started with the"""
    """StartBulkVolumeRead or StartBulkVolumeWrite methods."""
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



@cli.command('startbulkread', short_help="""StartBulkVolumeRead enables you to initialize a bulk volume read session on a specified volume. Only two bulk volume processes can run simultaneously on a volume. When you initialize the session, data is read from a SolidFire storage volume for the purposes of storing the data on an external backup source. The external data is accessed by a web server running on an SF-series node. Communications and server interaction information for external data access is passed by a script running on the storage system. At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read is complete. You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter. When you read a previous snapshot, the system does not create a new snapshot of the volume or delete the previous snapshot when the read completes. Note: This process creates a new snapshot if the ID of an existing snapshot is not provided. Snapshots can be created if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""The ID of the volume to be read. """)
@click.option('--format',
              type=str,
              required=True,
              help="""The format of the volume data. It can be either of the following formats: uncompressed: Every byte of the volume is returned without any compression. native: Opaque data is returned that is smaller and more efficiently stored and written on a subsequent bulk volume write. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""The ID of a previously created snapshot used for bulk volume reads. If no ID is entered, a snapshot of the current active volume image is made. """)
@click.option('--script',
              type=str,
              required=False,
              help="""The executable name of a script. If unspecified, the key and URL is necessary to access SF-series nodes. The script is run on the primary node and the key and URL is returned to the script so the local web server can be contacted. """)
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
    """StartBulkVolumeRead enables you to initialize a bulk volume read session on a specified volume. Only two bulk volume processes"""
    """can run simultaneously on a volume. When you initialize the session, data is read from a SolidFire storage volume for the purposes"""
    """of storing the data on an external backup source. The external data is accessed by a web server running on an SF-series node."""
    """Communications and server interaction information for external data access is passed by a script running on the storage system."""
    """At the start of a bulk volume read operation, a snapshot of the volume is made and the snapshot is deleted when the read is complete. You can also read a snapshot of the volume by entering the ID of the snapshot as a parameter. When you read a"""
    """previous snapshot, the system does not create a new snapshot of the volume or delete the previous snapshot when the"""
    """read completes."""
    """Note: This process creates a new snapshot if the ID of an existing snapshot is not provided. Snapshots can be created if cluster fullness is at stage 2 or 3. Snapshots are not created when cluster fullness is at stage 4 or 5."""
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



@cli.command('listdeleted', short_help="""ListDeletedVolumes enables you to retrieve the list of volumes that have been marked for deletion and purged from the system. """, cls=SolidFireCommand)
@click.option('--includevirtualvolumes',
              type=bool,
              required=False,
              help="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """)
@pass_context
def listdeleted(ctx,
           # Optional main parameter
           includevirtualvolumes = None):
    """ListDeletedVolumes enables you to retrieve the list of volumes that have been marked for deletion and purged from the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""includevirtualvolumes = """+str(includevirtualvolumes)+""";"""+"")
    try:
        _ListDeletedVolumesResult = ctx.element.list_deleted_volumes(include_virtual_volumes=includevirtualvolumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListDeletedVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('purgedeleted', short_help="""PurgeDeletedVolume immediately and permanently purges a volume that has been deleted. You must delete a volume using DeleteVolume before it can be purged. Volumes are purged automatically after a period of time, so usage of this method is not typically required. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""The ID of the volume to be purged. """)
@pass_context
def purgedeleted(ctx,
           # Mandatory main parameter
           volumeid):
    """PurgeDeletedVolume immediately and permanently purges a volume that has been deleted. You must delete a volume using"""
    """DeleteVolume before it can be purged. Volumes are purged automatically after a period of time, so usage of this method is not"""
    """typically required."""
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
@click.option('--includevirtualvolumes',
              type=bool,
              required=False,
              help="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """)
@pass_context
def liststatsby(ctx,
           # Optional main parameter
           includevirtualvolumes = None):
    """ListVolumeStatsByVolume returns high-level activity measurements for every volume, by volume. Values are cumulative from the"""
    """creation of the volume."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""includevirtualvolumes = """+str(includevirtualvolumes)+""";"""+"")
    try:
        _ListVolumeStatsByVolumeResult = ctx.element.list_volume_stats_by_volume(include_virtual_volumes=includevirtualvolumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumeStatsByVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateVolume enables you to create a new (empty) volume on the cluster. As soon as the volume creation is complete, the volume is available for connection via iSCSI. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              help="""The name of the volume access group (might be user specified). Not required to be unique, but recommended. Might be 1 to 64 characters in length. """)
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
              help="""Specifies whether 512e emulation is enabled or not. Possible values are: true: The volume provides 512-byte sector emulation. false: 512e emulation is not enabled. """)

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
@click.option('--attributes',
              type=str,
              required=False,
              help="""The list of name-value pairs in JSON object format. Total attribute size must be less than 1000B, or 1KB, including JSON formatting characters.  Has the following subparameters: """)
@click.option('--slicecount',
              type=int,
              required=False,
              help=""" """)
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
           qosminiops = None,
           # Optional subparameter of optional main parameter.
           qosmaxiops = None,
           # Optional subparameter of optional main parameter.
           qosburstiops = None,
           # Optional subparameter of optional main parameter.
           qosbursttime = None,
           # Optional main parameter
           attributes = None,
           # Optional main parameter
           slicecount = None):
    """CreateVolume enables you to create a new (empty) volume on the cluster. As soon as the volume creation is complete, the volume is"""
    """available for connection via iSCSI."""
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



@cli.command('cancelclone', short_help="""CancelClone enables you to stop an ongoing CloneVolume or CopyVolume process. When you cancel a group clone operation, the system completes and removes the operation's associated asyncHandle. """, cls=SolidFireCommand)
@click.option('--cloneid',
              type=int,
              required=True,
              help="""The cloneID for the ongoing clone process. """)
@pass_context
def cancelclone(ctx,
           # Mandatory main parameter
           cloneid):
    """CancelClone enables you to stop an ongoing CloneVolume or CopyVolume process. When you cancel a group clone operation, the"""
    """system completes and removes the operation&#x27;s associated asyncHandle."""
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



@cli.command('getdefaultqos', short_help="""GetDefaultQoS enables you to retrieve the default QoS values for a newly created volume. """, cls=SolidFireCommand)
@pass_context
def getdefaultqos(ctx):
    """GetDefaultQoS enables you to retrieve the default QoS values for a newly created volume."""
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



@cli.command('getasyncresult', short_help="""You can use GetAsyncResult to retrieve the result of asynchronous method calls. Some method calls require some time to run, and might not be finished when the system sends the initial response. To obtain the status or result of the method call, use GetAsyncResult to poll the asyncHandle value returned by the method. GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual data returned for the operation depends on the original method call and the return data is documented with each method. """, cls=SolidFireCommand)
@click.option('--asynchandle',
              type=int,
              required=True,
              help="""A value that was returned from the original asynchronous method call. """)
@click.option('--keepresult',
              type=bool,
              required=False,
              help="""If true, GetAsyncResult does not remove the asynchronous result upon returning it, enabling future queries to that asyncHandle. """)
@pass_context
def getasyncresult(ctx,
           # Mandatory main parameter
           asynchandle,
           # Optional main parameter
           keepresult = None):
    """You can use GetAsyncResult to retrieve the result of asynchronous method calls. Some method calls require some time to run, and"""
    """might not be finished when the system sends the initial response. To obtain the status or result of the method call, use"""
    """GetAsyncResult to poll the asyncHandle value returned by the method."""
    """GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual"""
    """data returned for the operation depends on the original method call and the return data is documented with each method."""
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
              help="""An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values are: BulkVolume: Copy operations between volumes, such as backups or restores. Clone: Volume cloning operations. DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster. RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster """)
@pass_context
def listasyncresults(ctx,
           # Optional main parameter
           asyncresulttypes = None):
    """You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system."""
    """Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult"""
    """to query any of the asyncHandles returned by ListAsyncResults."""
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



@cli.command('liststatsbyaccessgroup', short_help="""ListVolumeStatsByVolumeAccessGroup enables you to get total activity measurements for all of the volumes that are a member of the specified volume access group(s). """, cls=SolidFireCommand)
@click.option('--volumeaccessgroups',
              type=str,
              required=False,
              help="""An array of VolumeAccessGroupIDs for which volume activity is returned. If omitted, statistics for all volume access groups are returned. """)
@click.option('--includevirtualvolumes',
              type=bool,
              required=False,
              help="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """)
@pass_context
def liststatsbyaccessgroup(ctx,
           # Optional main parameter
           volumeaccessgroups = None,
           # Optional main parameter
           includevirtualvolumes = None):
    """ListVolumeStatsByVolumeAccessGroup enables you to get total activity measurements for all of the volumes that are a member of the"""
    """specified volume access group(s)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    volumeaccessgroups = parser.parse_array(volumeaccessgroups)    
    

    ctx.logger.info("""volumeaccessgroups = """+str(volumeaccessgroups)+""";"""+"""includevirtualvolumes = """+str(includevirtualvolumes)+""";"""+"")
    try:
        _ListVolumeStatsByVolumeAccessGroupResult = ctx.element.list_volume_stats_by_volume_access_group(volume_access_groups=volumeaccessgroups, include_virtual_volumes=includevirtualvolumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumeStatsByVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listbulkjobs', short_help="""ListBulkVolumeJobs enables you to retrieve information about each bulk volume read or write operation that is occurring in the system. """, cls=SolidFireCommand)
@pass_context
def listbulkjobs(ctx):
    """ListBulkVolumeJobs enables you to retrieve information about each bulk volume read or write operation that is occurring in the"""
    """system."""
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



@cli.command('clone', short_help="""CloneVolume enables you to create a copy of a volume. This method is asynchronous and might take a variable amount of time to complete. The cloning process begins immediately when you make the CloneVolume request and is representative of the state of the volume when the API method is issued. You can use the GetAsyncResult method to determine when the cloning process is complete and the new volume is available for connections. You can use ListSyncJobs to see the progress of creating the clone. Note: The initial attributes and QoS settings for the volume are inherited from the volume being cloned. You can change these settings with ModifyVolume. Note: Cloned volumes do not inherit volume access group memberships from the source volume. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""VolumeID for the volume to be cloned. """)
@click.option('--name',
              type=str,
              required=True,
              help="""The name of the new cloned volume. Might be 1 to 64 characters in length. """)
@click.option('--newaccountid',
              type=int,
              required=False,
              help="""AccountID for the owner of the new volume. If unspecified, the accountID of the owner of the volume being cloned is used. """)
@click.option('--newsize',
              type=int,
              required=False,
              help="""New size of the volume, in bytes. Might be greater or less than the size of the volume being cloned. If unspecified, the volume size is not changed. Size is rounded to the nearest 1MB. """)
@click.option('--access',
              type=str,
              required=False,
              help="""Specifies the level of access allowed for the new volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If unspecified, the level of access of the volume being cloned is used. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
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
    """CloneVolume enables you to create a copy of a volume. This method is asynchronous and might take a variable amount of time to complete. The cloning process begins immediately when you make the CloneVolume request and is representative of the state of the volume when the API method is issued. You can use the GetAsyncResult method to determine when the cloning process is complete and the new volume is available for connections. You can use ListSyncJobs to see the progress of creating the clone."""
    """Note: The initial attributes and QoS settings for the volume are inherited from the volume being cloned. You can change these settings with ModifyVolume."""
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



@cli.command('modify', short_help="""ModifyVolume enables you to modify settings on an existing volume. You can make modifications to one volume at a time and changes take place immediately. If you do not specify QoS values when you modify a volume, they remain the same as before the modification. You can retrieve default QoS values for a newly created volume by running the GetDefaultQoS method. When you need to increase the size of a volume that is being replicated, do so in the following order to prevent replication errors: 1. Increase the size of the "Replication Target" volume. 2. Increase the size of the source or "Read / Write" volume. NetApp recommends that both the target and source volumes are the same size. Note: If you change the "access" status to locked or target, all existing iSCSI connections are terminated. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""VolumeID for the volume to be modified. """)
@click.option('--accountid',
              type=int,
              required=False,
              help="""AccountID to which the volume is reassigned. If unspecified, the previous account name is used. """)
@click.option('--access',
              type=str,
              required=False,
              help="""Specifies the access allowed for the volume. Possible values are: readOnly: Only read operations are allowed. readWrite: Reads and writes are allowed. locked: No reads or writes are allowed. If not specified, the access value does not change. replicationTarget: Identify a volume as the target volume for a paired set of volumes. If the volume is not paired, the access status is locked. If a value is not specified, the access value does not change. """)

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
              help="""New size of the volume in bytes. 1000000000 is equal to 1GB. Size is rounded up to the nearest 1MB. This parameter can only be used to increase the size of a volume. """)
@click.option('--setcreatetime',
              type=bool,
              required=False,
              help="""If set to true, changes the recorded date of volume creation. """)
@click.option('--createtime',
              type=str,
              required=False,
              help="""An ISO 8601 date string to set as the new volume creation date. Required if "setCreateTime" is set to true. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
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
           setcreatetime = None,
           # Optional main parameter
           createtime = None,
           # Optional main parameter
           attributes = None):
    """ModifyVolume enables you to modify settings on an existing volume. You can make modifications to one volume at a time and"""
    """changes take place immediately. If you do not specify QoS values when you modify a volume, they remain the same as before the modification. You can retrieve"""
    """default QoS values for a newly created volume by running the GetDefaultQoS method."""
    """When you need to increase the size of a volume that is being replicated, do so in the following order to prevent replication errors:"""
    """1. Increase the size of the &quot;Replication Target&quot; volume."""
    """2. Increase the size of the source or &quot;Read / Write&quot; volume."""
    """NetApp recommends that both the target and source volumes are the same size."""
    """Note: If you change the &quot;access&quot; status to locked or target, all existing iSCSI connections are terminated."""
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
    

    ctx.logger.info("""volumeid = """+str(volumeid)+""";"""+"""accountid = """+str(accountid)+""";"""+"""access = """+str(access)+""";"""+"""qos = """+str(qos)+""";"""+"""totalsize = """+str(totalsize)+""";"""+"""setcreatetime = """+str(setcreatetime)+""";"""+"""createtime = """+str(createtime)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _ModifyVolumeResult = ctx.element.modify_volume(volume_id=volumeid, account_id=accountid, access=access, qos=qos, total_size=totalsize, set_create_time=setcreatetime, create_time=createtime, attributes=kwargsDict)
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
              help="""VolumeID of the deleted volume to be restored. """)
@pass_context
def restoredeleted(ctx,
           # Mandatory main parameter
           volumeid):
    """RestoreDeletedVolume marks a deleted volume as active again. This action makes the volume immediately available for iSCSI connection."""
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



@cli.command('copy', short_help="""CopyVolume enables you to overwrite the data contents of an existing volume with the data contents of another volume (or snapshot). Attributes of the destination volume such as IQN, QoS settings, size, account, and volume access group membership are not changed. The destination volume must already exist and must be the same size as the source volume. NetApp strongly recommends that clients unmount the destination volume before the CopyVolume operation begins. If the destination volume is modified during the copy operation, the changes will be lost. This method is asynchronous and may take a variable amount of time to complete. You can use the GetAsyncResult method to determine when the process has finished, and ListSyncJobs to see the progress of the copy. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""VolumeID of the volume to be read from. """)
@click.option('--dstvolumeid',
              type=int,
              required=True,
              help="""VolumeID of the volume to be overwritten. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""ID of the snapshot that is used as the source of the clone. If no ID is provided, the current active volume is used. """)
@pass_context
def copy(ctx,
           # Mandatory main parameter
           volumeid,
           # Mandatory main parameter
           dstvolumeid,
           # Optional main parameter
           snapshotid = None):
    """CopyVolume enables you to overwrite the data contents of an existing volume with the data contents of another volume (or"""
    """snapshot). Attributes of the destination volume such as IQN, QoS settings, size, account, and volume access group membership are"""
    """not changed. The destination volume must already exist and must be the same size as the source volume."""
    """NetApp strongly recommends that clients unmount the destination volume before the CopyVolume operation begins. If the"""
    """destination volume is modified during the copy operation, the changes will be lost."""
    """This method is asynchronous and may take a variable amount of time to complete. You can use the GetAsyncResult method to"""
    """determine when the process has finished, and ListSyncJobs to see the progress of the copy."""
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



@cli.command('listactive', short_help="""ListActiveVolumes enables you to return the list of active volumes currently in the system. The list of volumes is returned sorted in VolumeID order and can be returned in multiple parts (pages). """, cls=SolidFireCommand)
@click.option('--startvolumeid',
              type=int,
              required=False,
              help="""Starting VolumeID to return. If no volume exists with this VolumeID, the next volume by VolumeID order is used as the start of the list. To page through the list, pass the VolumeID of the last volume in the previous response + 1. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""Maximum number of Volume Info objects to return. A value of 0 (zero) returns all volumes (unlimited). """)
@click.option('--includevirtualvolumes',
              type=bool,
              required=False,
              help="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """)
@pass_context
def listactive(ctx,
           # Optional main parameter
           startvolumeid = None,
           # Optional main parameter
           limit = None,
           # Optional main parameter
           includevirtualvolumes = None):
    """ListActiveVolumes enables you to return the list of active volumes currently in the system. The list of volumes is returned sorted in"""
    """VolumeID order and can be returned in multiple parts (pages)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""startvolumeid = """+str(startvolumeid)+""";"""+"""limit = """+str(limit)+""";"""+"""includevirtualvolumes = """+str(includevirtualvolumes)+""";"""+"")
    try:
        _ListActiveVolumesResult = ctx.element.list_active_volumes(start_volume_id=startvolumeid, limit=limit, include_virtual_volumes=includevirtualvolumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListActiveVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""The ListVolumes method enables you to retrieve a list of volumes that are in a cluster. You can specify the volumes you want to return in the list by using the available parameters. """, cls=SolidFireCommand)
@click.option('--startvolumeid',
              type=int,
              required=False,
              help="""Only volumes with an ID greater than or equal to this value are returned. Mutually exclusive with the volumeIDs parameter. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""Specifies the maximum number of volume results that are returned. Mutually exclusive with the volumeIDs parameter. """)
@click.option('--volumestatus',
              type=str,
              required=False,
              help="""Only volumes with a status equal to the status value are returned. Possible values are: creating snapshotting active deleted """)
@click.option('--accounts',
              type=str,
              required=False,
              help="""Returns only the volumes owned by the accounts you specify here. Mutually exclusive with the volumeIDs parameter. """)
@click.option('--ispaired',
              type=bool,
              required=False,
              help="""Returns volumes that are paired or not paired. Possible values are: true: Returns all paired volumes. false: Returns all volumes that are not paired. """)
@click.option('--volumeids',
              type=str,
              required=False,
              help="""A list of volume IDs. If you supply this parameter, other parameters operate only on this set of volumes. Mutually exclusive with the accounts, startVolumeID, and limit parameters. """)
@click.option('--volumename',
              type=str,
              required=False,
              help="""Only volume object information matching the volume name is returned. """)
@click.option('--includevirtualvolumes',
              type=bool,
              required=False,
              help="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """)
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
           volumeids = None,
           # Optional main parameter
           volumename = None,
           # Optional main parameter
           includevirtualvolumes = None):
    """The ListVolumes method enables you to retrieve a list of volumes that are in a cluster. You can specify the volumes you want to"""
    """return in the list by using the available parameters."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                

    accounts = parser.parse_array(accounts)        

    volumeids = parser.parse_array(volumeids)        
    

    ctx.logger.info("""startvolumeid = """+str(startvolumeid)+""";"""+"""limit = """+str(limit)+""";"""+"""volumestatus = """+str(volumestatus)+""";"""+"""accounts = """+str(accounts)+""";"""+"""ispaired = """+str(ispaired)+""";"""+"""volumeids = """+str(volumeids)+""";"""+"""volumename = """+str(volumename)+""";"""+"""includevirtualvolumes = """+str(includevirtualvolumes)+""";"""+"")
    try:
        _ListVolumesResult = ctx.element.list_volumes(start_volume_id=startvolumeid, limit=limit, volume_status=volumestatus, accounts=accounts, is_paired=ispaired, volume_ids=volumeids, volume_name=volumename, include_virtual_volumes=includevirtualvolumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('clonemultiple', short_help="""CloneMultipleVolumes enables you to create a clone of a group of specified volumes. You can assign a consistent set of characteristics to a group of multiple volumes when they are cloned together. Before using groupSnapshotID to clone the volumes in a group snapshot, you must create the group snapshot by using the CreateGroupSnapshot API method or the Element OS Web UI. Using groupSnapshotID is optional when cloning multiple volumes. Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is at stage 4 or 5. """, cls=SolidFireCommand)
@click.option('--volumes',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["volumeid", "accessvolumes", "name", "newaccountidvolumes", "newsize", "attributes", ],
              required=True,
              help="""Unique ID for each volume to include in the clone. If optional parameters are not specified, the values are inherited from the source volumes. Required parameter for "volumes" array: volumeID Optional parameters for "volumes" array: access: Can be one of readOnly, readWrite, locked, or replicationTarget attributes: List of name-value pairs in JSON object format. name: New name for the clone. newAccountID: Account ID for the new volumes. newSize: New size Total size of the volume, in bytes. Size is rounded up to the nearest 1MB.  Has the following subparameters: --volumeid --accessvolumes --name --newaccountidvolumes --newsize --attributes """)
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
              help="""New default access method for the new volumes if not overridden by information passed in the volume's array. """)
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
    """CloneMultipleVolumes enables you to create a clone of a group of specified volumes. You can assign a consistent set of characteristics"""
    """to a group of multiple volumes when they are cloned together."""
    """Before using groupSnapshotID to clone the volumes in a group snapshot, you must create the group snapshot by using the"""
    """CreateGroupSnapshot API method or the Element OS Web UI. Using groupSnapshotID is optional when cloning multiple volumes."""
    """Note: Cloning multiple volumes is allowed if cluster fullness is at stage 2 or 3. Clones are not created when cluster fullness is"""
    """at stage 4 or 5."""
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



@cli.command('setdefaultqos', short_help="""SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or IOPS) for a volume. For more information about QoS in a SolidFire cluster, see the User Guide. """, cls=SolidFireCommand)
@click.option('--miniops',
              type=int,
              required=False,
              help="""The minimum number of sustained IOPS provided by the cluster to a volume. """)
@click.option('--maxiops',
              type=int,
              required=False,
              help="""The maximum number of sustained IOPS provided by the cluster to a volume. """)
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
    """SetDefaultQoS enables you to configure the default Quality of Service (QoS) values (measured in inputs and outputs per second, or"""
    """IOPS) for a volume. For more information about QoS in a SolidFire cluster, see the User Guide."""
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



@cli.command('getstats', short_help="""GetVolumeStats enables  you to retrieve high-level activity measurements for a single volume. Values are cumulative from the creation of the volume. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""Specifies the volume for which statistics are gathered. """)
@pass_context
def getstats(ctx,
           # Mandatory main parameter
           volumeid):
    """GetVolumeStats enables  you to retrieve high-level activity measurements for a single volume. Values are cumulative from the creation of the volume."""
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



@cli.command('listforaccount', short_help="""ListVolumesForAccount returns the list of active and (pending) deleted volumes for an account. """, cls=SolidFireCommand)
@click.option('--accountid',
              type=int,
              required=True,
              help="""Returns all volumes owned by this AccountID. """)
@click.option('--startvolumeid',
              type=int,
              required=False,
              help="""The ID of the first volume to list. This can be useful for paging results. By default, this starts at the lowest VolumeID. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of volumes to return from the API. """)
@click.option('--includevirtualvolumes',
              type=bool,
              required=False,
              help="""Specifies that virtual volumes are included in the response by default. To exclude virtual volumes, set to false. """)
@pass_context
def listforaccount(ctx,
           # Mandatory main parameter
           accountid,
           # Optional main parameter
           startvolumeid = None,
           # Optional main parameter
           limit = None,
           # Optional main parameter
           includevirtualvolumes = None):
    """ListVolumesForAccount returns the list of active and (pending) deleted volumes for an account."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                
    

    ctx.logger.info("""accountid = """+str(accountid)+""";"""+"""startvolumeid = """+str(startvolumeid)+""";"""+"""limit = """+str(limit)+""";"""+"""includevirtualvolumes = """+str(includevirtualvolumes)+""";"""+"")
    try:
        _ListVolumesForAccountResult = ctx.element.list_volumes_for_account(account_id=accountid, start_volume_id=startvolumeid, limit=limit, include_virtual_volumes=includevirtualvolumes)
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



@cli.command('cancelgroupclone', short_help="""CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process occurring on a group of volumes. When you cancel a group clone operation, the system completes and removes the operation's associated asyncHandle. """, cls=SolidFireCommand)
@click.option('--groupcloneid',
              type=int,
              required=True,
              help="""The cloneID for the ongoing clone process. """)
@pass_context
def cancelgroupclone(ctx,
           # Mandatory main parameter
           groupcloneid):
    """CancelGroupClone enables you to stop an ongoing CloneMultipleVolumes process occurring on a group of volumes. When you cancel"""
    """a group clone operation, the system completes and removes the operation&#x27;s associated asyncHandle."""
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



@cli.command('delete', short_help="""DeleteVolume marks an active volume for deletion. When marked, the volume is purged (permanently deleted) after the cleanup interval elapses. After making a request to delete a volume, any active iSCSI connections to the volume are immediately terminated and no further connections are allowed while the volume is in this state. A marked volume is not returned in target discovery requests. Any snapshots of a volume that has been marked for deletion are not affected. Snapshots are kept until the volume is purged from the system. If a volume is marked for deletion and has a bulk volume read or bulk volume write operation in progress, the bulk volume read or write operation is stopped. If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state. The remote volume that the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume. Until the deleted volume is purged, it can be restored and data transfers resume. If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed. The purged volume becomes permanently unavailable. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              help="""The ID of the volume to be deleted. """)
@pass_context
def delete(ctx,
           # Mandatory main parameter
           volumeid):
    """DeleteVolume marks an active volume for deletion. When marked, the volume is purged (permanently deleted) after the cleanup"""
    """interval elapses. After making a request to delete a volume, any active iSCSI connections to the volume are immediately terminated"""
    """and no further connections are allowed while the volume is in this state. A marked volume is not returned in target discovery"""
    """requests."""
    """Any snapshots of a volume that has been marked for deletion are not affected. Snapshots are kept until the volume is purged from"""
    """the system."""
    """If a volume is marked for deletion and has a bulk volume read or bulk volume write operation in progress, the bulk volume read or"""
    """write operation is stopped."""
    """If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred"""
    """to it or from it while in a deleted state. The remote volume that the deleted volume was paired with enters into a PausedMisconfigured state and data is no longer sent to it or from the deleted volume. Until the deleted volume is purged, it can be restored and data transfers resume. If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed. The purged volume becomes permanently unavailable."""
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

