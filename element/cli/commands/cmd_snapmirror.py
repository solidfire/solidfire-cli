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
    """deleteendpoints resumerelationship initializerelationship createvolume listvolumes listrelationships abortrelationship listschedules quiescerelationship listluns modifyrelationship listendpoints listpolicies createendpoint getclusteridentity modifyendpoint listnetworkinterfaces listaggregates resyncrelationship listvservers modifyendpointunmanaged deleterelationships listnodes breakvolume getontapversioninfo createendpointunmanaged breakrelationship updaterelationship createrelationship """

@cli.command('deleteendpoints', short_help="""The SolidFire Element OS web UI uses DeleteSnapMirrorEndpoints to delete one or more SnapMirror endpoints from the system. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointids',
              type=str,
              required=True,
              prompt=True,
              help="""An array of IDs of SnapMirror endpoints to delete. """)
@pass_context
def deleteendpoints(ctx,
           # Mandatory main parameter
           snapmirrorendpointids):
    """The SolidFire Element OS web UI uses DeleteSnapMirrorEndpoints to delete one or more SnapMirror endpoints from the system."""

    

    cli_utils.establish_connection(ctx)
    

    snapmirrorendpointids = parser.parse_array(snapmirrorendpointids)
    

    ctx.logger.info(""": """"""snapmirrorendpointids = """ + str(snapmirrorendpointids)+""";"""+"")
    try:
        _DeleteSnapMirrorEndpointsResult = ctx.element.delete_snap_mirror_endpoints(snap_mirror_endpoint_ids=snapmirrorendpointids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteSnapMirrorEndpointsResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteSnapMirrorEndpointsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('resumerelationship', short_help="""The SolidFire Element OS web UI uses the ResumeSnapMirrorRelationship method to enable future transfers for a quiesced SnapMirror relationship. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)

@click.option('--type',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@pass_context
def resumerelationship(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           type,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserver,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name):
    """The SolidFire Element OS web UI uses the ResumeSnapMirrorRelationship method to enable future transfers for a quiesced SnapMirror relationship."""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(type is not None or
       volumeid is not None or
       vserver is not None or
       name is not None or
       False):
        if not (type and volumeid and vserver and name and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
type
volumeid
vserver
name
""")
        kwargsDict = dict()
        kwargsDict["type"] = type
        kwargsDict["volume_id"] = volumeid
        kwargsDict["vserver"] = vserver
        kwargsDict["name"] = name

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""destinationvolume = """ + str(destinationvolume)+""";"""+"")
    try:
        _ResumeSnapMirrorRelationshipResult = ctx.element.resume_snap_mirror_relationship(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ResumeSnapMirrorRelationshipResult), indent=4))
        return
    else:
        cli_utils.print_result(_ResumeSnapMirrorRelationshipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('initializerelationship', short_help="""The SolidFire Element OS web UI uses the InitializeSnapMirrorRelationship method to initialize the destination volume in a SnapMirror relationship by performing an initial baseline transfer between clusters. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the remote ONTAP system. """)

@click.option('--type',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@click.option('--maxtransferrate',
              type=int,
              required=False,
              help="""Specifies the maximum data transfer rate between the volumes in kilobytes per second. The default value, 0, is unlimited and permits the SnapMirror relationship to fully utilize the available network bandwidth. """)
@pass_context
def initializerelationship(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           type,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserver,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name,
           # Optional main parameter
           maxtransferrate = None):
    """The SolidFire Element OS web UI uses the InitializeSnapMirrorRelationship method to initialize the destination volume in a SnapMirror relationship by performing an initial baseline transfer between clusters."""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(type is not None or
       volumeid is not None or
       vserver is not None or
       name is not None or
       False):
        if not (type and volumeid and vserver and name and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
type
volumeid
vserver
name
""")
        kwargsDict = dict()
        kwargsDict["type"] = type
        kwargsDict["volume_id"] = volumeid
        kwargsDict["vserver"] = vserver
        kwargsDict["name"] = name

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""destinationvolume = """ + str(destinationvolume)+";" + """maxtransferrate = """+str(maxtransferrate)+""";"""+"")
    try:
        _InitializeSnapMirrorRelationshipResult = ctx.element.initialize_snap_mirror_relationship(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume, max_transfer_rate=maxtransferrate)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_InitializeSnapMirrorRelationshipResult), indent=4))
        return
    else:
        cli_utils.print_result(_InitializeSnapMirrorRelationshipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createvolume', short_help="""The SolidFire Element OS web UI uses the CreateSnapMirrorVolume method to create a volume on the remote ONTAP system. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)
@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver. """)
@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The destination ONTAP volume name. """)
@click.option('--type',
              type=str,
              required=False,
              help="""The volume type. Possible values: rw: Read-write volume ls: Load-sharing volume dp: Data protection volume If no type is provided the default type is dp. """)
@click.option('--aggregate',
              type=str,
              required=True,
              prompt=True,
              help="""The containing ONTAP aggregate in which to create the volume. You can use ListSnapMirrorAggregates to get information about available ONTAP aggregates. """)
@click.option('--size',
              type=int,
              required=True,
              prompt=True,
              help="""The size of the volume in bytes. """)
@pass_context
def createvolume(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory main parameter
           vserver,
           # Mandatory main parameter
           name,
           # Mandatory main parameter
           aggregate,
           # Mandatory main parameter
           size,
           # Optional main parameter
           type = None):
    """The SolidFire Element OS web UI uses the CreateSnapMirrorVolume method to create a volume on the remote ONTAP system."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""vserver = """ + str(vserver)+";"+"""name = """ + str(name)+";"+"""aggregate = """ + str(aggregate)+";"+"""size = """ + str(size)+";" + """type = """+str(type)+""";"""+"")
    try:
        _CreateSnapMirrorVolumeResult = ctx.element.create_snap_mirror_volume(snap_mirror_endpoint_id=snapmirrorendpointid, vserver=vserver, name=name, aggregate=aggregate, size=size, type=type)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateSnapMirrorVolumeResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateSnapMirrorVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listvolumes', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorVolumes method to list all SnapMirror volumes available on a remote ONTAP system. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""List only the volumes associated with the specified endpoint ID. If no endpoint ID is provided, the system lists volumes from all known SnapMirror endpoints. """)
