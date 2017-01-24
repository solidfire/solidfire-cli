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
<<<<<<< HEAD
    """ListHosts ListTasks EnableFeature List ListBindings GetCount GetFeatureStatus """

@cli.command('ListHosts', short_help="""ListVirtualVolumeHosts returns a list of known ESX hosts. """)
@click.option('--virtual_volume_host_ids',
=======
    """EnableFeature GetFeatureStatus ListTasks ListBindings List ListHosts GetTaskUpdate PrepareVirtualSnapshot CreateHost GetUnsharedChunks GetCount """

@cli.command('EnableFeature', short_help="""EnableFeature allows you to enable cluster features that are disabled by default. """)
@click.option('--feature',
              type=str,
              required=True,
              help="""Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def EnableFeature(ctx,
           feature):
    """EnableFeature allows you to enable cluster features that are disabled by default."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        EnableFeatureResult = ctx.element.enable_feature(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(EnableFeatureResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetFeatureStatus', short_help="""GetFeatureStatus allows you to retrieve the status of a cluster feature. """)
@click.option('--feature',
              type=str,
              required=False,
              help="""Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def GetFeatureStatus(ctx,
           feature = None):
    """GetFeatureStatus allows you to retrieve the status of a cluster feature."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        GetFeatureStatusResult = ctx.element.get_feature_status(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetFeatureStatusResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListTasks', short_help="""ListVirtualVolumeTasks returns a list of VVol Async Tasks. """)
@click.option('--virtual_volume_task_ids',
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
              type=str,
              required=False,
              help="""""")
@pass_context
<<<<<<< HEAD
def ListHosts(ctx,
           virtual_volume_host_ids = None):
    """ListVirtualVolumeHosts returns a list of known ESX hosts."""
=======
def ListTasks(ctx,
           virtual_volume_task_ids = None):
    """ListVirtualVolumeTasks returns a list of VVol Async Tasks."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
    virtual_volume_host_ids = parser.parse_array(virtual_volume_host_ids)

    ctx.logger.info("""virtual_volume_host_ids = """+str(virtual_volume_host_ids)+""";"""+"")
    try:
        ListVirtualVolumeHostsResult = ctx.element.list_virtual_volume_hosts(virtual_volume_host_ids=virtual_volume_host_ids)
=======
    virtual_volume_task_ids = parser.parse_array(virtual_volume_task_ids)

    ctx.logger.info("""virtual_volume_task_ids = """+str(virtual_volume_task_ids)+""";"""+"")
    try:
        ListVirtualVolumeTasksResult = ctx.element.list_virtual_volume_tasks(virtual_volume_task_ids=virtual_volume_task_ids)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(ListVirtualVolumeHostsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(ListVirtualVolumeTasksResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.



@cli.command('ListTasks', short_help="""ListVirtualVolumeTasks returns a list of VVol Async Tasks. """)
@click.option('--virtual_volume_task_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListTasks(ctx,
           virtual_volume_task_ids = None):
    """ListVirtualVolumeTasks returns a list of VVol Async Tasks."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    virtual_volume_task_ids = parser.parse_array(virtual_volume_task_ids)

    ctx.logger.info("""virtual_volume_task_ids = """+str(virtual_volume_task_ids)+""";"""+"")
    try:
        ListVirtualVolumeTasksResult = ctx.element.list_virtual_volume_tasks(virtual_volume_task_ids=virtual_volume_task_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(ListVirtualVolumeTasksResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(ListVirtualVolumeBindingsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.



@cli.command('List', short_help="""ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset. """)
@click.option('--details',
              type=bool,
              required=False,
              help="""Possible values:true: Include more details about each VVOL in the response.false: Include the standard level of detail about each VVOL in the response. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of virtual volumes to list. """)
@click.option('--recursive',
              type=bool,
              required=False,
              help="""Possible values:true: Include information about the children of each VVOL in the response.false: Do not include information about the children of each VVOL in the response. """)
@click.option('--start_virtual_volume_id',
              type=str,
<<<<<<< HEAD
              required=True,
              help="""Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def EnableFeature(ctx,
           feature):
    """EnableFeature allows you to enable cluster features that are disabled by default."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        EnableFeatureResult = ctx.element.enable_feature(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(EnableFeatureResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset. """)
@click.option('--details',
              type=bool,
              required=False,
              help="""Possible values:true: Include more details about each VVOL in the response.false: Include the standard level of detail about each VVOL in the response. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of virtual volumes to list. """)
@click.option('--recursive',
              type=bool,
              required=False,
              help="""Possible values:true: Include information about the children of each VVOL in the response.false: Do not include information about the children of each VVOL in the response. """)
@click.option('--start_virtual_volume_id',
              type=str,
              required=False,
              help="""The ID of the virtual volume at which to begin the list. """)
@click.option('--virtual_volume_ids',
=======
              required=False,
              help="""The ID of the virtual volume at which to begin the list. """)
@click.option('--virtual_volume_ids',
              type=str,
              required=False,
              help="""A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
def List(ctx,
           details = None,
           limit = None,
           recursive = None,
           start_virtual_volume_id = None,
           virtual_volume_ids = None):
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    virtual_volume_ids = parser.parse_array(virtual_volume_ids)

    ctx.logger.info("""details = """+str(details)+""";"""+"""limit = """+str(limit)+""";"""+"""recursive = """+str(recursive)+""";"""+"""start_virtual_volume_id = """+str(start_virtual_volume_id)+""";"""+"""virtual_volume_ids = """+str(virtual_volume_ids)+""";"""+"")
    try:
        ListVirtualVolumesResult = ctx.element.list_virtual_volumes(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=start_virtual_volume_id, virtual_volume_ids=virtual_volume_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVirtualVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListHosts', short_help="""ListVirtualVolumeHosts returns a list of known ESX hosts. """)
@click.option('--virtual_volume_host_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListHosts(ctx,
           virtual_volume_host_ids = None):
    """ListVirtualVolumeHosts returns a list of known ESX hosts."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    virtual_volume_host_ids = parser.parse_array(virtual_volume_host_ids)

    ctx.logger.info("""virtual_volume_host_ids = """+str(virtual_volume_host_ids)+""";"""+"")
    try:
        ListVirtualVolumeHostsResult = ctx.element.list_virtual_volume_hosts(virtual_volume_host_ids=virtual_volume_host_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVirtualVolumeHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetTaskUpdate', short_help="""GetVirtualVolumeTaskUpdate checks the status of a VVol Async Task. """)
@click.option('--virtual_volume_task_id',
              type=str,
              required=True,
              help="""The UUID of the VVol Task. """)
@click.option('--calling_virtual_volume_host_id',
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
              type=str,
              required=False,
              help="""A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
<<<<<<< HEAD
def List(ctx,
           details = None,
           limit = None,
           recursive = None,
           start_virtual_volume_id = None,
           virtual_volume_ids = None):
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset."""
=======
def GetTaskUpdate(ctx,
           virtual_volume_task_id,
           calling_virtual_volume_host_id = None):
    """GetVirtualVolumeTaskUpdate checks the status of a VVol Async Task."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
    virtual_volume_ids = parser.parse_array(virtual_volume_ids)

    ctx.logger.info("""details = """+str(details)+""";"""+"""limit = """+str(limit)+""";"""+"""recursive = """+str(recursive)+""";"""+"""start_virtual_volume_id = """+str(start_virtual_volume_id)+""";"""+"""virtual_volume_ids = """+str(virtual_volume_ids)+""";"""+"")
    try:
        ListVirtualVolumesResult = ctx.element.list_virtual_volumes(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=start_virtual_volume_id, virtual_volume_ids=virtual_volume_ids)
=======
    ctx.logger.info("""virtual_volume_task_id = """+str(virtual_volume_task_id)+""";"""+"""calling_virtual_volume_host_id = """+str(calling_virtual_volume_host_id)+""";"""+"")
    try:
        VirtualVolumeTaskResult = ctx.element.get_virtual_volume_task_update(virtual_volume_task_id=virtual_volume_task_id, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(ListVirtualVolumesResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(VirtualVolumeTaskResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.



@cli.command('ListBindings', short_help="""ListVirtualVolumeBindings returns a list of VVol bindings. """)
@click.option('--virtual_volume_binding_ids',
              type=str,
              required=False,
              help="""""")
@pass_context
def ListBindings(ctx,
           virtual_volume_binding_ids = None):
    """ListVirtualVolumeBindings returns a list of VVol bindings."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    virtual_volume_binding_ids = parser.parse_array(virtual_volume_binding_ids)

    ctx.logger.info("""virtual_volume_binding_ids = """+str(virtual_volume_binding_ids)+""";"""+"")
    try:
        ListVirtualVolumeBindingsResult = ctx.element.list_virtual_volume_bindings(virtual_volume_binding_ids=virtual_volume_binding_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(ListVirtualVolumeBindingsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetCount', short_help="""Enables retrieval of the number of virtual volumes currently in the system. """)
@pass_context
def GetCount(ctx):
    """Enables retrieval of the number of virtual volumes currently in the system."""
=======
    cli_utils.print_result(PrepareVirtualSnapshotResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CreateHost', short_help="""CreateVirtualVolumeHost creates a new ESX host. """)
@click.option('--virtual_volume_host_id',
              type=str,
              required=True,
              help="""The GUID of the ESX host. """)
@click.option('--cluster_id',
              type=str,
              required=True,
              help="""The GUID of the ESX Cluster. """)
@click.option('--initiator_names',
              type=str,
              required=False,
              help="""""")
@click.option('--visible_protocol_endpoint_ids',
              type=str,
              required=False,
              help="""A list of PEs the host is aware of. """)
@click.option('--host_address',
              type=str,
              required=False,
              help="""IP or DNS name for the host. """)
@click.option('--calling_virtual_volume_host_id',
              type=str,
              required=False,
              help="""""")
@pass_context
def CreateHost(ctx,
           virtual_volume_host_id,
           cluster_id,
           initiator_names = None,
           visible_protocol_endpoint_ids = None,
           host_address = None,
           calling_virtual_volume_host_id = None):
    """CreateVirtualVolumeHost creates a new ESX host."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
    ctx.logger.info("")
    try:
        GetVirtualVolumeCountResult = ctx.element.get_virtual_volume_count()
=======
    initiator_names = parser.parse_array(initiator_names)

    visible_protocol_endpoint_ids = parser.parse_array(visible_protocol_endpoint_ids)

    ctx.logger.info("""virtual_volume_host_id = """+str(virtual_volume_host_id)+""";"""+"""cluster_id = """+str(cluster_id)+""";"""+"""initiator_names = """+str(initiator_names)+""";"""+"""visible_protocol_endpoint_ids = """+str(visible_protocol_endpoint_ids)+""";"""+"""host_address = """+str(host_address)+""";"""+"""calling_virtual_volume_host_id = """+str(calling_virtual_volume_host_id)+""";"""+"")
    try:
        VirtualVolumeNullResult = ctx.element.create_virtual_volume_host(virtual_volume_host_id=virtual_volume_host_id, cluster_id=cluster_id, initiator_names=initiator_names, visible_protocol_endpoint_ids=visible_protocol_endpoint_ids, host_address=host_address, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(GetVirtualVolumeCountResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(VirtualVolumeNullResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.



@cli.command('GetFeatureStatus', short_help="""GetFeatureStatus allows you to retrieve the status of a cluster feature. """)
@click.option('--feature',
              type=str,
              required=False,
              help="""Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def GetFeatureStatus(ctx,
           feature = None):
    """GetFeatureStatus allows you to retrieve the status of a cluster feature."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        GetFeatureStatusResult = ctx.element.get_feature_status(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(GetFeatureStatusResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(VirtualVolumeUnsharedChunkResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetCount', short_help="""Enables retrieval of the number of virtual volumes currently in the system. """)
@pass_context
def GetCount(ctx):
    """Enables retrieval of the number of virtual volumes currently in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        GetVirtualVolumeCountResult = ctx.element.get_virtual_volume_count()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetVirtualVolumeCountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.

