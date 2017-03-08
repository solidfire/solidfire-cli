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
    """listhosts listtasks enablefeature list listbindings getcount getfeaturestatus """

@cli.command('listhosts', short_help="""ListVirtualVolumeHosts returns a list of known ESX hosts. """, cls=SolidFireCommand)
@click.option('--virtualvolumehostids',
              type=str,
              required=False,
              help=""" """)
@pass_context
def listhosts(ctx,
           # Optional main parameter
           virtualvolumehostids = None):
    """ListVirtualVolumeHosts returns a list of known ESX hosts."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    virtualvolumehostids = parser.parse_array(virtualvolumehostids)
    

    ctx.logger.info("""virtualvolumehostids = """+str(virtualvolumehostids)+""";"""+"")
    try:
        _ListVirtualVolumeHostsResult = ctx.element.(virtual_volume_host_ids=virtualvolumehostids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVirtualVolumeHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listtasks', short_help="""ListVirtualVolumeTasks returns a list of VVol Async Tasks. """, cls=SolidFireCommand)
@click.option('--virtualvolumetaskids',
              type=str,
              required=False,
              help=""" """)
@pass_context
def listtasks(ctx,
           # Optional main parameter
           virtualvolumetaskids = None):
    """ListVirtualVolumeTasks returns a list of VVol Async Tasks."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    virtualvolumetaskids = parser.parse_array(virtualvolumetaskids)
    

    ctx.logger.info("""virtualvolumetaskids = """+str(virtualvolumetaskids)+""";"""+"")
    try:
        _ListVirtualVolumeTasksResult = ctx.element.(virtual_volume_task_ids=virtualvolumetaskids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVirtualVolumeTasksResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enablefeature', short_help="""EnableFeature allows you to enable cluster features that are disabled by default. """, cls=SolidFireCommand)
@click.option('--feature',
              type=str,
              required=True,
              help="""Valid values: vvols: Enable the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def enablefeature(ctx,
           # Mandatory main parameter
           feature):
    """EnableFeature allows you to enable cluster features that are disabled by default."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        _EnableFeatureResult = ctx.element.(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_EnableFeatureResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset. """, cls=SolidFireCommand)
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
    """ListVirtualVolumes enables you to list the virtual volumes currently in the system. You can use this method to list all virtual volumes, or only list a subset."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

                    

    virtualvolumeids = parser.parse_array(virtualvolumeids)
    

    ctx.logger.info("""details = """+str(details)+""";"""+"""limit = """+str(limit)+""";"""+"""recursive = """+str(recursive)+""";"""+"""startvirtualvolumeid = """+str(startvirtualvolumeid)+""";"""+"""virtualvolumeids = """+str(virtualvolumeids)+""";"""+"")
    try:
        _ListVirtualVolumesResult = ctx.element.(details=details, limit=limit, recursive=recursive, start_virtual_volume_id=startvirtualvolumeid, virtual_volume_ids=virtualvolumeids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVirtualVolumesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listbindings', short_help="""ListVirtualVolumeBindings returns a list of VVol bindings. """, cls=SolidFireCommand)
@click.option('--virtualvolumebindingids',
              type=str,
              required=False,
              help=""" """)
@pass_context
def listbindings(ctx,
           # Optional main parameter
           virtualvolumebindingids = None):
    """ListVirtualVolumeBindings returns a list of VVol bindings."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    virtualvolumebindingids = parser.parse_array(virtualvolumebindingids)
    

    ctx.logger.info("""virtualvolumebindingids = """+str(virtualvolumebindingids)+""";"""+"")
    try:
        _ListVirtualVolumeBindingsResult = ctx.element.(virtual_volume_binding_ids=virtualvolumebindingids)
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
        _GetVirtualVolumeCountResult = ctx.element.()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetVirtualVolumeCountResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getfeaturestatus', short_help="""GetFeatureStatus allows you to retrieve the status of a cluster feature. """, cls=SolidFireCommand)
@click.option('--feature',
              type=str,
              required=False,
              help="""Valid values: vvols: Find the status of the Virtual Volumes (VVOLs) cluster feature. """)
@pass_context
def getfeaturestatus(ctx,
           # Optional main parameter
           feature = None):
    """GetFeatureStatus allows you to retrieve the status of a cluster feature."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    
    

    ctx.logger.info("""feature = """+str(feature)+""";"""+"")
    try:
        _GetFeatureStatusResult = ctx.element.(feature=feature)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetFeatureStatusResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