@click.option('--vserver',
              type=str,
              required=False,
              help="""List volumes hosted on the specified Vserver. The Vserver must be of type "data". """)
@click.option('--name',
              type=str,
              required=False,
              help="""List only ONTAP volumes with the specified name. """)
@click.option('--type',
              type=str,
              required=False,
              help="""List only ONTAP volumes of the specified type. Possible values: rw: Read-write volumes ls: Load-sharing volumes dp: Data protection volumes """)
@pass_context
def listvolumes(ctx,
           # Optional main parameter
           snapmirrorendpointid = None,
           # Optional main parameter
           vserver = None,
           # Optional main parameter
           name = None,
           # Optional main parameter
           type = None):
    """The SolidFire Element OS web UI uses the ListSnapMirrorVolumes method to list all SnapMirror volumes available on a remote ONTAP system."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+";" + """vserver = """+str(vserver)+";" + """name = """+str(name)+";" + """type = """+str(type)+""";"""+"")
    try:
        _ListSnapMirrorVolumesResult = ctx.element.list_snap_mirror_volumes(snap_mirror_endpoint_id=snapmirrorendpointid, vserver=vserver, name=name, type=type)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorVolumesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listrelationships', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorRelationships method to list one or all SnapMirror relationships on a SolidFire cluster """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""List only the relationships associated with the specified endpoint ID. If no endpoint ID is provided, the system lists relationships from all known SnapMirror endpoints. """)

@click.option('--typedestinationvolume',
              type=str,
              required=False,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeiddestinationvolume',
              type=int,
              required=False,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserverdestinationvolume',
              type=str,
              required=False,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--namedestinationvolume',
              type=str,
              required=False,
              help="""The name of the volume. """)

@click.option('--typesourcevolume',
              type=str,
              required=False,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeidsourcevolume',
              type=int,
              required=False,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserversourcevolume',
              type=str,
              required=False,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--namesourcevolume',
              type=str,
              required=False,
              help="""The name of the volume. """)
@click.option('--vserver',
              type=str,
              required=False,
              help="""List relationships on the specified Vserver. """)
@click.option('--relationshipid',
              type=str,
              required=False,
              help="""List relationships associated with the specified relationshipID. """)
@pass_context
def listrelationships(ctx,
           # Optional main parameter
           snapmirrorendpointid = None,
           # Optional subparameter of optional main parameter.
           typedestinationvolume = None,
           # Optional subparameter of optional main parameter.
           volumeiddestinationvolume = None,
           # Optional subparameter of optional main parameter.
           vserverdestinationvolume = None,
           # Optional subparameter of optional main parameter.
           namedestinationvolume = None,
           # Optional subparameter of optional main parameter.
           typesourcevolume = None,
           # Optional subparameter of optional main parameter.
           volumeidsourcevolume = None,
           # Optional subparameter of optional main parameter.
           vserversourcevolume = None,
           # Optional subparameter of optional main parameter.
           namesourcevolume = None,
           # Optional main parameter
           vserver = None,
           # Optional main parameter
           relationshipid = None):
    """The SolidFire Element OS web UI uses the ListSnapMirrorRelationships method to list one or all SnapMirror relationships on a SolidFire cluster"""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(typedestinationvolume is not None or
       volumeiddestinationvolume is not None or
       vserverdestinationvolume is not None or
       namedestinationvolume is not None or
       False):
        if not (typedestinationvolume and volumeiddestinationvolume and vserverdestinationvolume and namedestinationvolume and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
typedestinationvolume
volumeiddestinationvolume
vserverdestinationvolume
namedestinationvolume
""")
        kwargsDict = dict()
        kwargsDict["type"] = typedestinationvolume
        kwargsDict["volume_id"] = volumeiddestinationvolume
        kwargsDict["vserver"] = vserverdestinationvolume
        kwargsDict["name"] = namedestinationvolume

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    

    sourcevolume = None
    if(typesourcevolume is not None or
       volumeidsourcevolume is not None or
       vserversourcevolume is not None or
       namesourcevolume is not None or
       False):
        if not (typesourcevolume and volumeidsourcevolume and vserversourcevolume and namesourcevolume and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
typesourcevolume
volumeidsourcevolume
vserversourcevolume
namesourcevolume
""")
        kwargsDict = dict()
        kwargsDict["type"] = typesourcevolume
        kwargsDict["volume_id"] = volumeidsourcevolume
        kwargsDict["vserver"] = vserversourcevolume
        kwargsDict["name"] = namesourcevolume

        sourcevolume = SnapMirrorVolumeInfo(**kwargsDict)
    
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+";" + """destinationvolume = """+str(destinationvolume)+";" + """sourcevolume = """+str(sourcevolume)+";" + """vserver = """+str(vserver)+";" + """relationshipid = """+str(relationshipid)+""";"""+"")
    try:
        _ListSnapMirrorRelationshipsResult = ctx.element.list_snap_mirror_relationships(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume, source_volume=sourcevolume, vserver=vserver, relationship_id=relationshipid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorRelationshipsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorRelationshipsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('abortrelationship', short_help="""The SolidFire Element OS web UI uses the AbortSnapMirrorRelationship method to stop SnapMirror transfers that have started but are not yet complete. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)

