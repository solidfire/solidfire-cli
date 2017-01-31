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


@click.group()
@pass_context
def cli(ctx):
<<<<<<< HEAD
    """listhosts listtasks getfeaturestatus list listbindings getcount enablefeature """

@cli.command('listhosts', short_help="""ListVirtualVolumeHosts returns a list of known ESX hosts. """)
@click.option('--virtualvolumehostids',
=======
    """listtasks list getcount getfeaturestatus listbindings enablefeature listhosts """

@cli.command('listtasks', short_help="""ListVirtualVolumeTasks returns a list of VVol Async Tasks. """)
@click.option('--virtualvolumetaskids',
>>>>>>> Fixes the modifylunassignments bug
              type=str,
              required=False,
              help="""""")
@pass_context
<<<<<<< HEAD
def listhosts(ctx,
           virtualvolumehostids = None):
    """ListVirtualVolumeHosts returns a list of known ESX hosts."""
=======
def listtasks(ctx,
           virtualvolumetaskids = None):
    """ListVirtualVolumeTasks returns a list of VVol Async Tasks."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
    virtualvolumehostids = parser.parse_array(virtualvolumehostids)
    

    ctx.logger.info("""virtualvolumehostids = """+str(virtualvolumehostids)+""";"""+"")
    try:
        _ListVirtualVolumeHostsResult = ctx.element.list_virtual_volume_hosts(virtual_volume_host_ids=virtualvolumehostids)
=======
    virtualvolumetaskids = parser.parse_array(virtualvolumetaskids)
    

    ctx.logger.info("""virtualvolumetaskids = """+str(virtualvolumetaskids)+""";"""+"")
    try:
        _ListVirtualVolumeTasksResult = ctx.element.list_virtual_volume_tasks(virtual_volume_task_ids=virtualvolumetaskids)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_ListVirtualVolumeHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listtasks', short_help="""ListVirtualVolumeTasks returns a list of VVol Async Tasks. """)
@click.option('--virtualvolumetaskids',
              type=str,
              required=False,
              help="""""")
@pass_context
def listtasks(ctx,
           virtualvolumetaskids = None):
    """ListVirtualVolumeTasks returns a list of VVol Async Tasks."""
=======
    cli_utils.print_result(_ListVirtualVolumeTasksResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset. """)
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
@click.option('--startvirtualvolumeid',
              type=str,
              required=False,
              help="""The ID of the virtual volume at which to begin the list. """)
