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
    """modifyhost gettaskupdate unbindallfromhost modifymetadata modifyvasaproviderinfo getunsharedchunks querymetadata listtasks create fastclone canceltask getallocatedbitmap getunsharedbitmap listhosts rollback copydiffsto clone modify preparevirtualsnapshot getfeaturestatus unbind createhost bind list getvasaproviderinfo snapshot listbindings getcount enablefeature delete """

@cli.command('modifyhost', short_help="""ModifyVirtualVolumeHost changes an existing ESX host. """, cls=SolidFireCommand)
@click.option('--virtualvolumehostid',
              type=str,
              required=True,
              help="""The GUID of the ESX host. """)
@click.option('--clusterid',
              type=str,
              required=False,
              help="""The GUID of the ESX Cluster. """)
@click.option('--visibleprotocolendpointids',
              type=str,
              required=False,
              help="""A list of PEs the host is aware of. """)
@click.option('--initiatornames',
              type=str,
              required=False,
              help="""List of iSCSI initiator IQNs for the host. """)
@click.option('--hostaddress',
              type=str,
              required=False,
              help="""IP or DNS name for the host. """)
@pass_context
def modifyhost(ctx,
           # Mandatory main parameter
           virtualvolumehostid,
           # Optional main parameter
           clusterid = None,
           # Optional main parameter
           visibleprotocolendpointids = None,
           # Optional main parameter
           initiatornames = None,
           # Optional main parameter
           hostaddress = None):
    """ModifyVirtualVolumeHost changes an existing ESX host."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            

    visibleprotocolendpointids = parser.parse_array(visibleprotocolendpointids)    

    initiatornames = parser.parse_array(initiatornames)    
    

    ctx.logger.info("""virtualvolumehostid = """+str(virtualvolumehostid)+""";"""+"""clusterid = """+str(clusterid)+""";"""+"""visibleprotocolendpointids = """+str(visibleprotocolendpointids)+""";"""+"""initiatornames = """+str(initiatornames)+""";"""+"""hostaddress = """+str(hostaddress)+""";"""+"")
    try:
        _VirtualVolumeNullResult = ctx.element.modify_virtual_volume_host(virtual_volume_host_id=virtualvolumehostid, cluster_id=clusterid, visible_protocol_endpoint_ids=visibleprotocolendpointids, initiator_names=initiatornames, host_address=hostaddress)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeNullResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('gettaskupdate', short_help="""GetVirtualVolumeTaskUpdate checks the status of a VVol Async Task. """, cls=SolidFireCommand)
@click.option('--virtualvolumetaskid',
              type=str,
              required=True,
              help="""The UUID of the VVol Task. """)
@pass_context
def gettaskupdate(ctx,
           # Mandatory main parameter
           virtualvolumetaskid):
    """GetVirtualVolumeTaskUpdate checks the status of a VVol Async Task."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""virtualvolumetaskid = """+str(virtualvolumetaskid)+""";"""+"")
    try:
        _VirtualVolumeTaskResult = ctx.element.get_virtual_volume_task_update(virtual_volume_task_id=virtualvolumetaskid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeTaskResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('unbindallfromhost', short_help="""UnbindAllVirtualVolumesFromHost removes all VVol  Host binding. """, cls=SolidFireCommand)
@pass_context
def unbindallfromhost(ctx):
    """UnbindAllVirtualVolumesFromHost removes all VVol  Host binding."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _UnbindAllVirtualVolumesFromHostResult = ctx.element.unbind_all_virtual_volumes_from_host()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_UnbindAllVirtualVolumesFromHostResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifymetadata', short_help="""ModifyVirtualVolumeMetadata is used to selectively modify the VVol metadata. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""VvolVolumeID for the volume to be modified. """)
@pass_context
def modifymetadata(ctx,
           # Mandatory main parameter
           virtualvolumeid):
    """ModifyVirtualVolumeMetadata is used to selectively modify the VVol metadata."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"")
    try:
        _VirtualVolumeNullResult = ctx.element.modify_virtual_volume_metadata(virtual_volume_id=virtualvolumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeNullResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyvasaproviderinfo', short_help="""Update the Vasa Provider info """, cls=SolidFireCommand)
@click.option('--keystore',
              type=str,
              required=False,
              help="""Signed SSL certificate for the Vasa Provider """)
@click.option('--vasaproviderid',
              type=str,
              required=False,
              help="""UUID identifying the vasa provider """)
@pass_context
def modifyvasaproviderinfo(ctx,
           # Optional main parameter
           keystore = None,
           # Optional main parameter
           vasaproviderid = None):
    """Update the Vasa Provider info"""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

        
    

    ctx.logger.info("""keystore = """+str(keystore)+""";"""+"""vasaproviderid = """+str(vasaproviderid)+""";"""+"")
    try:
        _VirtualVolumeNullResult = ctx.element.modify_vasa_provider_info(keystore=keystore, vasa_provider_id=vasaproviderid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeNullResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getunsharedchunks', short_help="""GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of  chunks not shared between two volumes. This call will return results in less  than 30 seconds. If the specified VVol and the base VVil are not related, an  error is thrown. If the offset/length combination is invalid or out fo range  an error is thrown. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume. """)
@click.option('--basevirtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume to compare against. """)
@click.option('--segmentstart',
              type=int,
              required=True,
              help="""Start Byte offset. """)
@click.option('--segmentlength',
              type=int,
              required=True,
              help="""Length of the scan segment in bytes. """)
@click.option('--chunksize',
              type=int,
              required=True,
              help="""Number of bytes represented by one bit in the bitmap. """)
@pass_context
def getunsharedchunks(ctx,
           # Mandatory main parameter
           virtualvolumeid,
           # Mandatory main parameter
           basevirtualvolumeid,
           # Mandatory main parameter
           segmentstart,
           # Mandatory main parameter
           segmentlength,
           # Mandatory main parameter
           chunksize):
    """GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of """
    """chunks not shared between two volumes. This call will return results in less """
    """than 30 seconds. If the specified VVol and the base VVil are not related, an """
    """error is thrown. If the offset/length combination is invalid or out fo range """
    """an error is thrown."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                    
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"""basevirtualvolumeid = """+str(basevirtualvolumeid)+""";"""+"""segmentstart = """+str(segmentstart)+""";"""+"""segmentlength = """+str(segmentlength)+""";"""+"""chunksize = """+str(chunksize)+""";"""+"")
    try:
        _VirtualVolumeUnsharedChunkResult = ctx.element.get_virtual_volume_unshared_chunks(virtual_volume_id=virtualvolumeid, base_virtual_volume_id=basevirtualvolumeid, segment_start=segmentstart, segment_length=segmentlength, chunk_size=chunksize)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeUnsharedChunkResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('querymetadata', short_help="""QueryVirtualVolumeMetadata returns a list of VVols matching a metadata query. """, cls=SolidFireCommand)
@pass_context
def querymetadata(ctx):
    """QueryVirtualVolumeMetadata returns a list of VVols matching a metadata query."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _QueryVirtualVolumeMetadataResult = ctx.element.query_virtual_volume_metadata()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_QueryVirtualVolumeMetadataResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listtasks', short_help="""ListVirtualVolumeTasks returns a list of virtual volume tasks in the system. """, cls=SolidFireCommand)
@click.option('--virtualvolumetaskids',
              type=str,
              required=False,
              help="""A list of virtual volume task IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume tasks. """)
@pass_context
def listtasks(ctx,
           # Optional main parameter
           virtualvolumetaskids = None):
    """ListVirtualVolumeTasks returns a list of virtual volume tasks in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    virtualvolumetaskids = parser.parse_array(virtualvolumetaskids)
    

    ctx.logger.info("""virtualvolumetaskids = """+str(virtualvolumetaskids)+""";"""+"")
    try:
        _ListVirtualVolumeTasksResult = ctx.element.list_virtual_volume_tasks(virtual_volume_task_ids=virtualvolumetaskids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVirtualVolumeTasksResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateVirtualVolume is used to create a new (empty) Virtual Volume on the cluster. When the volume is created successfully it is available for connection via PE. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              help="""Name of the Virtual Volume. Not required to be unique, but it is recommended. May be 1 to 64 characters in length. """)
@click.option('--storagecontainerid',
              type=str,
              required=True,
              help="""UUID for the Storage Container of this volume. """)
@click.option('--virtualvolumetype',
              type=str,
              required=True,
              help="""VMW_TYPE value for this volume. """)
@click.option('--totalsize',
              type=int,
              required=True,
              help="""Total size of the volume, in bytes. Size is rounded up to the nearest 1MB size. """)

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
@click.option('--metadata',
              type=str,
              required=False,
              help="""List of name/value pairs to save in the volume's metadata.  Has the following subparameters: """)
@pass_context
def create(ctx,
           # Mandatory main parameter
           name,
           # Mandatory main parameter
           storagecontainerid,
           # Mandatory main parameter
           virtualvolumetype,
           # Mandatory main parameter
           totalsize,
           # Optional subparameter of optional main parameter.
           qosminiops = None,
           # Optional subparameter of optional main parameter.
           qosmaxiops = None,
           # Optional subparameter of optional main parameter.
           qosburstiops = None,
           # Optional subparameter of optional main parameter.
           qosbursttime = None,
           # Optional main parameter
           metadata = None):
    """CreateVirtualVolume is used to create a new (empty) Virtual Volume on the cluster."""
    """When the volume is created successfully it is available for connection via PE."""
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

    if(metadata is not None):
        try:
            kwargsDict = simplejson.loads(metadata)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""name = """+str(name)+""";"""+"""storagecontainerid = """+str(storagecontainerid)+""";"""+"""virtualvolumetype = """+str(virtualvolumetype)+""";"""+"""totalsize = """+str(totalsize)+""";"""+"""qos = """+str(qos)+""";"""+"""metadata = """+str(metadata)+""";"""+"")
    try:
        _VirtualVolumeSyncResult = ctx.element.create_virtual_volume(name=name, storage_container_id=storagecontainerid, virtual_volume_type=virtualvolumetype, total_size=totalsize, qos=qos, metadata=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeSyncResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('fastclone', short_help="""FastCloneVirtualVolume is used to execute a VMware Virtual Volume fast clone. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume to clone. """)
@click.option('--name',
              type=str,
              required=False,
              help="""The name for the newly-created volume. """)

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
@pass_context
def fastclone(ctx,
           # Mandatory main parameter
           virtualvolumeid,
           # Optional main parameter
           name = None,
           # Optional subparameter of optional main parameter.
           qosminiops = None,
           # Optional subparameter of optional main parameter.
           qosmaxiops = None,
           # Optional subparameter of optional main parameter.
           qosburstiops = None,
           # Optional subparameter of optional main parameter.
           qosbursttime = None):
    """FastCloneVirtualVolume is used to execute a VMware Virtual Volume fast clone."""
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
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"""name = """+str(name)+""";"""+"""qos = """+str(qos)+""";"""+"")
    try:
        _VirtualVolumeAsyncResult = ctx.element.fast_clone_virtual_volume(virtual_volume_id=virtualvolumeid, name=name, qos=qos)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeAsyncResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('canceltask', short_help="""CancelVirtualVolumeTask attempts to cancel the VVol Async Task. """, cls=SolidFireCommand)
@click.option('--virtualvolumetaskid',
              type=str,
              required=True,
              help="""The UUID of the VVol Task to cancel. """)
@pass_context
def canceltask(ctx,
           # Mandatory main parameter
           virtualvolumetaskid):
    """CancelVirtualVolumeTask attempts to cancel the VVol Async Task."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""virtualvolumetaskid = """+str(virtualvolumetaskid)+""";"""+"")
    try:
        _VirtualVolumeNullResult = ctx.element.cancel_virtual_volume_task(virtual_volume_task_id=virtualvolumetaskid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeNullResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getallocatedbitmap', short_help="""GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data  representing a bitmap where non-zero bits indicate the allocation of a  segment (LBA range) of the volume. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume. """)
@click.option('--segmentstart',
              type=int,
              required=True,
              help="""Byte offset. """)
@click.option('--segmentlength',
              type=int,
              required=True,
              help="""Byte length adjusted to end on a chunk boundary. """)
@click.option('--chunksize',
              type=int,
              required=True,
              help="""Number of bytes represented by one bit in the bitmap. """)
@pass_context
def getallocatedbitmap(ctx,
           # Mandatory main parameter
           virtualvolumeid,
           # Mandatory main parameter
           segmentstart,
           # Mandatory main parameter
           segmentlength,
           # Mandatory main parameter
           chunksize):
    """GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data """
    """representing a bitmap where non-zero bits indicate the allocation of a """
    """segment (LBA range) of the volume."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"""segmentstart = """+str(segmentstart)+""";"""+"""segmentlength = """+str(segmentlength)+""";"""+"""chunksize = """+str(chunksize)+""";"""+"")
    try:
        _VirtualVolumeBitmapResult = ctx.element.get_virtual_volume_allocated_bitmap(virtual_volume_id=virtualvolumeid, segment_start=segmentstart, segment_length=segmentlength, chunk_size=chunksize)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeBitmapResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getunsharedbitmap', short_help="""GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data  representing a bitmap where non-zero bits indicate that data is not the same  between two volumes for a common segment (LBA range) of the volumes. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume. """)
@click.option('--basevirtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume to compare against. """)
@click.option('--segmentstart',
              type=int,
              required=True,
              help="""Byte offset. """)
@click.option('--segmentlength',
              type=int,
              required=True,
              help="""Byte length adjusted to end on a chunk boundary. """)
@click.option('--chunksize',
              type=int,
              required=True,
              help="""Number of bytes represented by one bit in the bitmap. """)
@pass_context
def getunsharedbitmap(ctx,
           # Mandatory main parameter
           virtualvolumeid,
           # Mandatory main parameter
           basevirtualvolumeid,
           # Mandatory main parameter
           segmentstart,
           # Mandatory main parameter
           segmentlength,
           # Mandatory main parameter
           chunksize):
    """GetVirtualVolumeAllocatedBitmap returns a b64-encoded block of data """
    """representing a bitmap where non-zero bits indicate that data is not the same """
    """between two volumes for a common segment (LBA range) of the volumes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                    
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"""basevirtualvolumeid = """+str(basevirtualvolumeid)+""";"""+"""segmentstart = """+str(segmentstart)+""";"""+"""segmentlength = """+str(segmentlength)+""";"""+"""chunksize = """+str(chunksize)+""";"""+"")
    try:
        _VirtualVolumeBitmapResult = ctx.element.get_virtual_volume_unshared_bitmap(virtual_volume_id=virtualvolumeid, base_virtual_volume_id=basevirtualvolumeid, segment_start=segmentstart, segment_length=segmentlength, chunk_size=chunksize)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeBitmapResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listhosts', short_help="""ListVirtualVolumeHosts returns a list of all virtual volume hosts known to the cluster. A virtual volume host is a VMware ESX host that has initiated a session with the VASA API provider. """, cls=SolidFireCommand)
@click.option('--virtualvolumehostids',
              type=str,
              required=False,
              help="""A list of virtual volume host IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume hosts. """)
@pass_context
def listhosts(ctx,
           # Optional main parameter
           virtualvolumehostids = None):
    """ListVirtualVolumeHosts returns a list of all virtual volume hosts known to the cluster. A virtual volume host is a VMware ESX host"""
    """that has initiated a session with the VASA API provider."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    virtualvolumehostids = parser.parse_array(virtualvolumehostids)
    

    ctx.logger.info("""virtualvolumehostids = """+str(virtualvolumehostids)+""";"""+"")
    try:
        _ListVirtualVolumeHostsResult = ctx.element.list_virtual_volume_hosts(virtual_volume_host_ids=virtualvolumehostids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVirtualVolumeHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('rollback', short_help="""RollbackVirtualVolume is used to restore a VMware Virtual Volume snapshot. """, cls=SolidFireCommand)
@click.option('--srcvirtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume snapshot. """)
@click.option('--dstvirtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume to restore to. """)
@pass_context
def rollback(ctx,
           # Mandatory main parameter
           srcvirtualvolumeid,
           # Mandatory main parameter
           dstvirtualvolumeid):
    """RollbackVirtualVolume is used to restore a VMware Virtual Volume snapshot."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

        
    

    ctx.logger.info("""srcvirtualvolumeid = """+str(srcvirtualvolumeid)+""";"""+"""dstvirtualvolumeid = """+str(dstvirtualvolumeid)+""";"""+"")
    try:
        _VirtualVolumeAsyncResult = ctx.element.rollback_virtual_volume(src_virtual_volume_id=srcvirtualvolumeid, dst_virtual_volume_id=dstvirtualvolumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeAsyncResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('copydiffsto', short_help="""CopyDiffsToVirtualVolume is a three-way merge function. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the snapshot Virtual Volume. """)
@click.option('--basevirtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the base Virtual Volume. """)
@click.option('--dstvirtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume to be overwritten. """)
@pass_context
def copydiffsto(ctx,
           # Mandatory main parameter
           virtualvolumeid,
           # Mandatory main parameter
           basevirtualvolumeid,
           # Mandatory main parameter
           dstvirtualvolumeid):
    """CopyDiffsToVirtualVolume is a three-way merge function."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"""basevirtualvolumeid = """+str(basevirtualvolumeid)+""";"""+"""dstvirtualvolumeid = """+str(dstvirtualvolumeid)+""";"""+"")
    try:
        _VirtualVolumeAsyncResult = ctx.element.copy_diffs_to_virtual_volume(virtual_volume_id=virtualvolumeid, base_virtual_volume_id=basevirtualvolumeid, dst_virtual_volume_id=dstvirtualvolumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeAsyncResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('clone', short_help="""CloneVirtualVolume is used to execute a VMware Virtual Volume clone. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume to clone. """)
@click.option('--name',
              type=str,
              required=False,
              help="""The name for the newly-created volume. """)

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
@pass_context
def clone(ctx,
           # Mandatory main parameter
           virtualvolumeid,
           # Optional main parameter
           name = None,
           # Optional subparameter of optional main parameter.
           qosminiops = None,
           # Optional subparameter of optional main parameter.
           qosmaxiops = None,
           # Optional subparameter of optional main parameter.
           qosburstiops = None,
           # Optional subparameter of optional main parameter.
           qosbursttime = None):
    """CloneVirtualVolume is used to execute a VMware Virtual Volume clone."""
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
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"""name = """+str(name)+""";"""+"""qos = """+str(qos)+""";"""+"")
    try:
        _VirtualVolumeAsyncResult = ctx.element.clone_virtual_volume(virtual_volume_id=virtualvolumeid, name=name, qos=qos)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeAsyncResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""ModifyVirtualVolume is used to modify settings on an existing virtual volume. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""VvolVolumeID for the volume to be modified. """)

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
@pass_context
def modify(ctx,
           # Mandatory main parameter
           virtualvolumeid,
           # Optional subparameter of optional main parameter.
           qosminiops = None,
           # Optional subparameter of optional main parameter.
           qosmaxiops = None,
           # Optional subparameter of optional main parameter.
           qosburstiops = None,
           # Optional subparameter of optional main parameter.
           qosbursttime = None,
           # Optional main parameter
           totalsize = None):
    """ModifyVirtualVolume is used to modify settings on an existing virtual volume."""
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
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"""qos = """+str(qos)+""";"""+"""totalsize = """+str(totalsize)+""";"""+"")
    try:
        _VirtualVolumeNullResult = ctx.element.modify_virtual_volume(virtual_volume_id=virtualvolumeid, qos=qos, total_size=totalsize)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeNullResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('preparevirtualsnapshot', short_help="""PrepareVirtualSnapshot is used to set up VMware Virtual Volume snapshot. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume to clone. """)
@click.option('--name',
              type=str,
              required=False,
              help="""The name for the newly-created volume. """)
@click.option('--writablesnapshot',
              type=bool,
              required=False,
              help="""Will the snapshot be writable? """)
@pass_context
def preparevirtualsnapshot(ctx,
           # Mandatory main parameter
           virtualvolumeid,
           # Optional main parameter
           name = None,
           # Optional main parameter
           writablesnapshot = None):
    """PrepareVirtualSnapshot is used to set up VMware Virtual Volume snapshot."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"""name = """+str(name)+""";"""+"""writablesnapshot = """+str(writablesnapshot)+""";"""+"")
    try:
        _PrepareVirtualSnapshotResult = ctx.element.prepare_virtual_snapshot(virtual_volume_id=virtualvolumeid, name=name, writable_snapshot=writablesnapshot)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_PrepareVirtualSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getfeaturestatus', short_help="""GetFeatureStatus enables you to retrieve the status of a cluster feature. """, cls=SolidFireCommand)
@click.option('--feature',
              type=str,
              required=False,
              help="""Specifies the feature for which the status is returned. Valid value is: vvols: Retrieve status for the NetApp SolidFire VVols cluster feature. """)
@pass_context
def getfeaturestatus(ctx,
           # Optional main parameter
           feature = None):
    """GetFeatureStatus enables you to retrieve the status of a cluster feature."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        _GetFeatureStatusResult = ctx.element.get_feature_status(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetFeatureStatusResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('unbind', short_help="""UnbindGetVirtualVolume removes the VVol  Host binding. """, cls=SolidFireCommand)
@click.option('--unbindcontext',
              type=str,
              required=True,
              help="""Normal, Start, or End? """)
@pass_context
def unbind(ctx,
           # Mandatory main parameter
           unbindcontext):
    """UnbindGetVirtualVolume removes the VVol  Host binding."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""unbindcontext = """+str(unbindcontext)+""";"""+"")
    try:
        _VirtualVolumeUnbindResult = ctx.element.unbind_virtual_volumes(unbind_context=unbindcontext)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeUnbindResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createhost', short_help="""CreateVirtualVolumeHost creates a new ESX host. """, cls=SolidFireCommand)
@click.option('--virtualvolumehostid',
              type=str,
              required=True,
              help="""The GUID of the ESX host. """)
@click.option('--clusterid',
              type=str,
              required=True,
              help="""The GUID of the ESX Cluster. """)
@click.option('--visibleprotocolendpointids',
              type=str,
              required=False,
              help="""A list of PEs the host is aware of. """)
@click.option('--hostaddress',
              type=str,
              required=False,
              help="""IP or DNS name for the host. """)
@pass_context
def createhost(ctx,
           # Mandatory main parameter
           virtualvolumehostid,
           # Mandatory main parameter
           clusterid,
           # Optional main parameter
           visibleprotocolendpointids = None,
           # Optional main parameter
           hostaddress = None):
    """CreateVirtualVolumeHost creates a new ESX host."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            

    visibleprotocolendpointids = parser.parse_array(visibleprotocolendpointids)    
    

    ctx.logger.info("""virtualvolumehostid = """+str(virtualvolumehostid)+""";"""+"""clusterid = """+str(clusterid)+""";"""+"""visibleprotocolendpointids = """+str(visibleprotocolendpointids)+""";"""+"""hostaddress = """+str(hostaddress)+""";"""+"")
    try:
        _VirtualVolumeNullResult = ctx.element.create_virtual_volume_host(virtual_volume_host_id=virtualvolumehostid, cluster_id=clusterid, visible_protocol_endpoint_ids=visibleprotocolendpointids, host_address=hostaddress)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeNullResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('bind', short_help="""BindVirtualVolume binds a VVol with a Host. """, cls=SolidFireCommand)
@click.option('--virtualvolumeids',
              type=str,
              required=True,
              help="""The UUID of the VVol to bind. """)
@click.option('--virtualvolumehostid',
              type=str,
              required=True,
              help="""The UUID of the ESX host. """)
@click.option('--bindcontext',
              type=str,
              required=True,
              help="""Normal or Start? """)
@pass_context
def bind(ctx,
           # Mandatory main parameter
           virtualvolumeids,
           # Mandatory main parameter
           virtualvolumehostid,
           # Mandatory main parameter
           bindcontext):
    """BindVirtualVolume binds a VVol with a Host."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    virtualvolumeids = parser.parse_array(virtualvolumeids)        
    

    ctx.logger.info("""virtualvolumeids = """+str(virtualvolumeids)+""";"""+"""virtualvolumehostid = """+str(virtualvolumehostid)+""";"""+"""bindcontext = """+str(bindcontext)+""";"""+"")
    try:
        _VirtualVolumeBindingListResult = ctx.element.bind_virtual_volumes(virtual_volume_ids=virtualvolumeids, virtual_volume_host_id=virtualvolumehostid, bind_context=bindcontext)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeBindingListResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset. """, cls=SolidFireCommand)
@click.option('--details',
              type=bool,
              required=False,
              help="""Specifies the level of detail about each virtual volume that is returned. Possible values are: true: Include more details about each virtual volume in the response. false: Include the standard level of detail about each virtual volume in the response. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of virtual volumes to list. """)
@click.option('--recursive',
              type=bool,
              required=False,
              help="""Specifies whether to include information about the children of each virtual volume in the response. Possible values are: true: Include information about the children of each virtual volume in the response. false: Do not include information about the children of each virtual volume in the response. """)
@click.option('--startvirtualvolumeid',
              type=str,
              required=False,
              help="""The ID of the virtual volume at which to begin the list. """)
@click.option('--virtualvolumeids',
              type=str,
              required=False,
              help="""A list of virtual volume IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
def list(ctx,
           # Optional main parameter
           details = None,
           # Optional main parameter
           limit = None,
           # Optional main parameter
           recursive = None,
           # Optional main parameter
           startvirtualvolumeid = None,
           # Optional main parameter
           virtualvolumeids = None):
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes,"""
    """or only list a subset."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                    

    virtualvolumeids = parser.parse_array(virtualvolumeids)
    

    ctx.logger.info("""details = """+str(details)+""";"""+"""limit = """+str(limit)+""";"""+"""recursive = """+str(recursive)+""";"""+"""startvirtualvolumeid = """+str(startvirtualvolumeid)+""";"""+"""virtualvolumeids = """+str(virtualvolumeids)+""";"""+"")
    try:
        _ListVirtualVolumesResult = ctx.element.list_virtual_volumes(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=startvirtualvolumeid, virtual_volume_ids=virtualvolumeids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVirtualVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getvasaproviderinfo', short_help="""Gets the Vasa Provider info """, cls=SolidFireCommand)
@pass_context
def getvasaproviderinfo(ctx):
    """Gets the Vasa Provider info"""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _VasaProviderInfoResult = ctx.element.get_vasa_provider_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VasaProviderInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('snapshot', short_help="""SnapshotVirtualVolume is used to take a VMware Virtual Volume snapshot. """, cls=SolidFireCommand)
@click.option('--virtualvolumeid',
              type=str,
              required=True,
              help="""The ID of the Virtual Volume to clone. """)
@click.option('--timeout',
              type=int,
              required=True,
              help="""Number of seconds to complete or fail. """)
@pass_context
def snapshot(ctx,
           # Mandatory main parameter
           virtualvolumeid,
           # Mandatory main parameter
           timeout):
    """SnapshotVirtualVolume is used to take a VMware Virtual Volume snapshot."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

        
    

    ctx.logger.info("""virtualvolumeid = """+str(virtualvolumeid)+""";"""+"""timeout = """+str(timeout)+""";"""+"")
    try:
        _SnapshotVirtualVolumeResult = ctx.element.snapshot_virtual_volume(virtual_volume_id=virtualvolumeid, timeout=timeout)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_SnapshotVirtualVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listbindings', short_help="""ListVirtualVolumeBindings returns a list of all virtual volumes in the cluster that are bound to protocol endpoints. """, cls=SolidFireCommand)
@click.option('--virtualvolumebindingids',
              type=str,
              required=False,
              help="""A list of virtual volume binding IDs for which to retrieve information. If you omit this parameter, the method returns information about all virtual volume bindings. """)
@pass_context
def listbindings(ctx,
           # Optional main parameter
           virtualvolumebindingids = None):
    """ListVirtualVolumeBindings returns a list of all virtual volumes in the cluster that are bound to protocol endpoints."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    virtualvolumebindingids = parser.parse_array(virtualvolumebindingids)
    

    ctx.logger.info("""virtualvolumebindingids = """+str(virtualvolumebindingids)+""";"""+"")
    try:
        _ListVirtualVolumeBindingsResult = ctx.element.list_virtual_volume_bindings(virtual_volume_binding_ids=virtualvolumebindingids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVirtualVolumeBindingsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getcount', short_help="""Enables retrieval of the number of virtual volumes currently in the system. """, cls=SolidFireCommand)
@pass_context
def getcount(ctx):
    """Enables retrieval of the number of virtual volumes currently in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _GetVirtualVolumeCountResult = ctx.element.get_virtual_volume_count()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetVirtualVolumeCountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enablefeature', short_help="""You can use EnableFeature to enable cluster features that are disabled by default. """, cls=SolidFireCommand)
@click.option('--feature',
              type=str,
              required=True,
              help="""Indicates which feature to enable. Valid value is: vvols: Enable the NetApp SolidFire VVols cluster feature. """)
@pass_context
def enablefeature(ctx,
           # Mandatory main parameter
           feature):
    """You can use EnableFeature to enable cluster features that are disabled by default."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        _EnableFeatureResult = ctx.element.enable_feature(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_EnableFeatureResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""DeleteVirtualVolume marks an active volume for deletion. It is purged (permanently deleted) after the cleanup interval elapses. After making a request to delete a volume, any active iSCSI connections to the volume is immediately terminated and no further connections are allowed while the volume is in this state. It is not returned in target discovery requests.  Any snapshots of a volume that has been marked to delete are not affected. Snapshots are kept until the volume is purged from the system.  If a volume is marked for deletion, and it has a bulk volume read or bulk volume write operation in progress, the bulk volume operation is stopped.  If the volume you delete is paired with a volume, replication between the paired volumes is suspended and no data is transferred to it or from it while in a deleted state. The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no integerer sent to it or from the deleted volume. Until the deleted volume is purged, it can be restored and data transfers resumes. If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed. The purged volume becomes permanently unavailable. """, cls=SolidFireCommand)
@click.option('--virtualvolumes',
              type=str,
              required=True,
              help="""The UUID of the volume to delete. """)
@pass_context
def delete(ctx,
           # Mandatory main parameter
           virtualvolumes):
    """DeleteVirtualVolume marks an active volume for deletion."""
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
    """The remote volume the deleted volume was paired with enters into a PausedMisconfigured state and data is no integerer sent to it or from the deleted volume."""
    """Until the deleted volume is purged, it can be restored and data transfers resumes."""
    """If the deleted volume gets purged from the system, the volume it was paired with enters into a StoppedMisconfigured state and the volume pairing status is removed."""
    """The purged volume becomes permanently unavailable."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    virtualvolumes = parser.parse_array(virtualvolumes)
    

    ctx.logger.info("""virtualvolumes = """+str(virtualvolumes)+""";"""+"")
    try:
        _VirtualVolumeNullResult = ctx.element.delete_virtual_volumes(virtual_volumes=virtualvolumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_VirtualVolumeNullResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

