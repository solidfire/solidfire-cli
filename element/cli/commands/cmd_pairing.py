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
    """completecluster completevolume listclusterpairs removevolumepair startvolume listactivepairedvolumes modifyvolumepair startcluster removeclusterpair """

@cli.command('completecluster', short_help="""You can use the CompleteClusterPairing method with the encoded key received from the  StartClusterPairing method to complete the cluster pairing process. The CompleteClusterPairing method is the second step in the cluster pairing process.  """, cls=SolidFireCommand)
@click.option('--clusterpairingkey',
              type=str,
              required=True,
              prompt=True,
              help="""A string of characters that is returned from the "StartClusterPairing" API method. """)
@pass_context
def completecluster(ctx,
           # Mandatory main parameter
           clusterpairingkey):
    """You can use the CompleteClusterPairing method with the encoded key received from the  StartClusterPairing method to complete the cluster pairing process. The CompleteClusterPairing method is the second step in the cluster pairing process. """

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""clusterpairingkey = """ + str(clusterpairingkey)+""";"""+"")
    try:
        _CompleteClusterPairingResult = ctx.element.complete_cluster_pairing(cluster_pairing_key=clusterpairingkey)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CompleteClusterPairingResult), indent=4))
        return
    else:
        cli_utils.print_result(_CompleteClusterPairingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('completevolume', short_help="""You can use the CompleteVolumePairing method to complete the pairing of two volumes. """, cls=SolidFireCommand)
@click.option('--volumepairingkey',
              type=str,
              required=True,
              prompt=True,
              help="""The key returned from the StartVolumePairing method. """)
@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume on which to complete the pairing process. """)
@pass_context
def completevolume(ctx,
           # Mandatory main parameter
           volumepairingkey,
           # Mandatory main parameter
           volumeid):
    """You can use the CompleteVolumePairing method to complete the pairing of two volumes."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""volumepairingkey = """ + str(volumepairingkey)+";"+"""volumeid = """ + str(volumeid)+""";"""+"")
    try:
        _CompleteVolumePairingResult = ctx.element.complete_volume_pairing(volume_pairing_key=volumepairingkey, volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CompleteVolumePairingResult), indent=4))
        return
    else:
        cli_utils.print_result(_CompleteVolumePairingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listclusterpairs', short_help="""You can use the ListClusterPairs method to list all the clusters that a cluster is paired with. This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing. """, cls=SolidFireCommand)
@pass_context
def listclusterpairs(ctx):
    """You can use the ListClusterPairs method to list all the clusters that a cluster is paired with. This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListClusterPairsResult = ctx.element.list_cluster_pairs()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListClusterPairsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListClusterPairsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('removevolumepair', short_help="""RemoveVolumePair enables you to remove the remote pairing between two volumes. Use this method on both the source and target volumes that are paired together. When you remove the volume pairing information, data is no longer replicated to or from the volume. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume on which to stop the replication process. """)
@pass_context
def removevolumepair(ctx,
           # Mandatory main parameter
           volumeid):
    """RemoveVolumePair enables you to remove the remote pairing between two volumes. Use this method on both the source and target volumes that are paired together. When you remove the volume pairing information, data is no longer replicated to or from the volume."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""volumeid = """ + str(volumeid)+""";"""+"")
    try:
        _RemoveVolumePairResult = ctx.element.remove_volume_pair(volume_id=volumeid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveVolumePairResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveVolumePairResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('startvolume', short_help="""StartVolumePairing enables you to create an encoded key from a volume that is used to pair with another volume. The key that this method creates is used in the CompleteVolumePairing API method to establish a volume pairing. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume on which to start the pairing process. """)
@click.option('--mode',
              type=str,
              required=False,
              help="""The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume. Possible values are: Async: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: Source acknowledges write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated. """)
@pass_context
def startvolume(ctx,
           # Mandatory main parameter
           volumeid,
           # Optional main parameter
           mode = None):
    """StartVolumePairing enables you to create an encoded key from a volume that is used to pair with another volume. The key that this"""
    """method creates is used in the CompleteVolumePairing API method to establish a volume pairing."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""volumeid = """ + str(volumeid)+";" + """mode = """+str(mode)+""";"""+"")
    try:
        _StartVolumePairingResult = ctx.element.start_volume_pairing(volume_id=volumeid, mode=mode)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_StartVolumePairingResult), indent=4))
        return
    else:
        cli_utils.print_result(_StartVolumePairingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listactivepairedvolumes', short_help="""ListActivePairedVolumes enables you to list all the active volumes paired with a volume. This method returns information about volumes with active and pending pairings. """, cls=SolidFireCommand)
@click.option('--startvolumeid',
              type=int,
              required=False,
              help="""The beginning of the range of active paired volumes to return. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""Maximum number of active paired volumes to return. """)
@pass_context
def listactivepairedvolumes(ctx,
           # Optional main parameter
           startvolumeid = None,
           # Optional main parameter
           limit = None):
    """ListActivePairedVolumes enables you to list all the active volumes paired with a volume. This method returns information about volumes with active and pending pairings."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""startvolumeid = """+str(startvolumeid)+";" + """limit = """+str(limit)+""";"""+"")
    try:
        _ListActivePairedVolumesResult = ctx.element.list_active_paired_volumes(start_volume_id=startvolumeid, limit=limit)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListActivePairedVolumesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListActivePairedVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifyvolumepair', short_help="""ModifyVolumePair enables you to pause or restart replication between a pair of volumes. """, cls=SolidFireCommand)