@click.option('--type',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@click.option('--clearcheckpoint',
              type=bool,
              required=False,
              help="""Determines whether or not to clear the restart checkpoint. """)
@pass_context
def abortrelationship(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           type,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserver,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name,
           # Optional main parameter
           clearcheckpoint = None):
    """The SolidFire Element OS web UI uses the AbortSnapMirrorRelationship method to stop SnapMirror transfers that have started but are not yet complete."""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(type is not None or
       volumeid is not None or
       vserver is not None or
       name is not None or
       False):
        if not (type and volumeid and vserver and name and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
type
volumeid
vserver
name
""")
        kwargsDict = dict()
        kwargsDict["type"] = type
        kwargsDict["volume_id"] = volumeid
        kwargsDict["vserver"] = vserver
        kwargsDict["name"] = name

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""destinationvolume = """ + str(destinationvolume)+";" + """clearcheckpoint = """+str(clearcheckpoint)+""";"""+"")
    try:
        _AbortSnapMirrorRelationshipResult = ctx.element.abort_snap_mirror_relationship(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume, clear_checkpoint=clearcheckpoint)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_AbortSnapMirrorRelationshipResult), indent=4))
        return
    else:
        cli_utils.print_result(_AbortSnapMirrorRelationshipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listschedules', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorSchedules method to get a list of schedules that are available on a remote ONTAP cluster. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""If provided, the system lists the schedules of the endpoint with the specified SnapMirror endpoint ID. If not provided, the system lists the schedules of all known SnapMirror endpoints. """)
@pass_context
def listschedules(ctx,
           # Optional main parameter
           snapmirrorendpointid = None):
    """The SolidFire Element OS web UI uses the ListSnapMirrorSchedules method to get a list of schedules that are available on a remote ONTAP cluster."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+""";"""+"")
    try:
        _ListSnapMirrorSchedulesResult = ctx.element.list_snap_mirror_schedules(snap_mirror_endpoint_id=snapmirrorendpointid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorSchedulesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorSchedulesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('quiescerelationship', short_help="""The SolidFire Element OS web UI uses the QuiesceSnapMirrorRelationship method to disable future data transfers for a SnapMirror relationship. If a transfer is in progress, the relationship status becomes "quiescing" until the transfer is complete. If the current transfer is aborted, it will not restart. You can reenable data transfers for the relationship using the ResumeSnapMirrorRelationship API method. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)