@click.option('--virtualvolumeids',
              type=str,
              required=False,
              help="""A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
def list(ctx,
           details = None,
           limit = None,
           recursive = None,
           startvirtualvolumeid = None,
           virtualvolumeids = None):
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
    virtualvolumetaskids = parser.parse_array(virtualvolumetaskids)
    

    ctx.logger.info("""virtualvolumetaskids = """+str(virtualvolumetaskids)+""";"""+"")
    try:
        _ListVirtualVolumeTasksResult = ctx.element.list_virtual_volume_tasks(virtual_volume_task_ids=virtualvolumetaskids)
=======
    virtualvolumeids = parser.parse_array(virtualvolumeids)
    

    ctx.logger.info("""details = """+str(details)+""";"""+"""limit = """+str(limit)+""";"""+"""recursive = """+str(recursive)+""";"""+"""startvirtualvolumeid = """+str(startvirtualvolumeid)+""";"""+"""virtualvolumeids = """+str(virtualvolumeids)+""";"""+"")
    try:
        _ListVirtualVolumesResult = ctx.element.list_virtual_volumes(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=startvirtualvolumeid, virtual_volume_ids=virtualvolumeids)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_ListVirtualVolumeTasksResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(_ListVirtualVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Fixes the modifylunassignments bug



@cli.command('getfeaturestatus', short_help="""GetFeatureStatus allows you to retrieve the status of a cluster feature. """)
@click.option('--feature',
              type=str,
              required=False,
              help="""Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def getfeaturestatus(ctx,
           feature = None):
    """GetFeatureStatus allows you to retrieve the status of a cluster feature."""
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



<<<<<<< HEAD
@cli.command('list', short_help="""ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset. """)
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
@click.option('--startvirtualvolumeid',
              type=str,
              required=False,
              help="""The ID of the virtual volume at which to begin the list. """)
@click.option('--virtualvolumeids',
              type=str,
              required=False,
              help="""A list of virtual volume  IDs for which to retrieve information. If you specify this parameter, the method returns information about only these virtual volumes. """)
@pass_context
def list(ctx,
           details = None,
           limit = None,
           recursive = None,
           startvirtualvolumeid = None,
           virtualvolumeids = None):
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset."""
=======
@cli.command('getfeaturestatus', short_help="""GetFeatureStatus allows you to retrieve the status of a cluster feature. """)
@click.option('--feature',
              type=str,
              required=False,
              help="""Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def getfeaturestatus(ctx,
           feature = None):
    """GetFeatureStatus allows you to retrieve the status of a cluster feature."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


<<<<<<< HEAD

    virtualvolumeids = parser.parse_array(virtualvolumeids)
    

    ctx.logger.info("""details = """+str(details)+""";"""+"""limit = """+str(limit)+""";"""+"""recursive = """+str(recursive)+""";"""+"""startvirtualvolumeid = """+str(startvirtualvolumeid)+""";"""+"""virtualvolumeids = """+str(virtualvolumeids)+""";"""+"")
    try:
        _ListVirtualVolumesResult = ctx.element.list_virtual_volumes(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=startvirtualvolumeid, virtual_volume_ids=virtualvolumeids)
=======
    

    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        _GetFeatureStatusResult = ctx.element.get_feature_status(feature=feature)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_ListVirtualVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(_GetFeatureStatusResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Fixes the modifylunassignments bug



@cli.command('listbindings', short_help="""ListVirtualVolumeBindings returns a list of VVol bindings. """)
@click.option('--virtualvolumebindingids',
              type=str,
              required=False,
              help="""""")
@pass_context
def listbindings(ctx,
           virtualvolumebindingids = None):
    """ListVirtualVolumeBindings returns a list of VVol bindings."""
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



<<<<<<< HEAD
@cli.command('getcount', short_help="""Enables retrieval of the number of virtual volumes currently in the system. """)
@pass_context
def getcount(ctx):
    """Enables retrieval of the number of virtual volumes currently in the system."""
=======
@cli.command('enablefeature', short_help="""EnableFeature allows you to enable cluster features that are disabled by default. """)
@click.option('--feature',
              type=str,
              required=True,
              help="""Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def enablefeature(ctx,
           feature):
    """EnableFeature allows you to enable cluster features that are disabled by default."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

<<<<<<< HEAD
    ctx.logger.info("")
    try:
        _GetVirtualVolumeCountResult = ctx.element.get_virtual_volume_count()
=======
    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        _EnableFeatureResult = ctx.element.enable_feature(feature=feature)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_GetVirtualVolumeCountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enablefeature', short_help="""EnableFeature allows you to enable cluster features that are disabled by default. """)
@click.option('--feature',
              type=str,
              required=True,
              help="""Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def enablefeature(ctx,
           feature):
    """EnableFeature allows you to enable cluster features that are disabled by default."""
=======
    cli_utils.print_result(_EnableFeatureResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listhosts', short_help="""ListVirtualVolumeHosts returns a list of known ESX hosts. """)
@click.option('--virtualvolumehostids',
              type=str,
              required=False,
              help="""""")
@pass_context
def listhosts(ctx,
           virtualvolumehostids = None):
    """ListVirtualVolumeHosts returns a list of known ESX hosts."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


<<<<<<< HEAD
    

    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        _EnableFeatureResult = ctx.element.enable_feature(feature=feature)
=======

    virtualvolumehostids = parser.parse_array(virtualvolumehostids)
    

    ctx.logger.info("""virtualvolumehostids = """+str(virtualvolumehostids)+""";"""+"")
    try:
        _ListVirtualVolumeHostsResult = ctx.element.list_virtual_volume_hosts(virtual_volume_host_ids=virtualvolumehostids)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_EnableFeatureResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(_ListVirtualVolumeHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Fixes the modifylunassignments bug