@click.option('--volumeid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume to be modified. """)
@click.option('--pausedmanual',
              type=bool,
              required=False,
              help="""Specifies whether to pause or restart volume replication process. Valid values are:  true: Pauses volume replication false: Restarts volume replication """)
@click.option('--mode',
              type=str,
              required=False,
              help="""Specifies the volume replication mode. Possible values are: Async: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster. Sync: The source acknowledges the write when the data is stored locally and on the remote cluster. SnapshotsOnly: Only snapshots created on the source cluster are replicated. Active writes from the source volume are not replicated. """)
@click.option('--pauselimit',
              type=int,
              required=False,
              help="""Internal use only. """)
@pass_context
def modifyvolumepair(ctx,
           # Mandatory main parameter
           volumeid,
           # Optional main parameter
           pausedmanual = None,
           # Optional main parameter
           mode = None,
           # Optional main parameter
           pauselimit = None):
    """ModifyVolumePair enables you to pause or restart replication between a pair of volumes."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    

    ctx.logger.info(""": """"""volumeid = """ + str(volumeid)+";" + """pausedmanual = """+str(pausedmanual)+";" + """mode = """+str(mode)+";" + """pauselimit = """+str(pauselimit)+""";"""+"")
    try:
        _ModifyVolumePairResult = ctx.element.modify_volume_pair(volume_id=volumeid, paused_manual=pausedmanual, mode=mode, pause_limit=pauselimit)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyVolumePairResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyVolumePairResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('startcluster', short_help="""You can use the StartClusterPairing method to create an encoded key from a cluster that is used to pair with another cluster. The key created from this API method is used in the CompleteClusterPairing API method to establish a cluster pairing. You can pair a cluster with a maximum of four other clusters.  """, cls=SolidFireCommand)
@pass_context
def startcluster(ctx):
    """You can use the StartClusterPairing method to create an encoded key from a cluster that is used to pair with another cluster. The key created from this API method is used in the CompleteClusterPairing API method to establish a cluster pairing. You can pair a cluster with a maximum of four other clusters. """

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _StartClusterPairingResult = ctx.element.start_cluster_pairing()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_StartClusterPairingResult), indent=4))
        return
    else:
        cli_utils.print_result(_StartClusterPairingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('removeclusterpair', short_help="""You can use the RemoveClusterPair method to close the open connections between two paired clusters. Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method. """, cls=SolidFireCommand)
@click.option('--clusterpairid',
              type=int,
              required=True,
              prompt=True,
              help="""Unique identifier used to pair two clusters. """)
@pass_context
def removeclusterpair(ctx,
           # Mandatory main parameter
           clusterpairid):
    """You can use the RemoveClusterPair method to close the open connections between two paired clusters."""
    """Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""clusterpairid = """ + str(clusterpairid)+""";"""+"")
    try:
        _RemoveClusterPairResult = ctx.element.remove_cluster_pair(cluster_pair_id=clusterpairid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveClusterPairResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveClusterPairResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