@click.option('--type',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@pass_context
def quiescerelationship(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           type,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserver,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name):
    """The SolidFire Element OS web UI uses the QuiesceSnapMirrorRelationship method to disable future data transfers for a SnapMirror relationship. If a transfer is in progress, the relationship status becomes "quiescing" until the transfer is complete. If the current transfer is aborted, it will not restart. You can reenable data transfers for the relationship using the ResumeSnapMirrorRelationship API method."""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(type is not None or
       volumeid is not None or
       vserver is not None or
       name is not None or
       False):
        if not (type and volumeid and vserver and name and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
type
volumeid
vserver
name
""")
        kwargsDict = dict()
        kwargsDict["type"] = type
        kwargsDict["volume_id"] = volumeid
        kwargsDict["vserver"] = vserver
        kwargsDict["name"] = name

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""destinationvolume = """ + str(destinationvolume)+""";"""+"")
    try:
        _QuiesceSnapMirrorRelationshipResult = ctx.element.quiesce_snap_mirror_relationship(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_QuiesceSnapMirrorRelationshipResult), indent=4))
        return
    else:
        cli_utils.print_result(_QuiesceSnapMirrorRelationshipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listluns', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorLuns method to list the LUN information for the SnapMirror relationship from the remote ONTAP cluster. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""List only the LUN information associated with the specified endpoint ID. """)

@click.option('--type',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@pass_context
def listluns(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           type,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserver,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name):
    """The SolidFire Element OS web UI uses the ListSnapMirrorLuns method to list the LUN information for the SnapMirror relationship from the remote ONTAP cluster."""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(type is not None or
       volumeid is not None or
       vserver is not None or
       name is not None or
       False):
        if not (type and volumeid and vserver and name and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
type
volumeid
vserver
name
""")
        kwargsDict = dict()
        kwargsDict["type"] = type
        kwargsDict["volume_id"] = volumeid
        kwargsDict["vserver"] = vserver
        kwargsDict["name"] = name

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""destinationvolume = """ + str(destinationvolume)+""";"""+"")
    try:
        _ListSnapMirrorLunsResult = ctx.element.list_snap_mirror_luns(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorLunsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorLunsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyrelationship', short_help="""You can use ModifySnapMirrorRelationship to change the intervals at which a scheduled snapshot occurs. You can also delete or pause a schedule by using this method. """, cls=SolidFireCommand)

@click.option('--type',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@click.option('--maxtransferrate',
              type=int,
              required=False,
              help="""Specifies the maximum data transfer rate between the volumes in kilobytes per second. The default value, 0, is unlimited and permits the SnapMirror relationship to fully utilize the available network bandwidth. """)
@click.option('--policyname',
              type=str,
              required=False,
              help="""Specifies the name of the ONTAP SnapMirror policy for the relationship. """)
@click.option('--schedulename',
              type=str,
              required=False,
              help="""The name of the pre-existing cron schedule on the ONTAP system that is used to update the SnapMirror relationship. """)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)
@pass_context
def modifyrelationship(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           type,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserver,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name,
           # Optional main parameter
           maxtransferrate = None,
           # Optional main parameter
           policyname = None,
           # Optional main parameter
           schedulename = None):
    """You can use ModifySnapMirrorRelationship to change the intervals at which a scheduled snapshot occurs. You can also delete or pause a schedule by using this method."""

    

    cli_utils.establish_connection(ctx)
    

    destinationvolume = None
    if(type is not None or
       volumeid is not None or
       vserver is not None or
       name is not None or
       False):
        if not (type and volumeid and vserver and name and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
type
volumeid
vserver
name
""")
        kwargsDict = dict()
        kwargsDict["type"] = type
        kwargsDict["volume_id"] = volumeid
        kwargsDict["vserver"] = vserver
        kwargsDict["name"] = name

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    
    
    
    
    

    ctx.logger.info(""": """"""destinationvolume = """ + str(destinationvolume)+";"+"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";" + """maxtransferrate = """+str(maxtransferrate)+";" + """policyname = """+str(policyname)+";" + """schedulename = """+str(schedulename)+""";"""+"")
    try:
        _ModifySnapMirrorRelationshipResult = ctx.element.modify_snap_mirror_relationship(destination_volume=destinationvolume, snap_mirror_endpoint_id=snapmirrorendpointid, max_transfer_rate=maxtransferrate, policy_name=policyname, schedule_name=schedulename)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifySnapMirrorRelationshipResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifySnapMirrorRelationshipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listendpoints', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorEndpoints method to list all SnapMirror endpoints that the SolidFire cluster is communicating with. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointids',
              type=str,
              required=False,
              help="""Return only the objects associated with these IDs. If no IDs are provided or the array is empty, the method returns all SnapMirror endpoint IDs. """)
@pass_context
def listendpoints(ctx,
           # Optional main parameter
           snapmirrorendpointids = None):
    """The SolidFire Element OS web UI uses the ListSnapMirrorEndpoints method to list all SnapMirror endpoints that the SolidFire cluster is communicating with."""

    

    cli_utils.establish_connection(ctx)
    

    snapmirrorendpointids = parser.parse_array(snapmirrorendpointids)
    

    ctx.logger.info(""": """"""snapmirrorendpointids = """+str(snapmirrorendpointids)+""";"""+"")
    try:
        _ListSnapMirrorEndpointsResult = ctx.element.list_snap_mirror_endpoints(snap_mirror_endpoint_ids=snapmirrorendpointids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorEndpointsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorEndpointsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listpolicies', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorPolicies method to list all SnapMirror policies on a remote ONTAP system. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""List only the policies associated with the specified endpoint ID. If no endpoint ID is provided, the system lists policies from all known SnapMirror endpoints. """)
@pass_context
def listpolicies(ctx,
           # Optional main parameter
           snapmirrorendpointid = None):
    """The SolidFire Element OS web UI uses the ListSnapMirrorPolicies method to list all SnapMirror policies on a remote ONTAP system."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+""";"""+"")
    try:
        _ListSnapMirrorPoliciesResult = ctx.element.list_snap_mirror_policies(snap_mirror_endpoint_id=snapmirrorendpointid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorPoliciesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorPoliciesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createendpoint', short_help="""The SolidFire Element OS web UI uses the CreateSnapMirrorEndpoint method to create a relationship with a remote SnapMirror endpoint. """, cls=SolidFireCommand)
@click.option('--managementip',
              type=str,
              required=True,
              prompt=True,
              help="""The management IP address of the remote SnapMirror endpoint. """)
@click.option('--username',
              type=str,
              required=True,
              prompt=True,
              help="""The management username for the ONTAP system. """)
@click.option('--password',
              type=str,
              required=True,
              prompt=True,
              help="""The management password for the ONTAP system. """)
@pass_context
def createendpoint(ctx,
           # Mandatory main parameter
           managementip,
           # Mandatory main parameter
           username,
           # Mandatory main parameter
           password):
    """The SolidFire Element OS web UI uses the CreateSnapMirrorEndpoint method to create a relationship with a remote SnapMirror endpoint."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    ctx.logger.info(""": """"""managementip = """ + str(managementip)+";"+"""username = """ + str(username)+";"+"""password = """ + str(password)+""";"""+"")
    try:
        _CreateSnapMirrorEndpointResult = ctx.element.create_snap_mirror_endpoint(management_ip=managementip, username=username, password=password)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateSnapMirrorEndpointResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateSnapMirrorEndpointResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getclusteridentity', short_help="""The SolidFire Element OS web UI uses GetSnapMirrorClusterIdentity to get identity information about the ONTAP cluster. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""If provided, the system lists the cluster identity of the endpoint with the specified snapMirrorEndpointID. If not provided, the system lists the cluster identity of all known SnapMirror endpoints. """)
@pass_context
def getclusteridentity(ctx,
           # Optional main parameter
           snapmirrorendpointid = None):
    """The SolidFire Element OS web UI uses GetSnapMirrorClusterIdentity to get identity information about the ONTAP cluster."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+""";"""+"")
    try:
        _GetSnapMirrorClusterIdentityResult = ctx.element.get_snap_mirror_cluster_identity(snap_mirror_endpoint_id=snapmirrorendpointid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetSnapMirrorClusterIdentityResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetSnapMirrorClusterIdentityResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyendpoint', short_help="""The SolidFire Element OS web UI uses the ModifySnapMirrorEndpoint method to change the name and management attributes for a SnapMirror endpoint. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The SnapMirror endpoint to modify. """)
@click.option('--managementip',
              type=str,
              required=False,
              help="""The new management IP Address for the ONTAP system. """)
@click.option('--username',
              type=str,
              required=False,
              help="""The new management username for the ONTAP system. """)
@click.option('--password',
              type=str,
              required=False,
              help="""The new management password for the ONTAP system. """)
@pass_context
def modifyendpoint(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Optional main parameter
           managementip = None,
           # Optional main parameter
           username = None,
           # Optional main parameter
           password = None):
    """The SolidFire Element OS web UI uses the ModifySnapMirrorEndpoint method to change the name and management attributes for a SnapMirror endpoint."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";" + """managementip = """+str(managementip)+";" + """username = """+str(username)+";" + """password = """+str(password)+""";"""+"")
    try:
        _ModifySnapMirrorEndpointResult = ctx.element.modify_snap_mirror_endpoint(snap_mirror_endpoint_id=snapmirrorendpointid, management_ip=managementip, username=username, password=password)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifySnapMirrorEndpointResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifySnapMirrorEndpointResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listnetworkinterfaces', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorNetworkInterfaces method to list all available SnapMirror interfaces on a remote ONTAP system """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""Return only the network interfaces associated with the specified endpoint ID. If no endpoint ID is provided, the system lists interfaces from all known SnapMirror endpoints. """)
@click.option('--interfacerole',
              type=str,
              required=False,
              help="""List only the network interface serving the specified role. """)
@pass_context
def listnetworkinterfaces(ctx,
           # Optional main parameter
           snapmirrorendpointid = None,
           # Optional main parameter
           interfacerole = None):
    """The SolidFire Element OS web UI uses the ListSnapMirrorNetworkInterfaces method to list all available SnapMirror interfaces on a remote ONTAP system"""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+";" + """interfacerole = """+str(interfacerole)+""";"""+"")
    try:
        _ListSnapMirrorNetworkInterfacesResult = ctx.element.list_snap_mirror_network_interfaces(snap_mirror_endpoint_id=snapmirrorendpointid, interface_role=interfacerole)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorNetworkInterfacesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorNetworkInterfacesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listaggregates', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorAggregates method to list all SnapMirror aggregates that are available on the remote ONTAP system. An aggregate describes a set of physical storage resources. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""Return only the aggregates associated with the specified endpoint ID. If no endpoint ID is provided, the system lists aggregates from all known SnapMirror endpoints. """)
@pass_context
def listaggregates(ctx,
           # Optional main parameter
           snapmirrorendpointid = None):
    """The SolidFire Element OS web UI uses the ListSnapMirrorAggregates method to list all SnapMirror aggregates that are available on the remote ONTAP system. An aggregate describes a set of physical storage resources."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+""";"""+"")
    try:
        _ListSnapMirrorAggregatesResult = ctx.element.list_snap_mirror_aggregates(snap_mirror_endpoint_id=snapmirrorendpointid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorAggregatesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorAggregatesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('resyncrelationship', short_help="""The SolidFire Element OS web UI uses the ResyncSnapMirrorRelationship method to establish or reestablish a mirror relationship between a source and destination endpoint. When you resync a relationship, the system removes snapshots on the destination volume that are newer than the common snapshot copy, and then mounts the destination volume as a data protection volume with the common snapshot copy as the exported snapshot copy. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)

@click.option('--typedestinationvolume',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeiddestinationvolume',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserverdestinationvolume',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--namedestinationvolume',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@click.option('--maxtransferrate',
              type=int,
              required=False,
              help="""Specifies the maximum data transfer rate between the volumes in kilobytes per second. The default value, 0, is unlimited and permits the SnapMirror relationship to fully utilize the available network bandwidth. """)

@click.option('--typesourcevolume',
              type=str,
              required=False,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeidsourcevolume',
              type=int,
              required=False,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserversourcevolume',
              type=str,
              required=False,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--namesourcevolume',
              type=str,
              required=False,
              help="""The name of the volume. """)
@pass_context
def resyncrelationship(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           typedestinationvolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeiddestinationvolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserverdestinationvolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           namedestinationvolume,
           # Optional main parameter
           maxtransferrate = None,
           # Optional subparameter of optional main parameter.
           typesourcevolume = None,
           # Optional subparameter of optional main parameter.
           volumeidsourcevolume = None,
           # Optional subparameter of optional main parameter.
           vserversourcevolume = None,
           # Optional subparameter of optional main parameter.
           namesourcevolume = None):
    """The SolidFire Element OS web UI uses the ResyncSnapMirrorRelationship method to establish or reestablish a mirror relationship between a source and destination endpoint. When you resync a relationship, the system removes snapshots on the destination volume that are newer than the common snapshot copy, and then mounts the destination volume as a data protection volume with the common snapshot copy as the exported snapshot copy."""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(typedestinationvolume is not None or
       volumeiddestinationvolume is not None or
       vserverdestinationvolume is not None or
       namedestinationvolume is not None or
       False):
        if not (typedestinationvolume and volumeiddestinationvolume and vserverdestinationvolume and namedestinationvolume and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
typedestinationvolume
volumeiddestinationvolume
vserverdestinationvolume
namedestinationvolume
""")
        kwargsDict = dict()
        kwargsDict["type"] = typedestinationvolume
        kwargsDict["volume_id"] = volumeiddestinationvolume
        kwargsDict["vserver"] = vserverdestinationvolume
        kwargsDict["name"] = namedestinationvolume

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    
    

    sourcevolume = None
    if(typesourcevolume is not None or
       volumeidsourcevolume is not None or
       vserversourcevolume is not None or
       namesourcevolume is not None or
       False):
        if not (typesourcevolume and volumeidsourcevolume and vserversourcevolume and namesourcevolume and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
typesourcevolume
volumeidsourcevolume
vserversourcevolume
namesourcevolume
""")
        kwargsDict = dict()
        kwargsDict["type"] = typesourcevolume
        kwargsDict["volume_id"] = volumeidsourcevolume
        kwargsDict["vserver"] = vserversourcevolume
        kwargsDict["name"] = namesourcevolume

        sourcevolume = SnapMirrorVolumeInfo(**kwargsDict)
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""destinationvolume = """ + str(destinationvolume)+";" + """maxtransferrate = """+str(maxtransferrate)+";" + """sourcevolume = """+str(sourcevolume)+""";"""+"")
    try:
        _ResyncSnapMirrorRelationshipResult = ctx.element.resync_snap_mirror_relationship(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume, max_transfer_rate=maxtransferrate, source_volume=sourcevolume)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ResyncSnapMirrorRelationshipResult), indent=4))
        return
    else:
        cli_utils.print_result(_ResyncSnapMirrorRelationshipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listvservers', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorVservers method to list all SnapMirror Vservers available on a remote ONTAP system. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""List only the Vservers associated with the specified endpoint ID. If no endpoint ID is provided, the system lists Vservers from all known SnapMirror endpoints. """)
