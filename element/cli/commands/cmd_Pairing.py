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
from uuid import UUID


@click.group()
@pass_context
def cli(ctx):
    """CompleteClusterPairing CompleteVolumePairing ListActivePairedVolumes ListClusterPairs ModifyVolumePair RemoveClusterPair RemoveVolumePair StartClusterPairing StartVolumePairing """
    ctx.sfapi = ctx.client

@cli.command('CompleteClusterPairing', short_help="CompleteClusterPairing")
@click.option('--cluster_pairing_key',
              type=str,
              required=True,
              help="""A string of characters that is returned from the "StartClusterPairing" API method. """)
@pass_context
def CompleteClusterPairing(ctx,
           cluster_pairing_key):
    """The CompleteClusterPairing method is the second step in the cluster pairing process."""
    """Use this method with the encoded key received from the &quot;StartClusterPairing&quot; API method to complete the cluster pairing process."""



    CompleteClusterPairingResult = ctx.element.complete_cluster_pairing(cluster_pairing_key=cluster_pairing_key)
    cli_utils.print_result(CompleteClusterPairingResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CompleteVolumePairing', short_help="CompleteVolumePairing")
@click.option('--volume_pairing_key',
              type=str,
              required=True,
              help="""The key returned from the "StartVolumePairing" API method. """)
@click.option('--volume_id',
              type=int,
              required=True,
              help="""The ID of volume on which to complete the pairing process. """)
@pass_context
def CompleteVolumePairing(ctx,
           volume_pairing_key,
           volume_id):
    """CompleteVolumePairing is used to complete the pairing of two volumes."""



    CompleteVolumePairingResult = ctx.element.complete_volume_pairing(volume_pairing_key=volume_pairing_key, volume_id=volume_id)
    cli_utils.print_result(CompleteVolumePairingResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListActivePairedVolumes', short_help="ListActivePairedVolumes")
@pass_context
def ListActivePairedVolumes(ctx):
    """ListActivePairedVolumes is used to list all of the active volumes paired with a volume."""
    """Volumes listed in the return for this method include volumes with active and pending pairings."""



    ListActivePairedVolumesResult = ctx.element.list_active_paired_volumes()
    cli_utils.print_result(ListActivePairedVolumesResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListClusterPairs', short_help="ListClusterPairs")
@pass_context
def ListClusterPairs(ctx):
    """ListClusterPairs is used to list all of the clusters a cluster is paired with."""
    """This method returns information about active and pending cluster pairings, such as statistics about the current pairing as well as the connectivity and latency (in milliseconds) of the cluster pairing."""



    ListClusterPairsResult = ctx.element.list_cluster_pairs()
    cli_utils.print_result(ListClusterPairsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ModifyVolumePair', short_help="ModifyVolumePair")
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



    ModifyVolumePairResult = ctx.element.modify_volume_pair(volume_id=volume_id, paused_manual=paused_manual, mode=mode)
    cli_utils.print_result(ModifyVolumePairResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveClusterPair', short_help="RemoveClusterPair")
@click.option('--cluster_pair_id',
              type=int,
              required=True,
              help="""Unique identifier used to pair two clusters. """)
@pass_context
def RemoveClusterPair(ctx,
           cluster_pair_id):
    """You can use the RemoveClusterPair method to close the open connections between two paired clusters.&lt;br/&gt;"""
    """&lt;b&gt;Note&lt;/b&gt;: Before you remove a cluster pair, you must first remove all volume pairing to the clusters with the &quot;RemoveVolumePair&quot; API method."""



    RemoveClusterPairResult = ctx.element.remove_cluster_pair(cluster_pair_id=cluster_pair_id)
    cli_utils.print_result(RemoveClusterPairResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveVolumePair', short_help="RemoveVolumePair")
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



    RemoveVolumePairResult = ctx.element.remove_volume_pair(volume_id=volume_id)
    cli_utils.print_result(RemoveVolumePairResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('StartClusterPairing', short_help="StartClusterPairing")
@pass_context
def StartClusterPairing(ctx):
    """StartClusterPairing is used to create an encoded key from a cluster that is used to pair with another cluster."""
    """The key created from this API method is used in the &quot;CompleteClusterPairing&quot; API method to establish a cluster pairing."""
    """You can pair a cluster with a maximum of four other SolidFire clusters."""



    StartClusterPairingResult = ctx.element.start_cluster_pairing()
    cli_utils.print_result(StartClusterPairingResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('StartVolumePairing', short_help="StartVolumePairing")
@click.option('--volume_id',
              type=int,
              required=True,
              help="""The ID of the volume on which to start the pairing process. """)
@click.option('--mode',
              type=str,
              required=False,
              help="""The mode of the volume on which to start the pairing process. The mode can only be set if the volume is the source volume.<br/> Possible values:<br/> <b>Async</b>: (default if no mode parameter specified) Writes are acknowledged when they complete locally. The cluster does not wait for writes to be replicated to the target cluster.<br/> <b>Sync</b>: Source acknowledges write when the data is stored locally and on the remote cluster.<br/> <b>SnapshotsOnly</b>: Only snapshots created on the source cluster will be replicated. Active writes from the source volume will not be replicated.<br/> """)
@pass_context
def StartVolumePairing(ctx,
           volume_id,
           mode = None):
    """StartVolumePairing is used to create an encoded key from a volume that is used to pair with another volume."""
    """The key that this method creates is used in the &quot;CompleteVolumePairing&quot; API method to establish a volume pairing."""



    StartVolumePairingResult = ctx.element.start_volume_pairing(volume_id=volume_id, mode=mode)
    cli_utils.print_result(StartVolumePairingResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

