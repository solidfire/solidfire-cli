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
from uuid import UUID
from element import exceptions
from solidfire import common


@click.group()
@pass_context
def cli(ctx):
    """CompleteCluster CompleteVolume ListClusterPairs RemoveVolumePair StartVolume ListActivePairedVolumes ModifyVolumePair StartCluster RemoveClusterPair """

@cli.command('CompleteCluster', short_help="""The CompleteClusterPairing method is the second step in the cluster pairing process. Use this method with the encoded key received from the "StartClusterPairing" API method to complete the cluster pairing process. """)
@click.option('--cluster_pairing_key',
              type=str,
              required=True,
              help="""A string of characters that is returned from the "StartClusterPairing" API method. """)
@pass_context
def CompleteCluster(ctx,
           cluster_pairing_key):
    """The CompleteClusterPairing method is the second step in the cluster pairing process."""
    """Use this method with the encoded key received from the &quot;StartClusterPairing&quot; API method to complete the cluster pairing process."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""cluster_pairing_key = """+str(cluster_pairing_key)+""";"""+"")
    try:
        CompleteClusterPairingResult = ctx.element.complete_cluster_pairing(cluster_pairing_key=cluster_pairing_key)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CompleteClusterPairingResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CompleteVolume', short_help="""CompleteVolumePairing is used to complete the pairing of two volumes. """)
@click.option('--volume_pairing_key',
              type=str,
              required=True,
              help="""The key returned from the "StartVolumePairing" API method. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""The ID of volume on which to complete the pairing process. """)
@pass_context
def CompleteVolume(ctx,
           volume_pairing_key,
           volume_id):
    """CompleteVolumePairing is used to complete the pairing of two volumes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_pairing_key = """+str(volume_pairing_key)+""";"""+"""volume_id = """+str(volume_id)+""";"""+"")
    try:
        CompleteVolumePairingResult = ctx.element.complete_volume_pairing(volume_pairing_key=volume_pairing_key, volume_id=volume_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CompleteVolumePairingResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListClusterPairs', short_help="""ListClusterPairs is used to list all of the clusters a cluster is paired with. This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing. """)
@pass_context
def ListClusterPairs(ctx):
    """ListClusterPairs is used to list all of the clusters a cluster is paired with."""
    """This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        ListClusterPairsResult = ctx.element.list_cluster_pairs()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListClusterPairsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveVolumePair', short_help="""RemoveVolumePair is used to remove the remote pairing between two volumes. When the volume pairing information is removed, data is no longer replicated to or from the volume. This method should be run on both the source and target volumes that are paired together. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""ID of the volume on which to stop the replication process. """)
@pass_context
def RemoveVolumePair(ctx,
           volume_id):
    """RemoveVolumePair is used to remove the remote pairing between two volumes."""
    """When the volume pairing information is removed, data is no longer replicated to or from the volume."""
    """This method should be run on both the source and target volumes that are paired together."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"")
    try:
        RemoveVolumePairResult = ctx.element.remove_volume_pair(volume_id=volume_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(RemoveVolumePairResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('StartVolume', short_help="""StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume. The key that this method creates is used in the "CompleteVolumePairing" API method to establish a volume pairing. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""The ID of the volume on which to start the pairing process. """)
@click.option('--mode',
              type=str,
              required=False,
              help="""The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.<br/> Possible values:<br/> <b>Async</b>: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.<br/> <b>Sync</b>: Source acknowledges write when the data is stored locally and on the remote cluster.<br/> <b>SnapshotsOnly</b>: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.<br/> """)
@pass_context
def StartVolume(ctx,
           volume_id,
           mode = None):
    """StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume."""
    """The key that this method creates is used in the &quot;CompleteVolumePairing&quot; API method to establish a volume pairing."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"""mode = """+str(mode)+""";"""+"")
    try:
        StartVolumePairingResult = ctx.element.start_volume_pairing(volume_id=volume_id, mode=mode)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(StartVolumePairingResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListActivePairedVolumes', short_help="""ListActivePairedVolumes is used to list all of the active volumes paired with a volume. Volumes listed in the return for this method include volumes with active and pending pairings. """)
@pass_context
def ListActivePairedVolumes(ctx):
    """ListActivePairedVolumes is used to list all of the active volumes paired with a volume."""
    """Volumes listed in the return for this method include volumes with active and pending pairings."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        ListActivePairedVolumesResult = ctx.element.list_active_paired_volumes()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListActivePairedVolumesResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ModifyVolumePair', short_help="""ModifyVolumePair is used to pause or restart replication between a pair of volumes. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""Identification number of the volume to be modified. """)
@click.option('--paused_manual',
              type=bool,
              required=False,
              help="""Valid values that can be entered:<br/> <b>true</b>: to pause volume replication.<br/> <b>false</b>: to restart volume replication.<br/> If no value is specified, no change in replication is performed. """)
@click.option('--mode',
              type=str,
              required=False,
              help="""Volume replication mode.<br/> Possible values:<br/> <b>Async</b>: Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.<br/> <b>Sync</b>: The source acknowledges the write when the data is stored locally and on the remote cluster.<br/> <b>SnapshotsOnly</b>: Only snapshots created on the source cluster will be replicated. Active writes from the source volume are not replicated.<br/> """)
@pass_context
def ModifyVolumePair(ctx,
           volume_id,
           paused_manual = None,
           mode = None):
    """ModifyVolumePair is used to pause or restart replication between a pair of volumes."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_id = """+str(volume_id)+""";"""+"""paused_manual = """+str(paused_manual)+""";"""+"""mode = """+str(mode)+""";"""+"")
    try:
        ModifyVolumePairResult = ctx.element.modify_volume_pair(volume_id=volume_id, paused_manual=paused_manual, mode=mode)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ModifyVolumePairResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('StartCluster', short_help="""StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster. The key created from this API method is used in the "CompleteClusterPairing" API method to establish a cluster pairing. You can pair a cluster with a maximum of four other SolidFire clusters. """)
@pass_context
def StartCluster(ctx):
    """StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster."""
    """The key created from this API method is used in the &quot;CompleteClusterPairing&quot; API method to establish a cluster pairing."""
    """You can pair a cluster with a maximum of four other SolidFire clusters."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        StartClusterPairingResult = ctx.element.start_cluster_pairing()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(StartClusterPairingResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveClusterPair', short_help="""You can use the RemoveClusterPair method to close the open connections between two paired clusters. Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the "RemoveVolumePair" API method. """)
@click.option('--cluster_pair_id',
              type=int,
              required=True,
              help="""Unique identifier used to pair two clusters. """)
@pass_context
def RemoveClusterPair(ctx,
           cluster_pair_id):
    """You can use the RemoveClusterPair method to close the open connections between two paired clusters."""
    """Note: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the &quot;RemoveVolumePair&quot; API method."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""cluster_pair_id = """+str(cluster_pair_id)+""";"""+"")
    try:
        RemoveClusterPairResult = ctx.element.remove_cluster_pair(cluster_pair_id=cluster_pair_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(RemoveClusterPairResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