@click.option('--vservertype',
              type=str,
              required=False,
              help="""List only Vservers of the specified type. Possible values: admin data node system """)
@click.option('--vservername',
              type=str,
              required=False,
              help="""List only Vservers with the specified name. """)
@pass_context
def listvservers(ctx,
           # Optional main parameter
           snapmirrorendpointid = None,
           # Optional main parameter
           vservertype = None,
           # Optional main parameter
           vservername = None):
    """The SolidFire Element OS web UI uses the ListSnapMirrorVservers method to list all SnapMirror Vservers available on a remote ONTAP system."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+";" + """vservertype = """+str(vservertype)+";" + """vservername = """+str(vservername)+""";"""+"")
    try:
        _ListSnapMirrorVserversResult = ctx.element.list_snap_mirror_vservers(snap_mirror_endpoint_id=snapmirrorendpointid, vserver_type=vservertype, vserver_name=vservername)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorVserversResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorVserversResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyendpointunmanaged', short_help="""The SolidFire Element OS web UI uses the ModifySnapMirrorEndpoint method to change the name and management attributes for a SnapMirror endpoint. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The SnapMirror endpoint to modify. """)
@click.option('--clustername',
              type=str,
              required=False,
              help="""The new name of the endpoint. """)
@click.option('--ipaddresses',
              type=str,
              required=False,
              help="""The new list of IP addresses for a cluster of ONTAP storage systems that should communicate with this SolidFire cluster. """)
@pass_context
def modifyendpointunmanaged(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Optional main parameter
           clustername = None,
           # Optional main parameter
           ipaddresses = None):
    """The SolidFire Element OS web UI uses the ModifySnapMirrorEndpoint method to change the name and management attributes for a SnapMirror endpoint."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ipaddresses = parser.parse_array(ipaddresses)
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";" + """clustername = """+str(clustername)+";" + """ipaddresses = """+str(ipaddresses)+""";"""+"")
    try:
        _ModifySnapMirrorEndpointUnmanagedResult = ctx.element.modify_snap_mirror_endpoint_unmanaged(snap_mirror_endpoint_id=snapmirrorendpointid, cluster_name=clustername, ip_addresses=ipaddresses)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifySnapMirrorEndpointUnmanagedResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifySnapMirrorEndpointUnmanagedResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('deleterelationships', short_help="""The SolidFire Element OS web UI uses the DeleteSnapMirrorRelationships method to remove a SnapMirror relationship between a source and destination endpoint. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)

@click.option('--type',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@pass_context
def deleterelationships(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           type,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserver,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name):
    """The SolidFire Element OS web UI uses the DeleteSnapMirrorRelationships method to remove a SnapMirror relationship between a source and destination endpoint."""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(type is not None or
       volumeid is not None or
       vserver is not None or
       name is not None or
       False):
        if not (type and volumeid and vserver and name and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
type
volumeid
vserver
name
""")
        kwargsDict = dict()
        kwargsDict["type"] = type
        kwargsDict["volume_id"] = volumeid
        kwargsDict["vserver"] = vserver
        kwargsDict["name"] = name

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""destinationvolume = """ + str(destinationvolume)+""";"""+"")
    try:
        _DeleteSnapMirrorRelationshipsResult = ctx.element.delete_snap_mirror_relationships(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteSnapMirrorRelationshipsResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteSnapMirrorRelationshipsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listnodes', short_help="""The SolidFire Element OS web UI uses the ListSnapMirrorNodes method to get a list of nodes in a remote ONTAP cluster. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""If provided, the system lists the nodes of the endpoint with the specified snapMirrorEndpointID. If not provided, the system lists the nodes of all known SnapMirror endpoints. """)
@pass_context
def listnodes(ctx,
           # Optional main parameter
           snapmirrorendpointid = None):
    """The SolidFire Element OS web UI uses the ListSnapMirrorNodes method to get a list of nodes in a remote ONTAP cluster."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+""";"""+"")
    try:
        _ListSnapMirrorNodesResult = ctx.element.list_snap_mirror_nodes(snap_mirror_endpoint_id=snapmirrorendpointid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListSnapMirrorNodesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListSnapMirrorNodesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('breakvolume', short_help="""The SolidFire Element OS web UI uses the BreakSnapMirrorVolume method to break the SnapMirror relationship between an ONTAP source container and SolidFire target volume. Breaking a SolidFire SnapMirror volume is useful if an ONTAP system becomes unavailable while replicating data to a SolidFire volume. This feature enables a storage administrator to take control of a SolidFire SnapMirror volume, break its relationship with the remote ONTAP system, and revert the volume to a previous snapshot. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The volume on which to perform the break operation. The volume access mode must be snapMirrorTarget. """)
@click.option('--snapshotid',
              type=int,
              required=False,
              help="""Roll back the volume to the snapshot identified by this ID. The default behavior is to roll back to the most recent snapshot. """)
@click.option('--preserve',
              type=bool,
              required=False,
              help="""Preserve any snapshots newer than the snapshot identified by snapshotID. Possible values: true: Preserve snapshots newer than snapshotID. false: Do not preserve snapshots newer than snapshotID. If false, any snapshots newer than snapshotID are deleted. """)
@click.option('--access',
              type=str,
              required=False,
              help="""Resulting volume access mode. Possible values: readWrite readOnly locked """)
@pass_context
def breakvolume(ctx,
           # Mandatory main parameter
           volumeid,
           # Optional main parameter
           snapshotid = None,
           # Optional main parameter
           preserve = None,
           # Optional main parameter
           access = None):
    """The SolidFire Element OS web UI uses the BreakSnapMirrorVolume method to break the SnapMirror relationship between an ONTAP source container and SolidFire target volume. Breaking a SolidFire SnapMirror volume is useful if an ONTAP system becomes unavailable while replicating data to a SolidFire volume. This feature enables a storage administrator to take control of a SolidFire SnapMirror volume, break its relationship with the remote ONTAP system, and revert the volume to a previous snapshot."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    

    ctx.logger.info(""": """"""volumeid = """ + str(volumeid)+";" + """snapshotid = """+str(snapshotid)+";" + """preserve = """+str(preserve)+";" + """access = """+str(access)+""";"""+"")
    try:
        _BreakSnapMirrorVolumeResult = ctx.element.break_snap_mirror_volume(volume_id=volumeid, snapshot_id=snapshotid, preserve=preserve, access=access)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_BreakSnapMirrorVolumeResult), indent=4))
        return
    else:
        cli_utils.print_result(_BreakSnapMirrorVolumeResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getontapversioninfo', short_help="""The SolidFire Element OS web UI uses GetOntapVersionInfo to get information about API version support from the ONTAP cluster in a SnapMirror relationship. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=False,
              help="""If provided, the system lists the version information from the endpoint with the specified snapMirrorEndpointID. If not provided, the system lists the version information of all known SnapMirror endpoints. """)
@pass_context
def getontapversioninfo(ctx,
           # Optional main parameter
           snapmirrorendpointid = None):
    """The SolidFire Element OS web UI uses GetOntapVersionInfo to get information about API version support from the ONTAP cluster in a SnapMirror relationship."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """+str(snapmirrorendpointid)+""";"""+"")
    try:
        _GetOntapVersionInfoResult = ctx.element.get_ontap_version_info(snap_mirror_endpoint_id=snapmirrorendpointid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetOntapVersionInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetOntapVersionInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createendpointunmanaged', short_help="""The SolidFire system uses the CreateSnapMirrorEndpointUnmanaged method to enable remote, unmanaged SnapMirror endpoints to communicate with a SolidFire cluster. Unmanaged endpoints cannot be administered using the SolidFire SnapMirror APIs. They must be managed with ONTAP management software or APIs. """, cls=SolidFireCommand)
@click.option('--clustername',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the endpoint. """)
@click.option('--ipaddresses',
              type=str,
              required=True,
              prompt=True,
              help="""The list of IP addresses for a cluster of ONTAP storage systems that should communicate with this SolidFire cluster. """)
@pass_context
def createendpointunmanaged(ctx,
           # Mandatory main parameter
           clustername,
           # Mandatory main parameter
           ipaddresses):
    """The SolidFire system uses the CreateSnapMirrorEndpointUnmanaged method to enable remote, unmanaged SnapMirror endpoints to communicate with a SolidFire cluster."""
    """Unmanaged endpoints cannot be administered using the SolidFire SnapMirror APIs. They must be managed with ONTAP management software or APIs."""

    

    cli_utils.establish_connection(ctx)
    
    

    ipaddresses = parser.parse_array(ipaddresses)
    

    ctx.logger.info(""": """"""clustername = """ + str(clustername)+";"+"""ipaddresses = """ + str(ipaddresses)+""";"""+"")
    try:
        _CreateSnapMirrorEndpointUnmanagedResult = ctx.element.create_snap_mirror_endpoint_unmanaged(cluster_name=clustername, ip_addresses=ipaddresses)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateSnapMirrorEndpointUnmanagedResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateSnapMirrorEndpointUnmanagedResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('breakrelationship', short_help="""The SolidFire Element OS web UI uses the BreakSnapMirrorRelationship method to break a SnapMirror relationship. When a SnapMirror relationship is broken, the destination volume is made read-write and independent, and can then diverge from the source. You can reestablish the relationship with the ResyncSnapMirrorRelationship API method. This method requires the ONTAP cluster to be available. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)

@click.option('--type',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@pass_context
def breakrelationship(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           type,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserver,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name):
    """The SolidFire Element OS web UI uses the BreakSnapMirrorRelationship method to break a SnapMirror relationship. When a SnapMirror relationship is broken, the destination volume is made read-write and independent, and can then diverge from the source. You can reestablish the relationship with the ResyncSnapMirrorRelationship API method. This method requires the ONTAP cluster to be available."""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(type is not None or
       volumeid is not None or
       vserver is not None or
       name is not None or
       False):
        if not (type and volumeid and vserver and name and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
type
volumeid
vserver
name
""")
        kwargsDict = dict()
        kwargsDict["type"] = type
        kwargsDict["volume_id"] = volumeid
        kwargsDict["vserver"] = vserver
        kwargsDict["name"] = name

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""destinationvolume = """ + str(destinationvolume)+""";"""+"")
    try:
        _BreakSnapMirrorRelationshipResult = ctx.element.break_snap_mirror_relationship(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_BreakSnapMirrorRelationshipResult), indent=4))
        return
    else:
        cli_utils.print_result(_BreakSnapMirrorRelationshipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('updaterelationship', short_help="""The SolidFire Element OS web UI uses the UpdateSnapMirrorRelationship method to make the destination volume in a SnapMirror relationship an up-to-date mirror of the source volume. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)

@click.option('--type',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserver',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@click.option('--maxtransferrate',
              type=int,
              required=False,
              help="""Specifies the maximum data transfer rate between the volumes in kilobytes per second. The default value, 0, is unlimited and permits the SnapMirror relationship to fully utilize the available network bandwidth. """)
@pass_context
def updaterelationship(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           type,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserver,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name,
           # Optional main parameter
           maxtransferrate = None):
    """The SolidFire Element OS web UI uses the UpdateSnapMirrorRelationship method to make the destination volume in a SnapMirror relationship an up-to-date mirror of the source volume."""

    

    cli_utils.establish_connection(ctx)
    
    

    destinationvolume = None
    if(type is not None or
       volumeid is not None or
       vserver is not None or
       name is not None or
       False):
        if not (type and volumeid and vserver and name and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
type
volumeid
vserver
name
""")
        kwargsDict = dict()
        kwargsDict["type"] = type
        kwargsDict["volume_id"] = volumeid
        kwargsDict["vserver"] = vserver
        kwargsDict["name"] = name

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""destinationvolume = """ + str(destinationvolume)+";" + """maxtransferrate = """+str(maxtransferrate)+""";"""+"")
    try:
        _UpdateSnapMirrorRelationshipResult = ctx.element.update_snap_mirror_relationship(snap_mirror_endpoint_id=snapmirrorendpointid, destination_volume=destinationvolume, max_transfer_rate=maxtransferrate)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_UpdateSnapMirrorRelationshipResult), indent=4))
        return
    else:
        cli_utils.print_result(_UpdateSnapMirrorRelationshipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createrelationship', short_help="""The SolidFire Element OS web UI uses the CreateSnapMirrorRelationship method to create a SnapMirror extended data protection relationship between a source and destination endpoint. """, cls=SolidFireCommand)
@click.option('--snapmirrorendpointid',
              type=int,
              required=True,
              prompt=True,
              help="""The endpoint ID of the remote ONTAP storage system communicating with the SolidFire cluster. """)

@click.option('--typesourcevolume',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeidsourcevolume',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserversourcevolume',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--namesourcevolume',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)

@click.option('--typedestinationvolume',
              type=str,
              required=True,
              prompt=True,
              help="""The type of volume. Possible values: solidfire: The volume resides on a SolidFire cluster. ontap:     The volume resides on a remote ONTAP cluster. """)

@click.option('--volumeiddestinationvolume',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume. Only valid if "type" is solidfire. """)

@click.option('--vserverdestinationvolume',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the Vserver that owns this volume. Only valid if "type" is ONTAP. """)

@click.option('--namedestinationvolume',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the volume. """)
@click.option('--relationshiptype',
              type=str,
              required=False,
              help="""The type of relationship. On SolidFire systems, this value is always "extended_data_protection". """)
@click.option('--policyname',
              type=str,
              required=False,
              help="""Specifies the name of the ONTAP SnapMirror policy for the relationship. If not specified, the default policy name is MirrorLatest. """)
@click.option('--schedulename',
              type=str,
              required=False,
              help="""The name of the preexisting cron schedule on the ONTAP system that is used to update the SnapMirror relationship. If no schedule is designated, snapMirror updates are not scheduled and must be updated manually. """)
@click.option('--maxtransferrate',
              type=int,
              required=False,
              help="""Specifies the maximum data transfer rate between the volumes in kilobytes per second. The default value, 0, is unlimited and permits the SnapMirror relationship to fully utilize the available network bandwidth. """)
@pass_context
def createrelationship(ctx,
           # Mandatory main parameter
           snapmirrorendpointid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           typesourcevolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeidsourcevolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserversourcevolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           namesourcevolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           typedestinationvolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeiddestinationvolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           vserverdestinationvolume,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           namedestinationvolume,
           # Optional main parameter
           relationshiptype = None,
           # Optional main parameter
           policyname = None,
           # Optional main parameter
           schedulename = None,
           # Optional main parameter
           maxtransferrate = None):
    """The SolidFire Element OS web UI uses the CreateSnapMirrorRelationship method to create a SnapMirror extended data protection relationship between a source and destination endpoint."""

    

    cli_utils.establish_connection(ctx)
    
    

    sourcevolume = None
    if(typesourcevolume is not None or
       volumeidsourcevolume is not None or
       vserversourcevolume is not None or
       namesourcevolume is not None or
       False):
        if not (typesourcevolume and volumeidsourcevolume and vserversourcevolume and namesourcevolume and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
typesourcevolume
volumeidsourcevolume
vserversourcevolume
namesourcevolume
""")
        kwargsDict = dict()
        kwargsDict["type"] = typesourcevolume
        kwargsDict["volume_id"] = volumeidsourcevolume
        kwargsDict["vserver"] = vserversourcevolume
        kwargsDict["name"] = namesourcevolume

        sourcevolume = SnapMirrorVolumeInfo(**kwargsDict)
    

    destinationvolume = None
    if(typedestinationvolume is not None or
       volumeiddestinationvolume is not None or
       vserverdestinationvolume is not None or
       namedestinationvolume is not None or
       False):
        if not (typedestinationvolume and volumeiddestinationvolume and vserverdestinationvolume and namedestinationvolume and  True):
            ctx.logger.error("""If you choose to provide , you must include all of the following parameters:
typedestinationvolume
volumeiddestinationvolume
vserverdestinationvolume
namedestinationvolume
""")
        kwargsDict = dict()
        kwargsDict["type"] = typedestinationvolume
        kwargsDict["volume_id"] = volumeiddestinationvolume
        kwargsDict["vserver"] = vserverdestinationvolume
        kwargsDict["name"] = namedestinationvolume

        destinationvolume = SnapMirrorVolumeInfo(**kwargsDict)
    
    
    
    
    

    ctx.logger.info(""": """"""snapmirrorendpointid = """ + str(snapmirrorendpointid)+";"+"""sourcevolume = """ + str(sourcevolume)+";"+"""destinationvolume = """ + str(destinationvolume)+";" + """relationshiptype = """+str(relationshiptype)+";" + """policyname = """+str(policyname)+";" + """schedulename = """+str(schedulename)+";" + """maxtransferrate = """+str(maxtransferrate)+""";"""+"")
    try:
        _CreateSnapMirrorRelationshipResult = ctx.element.create_snap_mirror_relationship(snap_mirror_endpoint_id=snapmirrorendpointid, source_volume=sourcevolume, destination_volume=destinationvolume, relationship_type=relationshiptype, policy_name=policyname, schedule_name=schedulename, max_transfer_rate=maxtransferrate)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateSnapMirrorRelationshipResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateSnapMirrorRelationshipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

