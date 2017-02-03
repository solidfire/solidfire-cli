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
    """removevolumesfrom create modifylunassignments list modify addinitiatorsto getlunassignments addvolumesto removeinitiatorsfrom getefficiency delete """

@cli.command('removevolumesfrom', short_help="""Remove volumes from a volume access group. """)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--volumes',
              type=str,
              required=True,
              help="""List of volumes to remove from this volume access group. """)
@pass_context
def removevolumesfrom(ctx,
           volumeaccessgroupid,
           volumes):
    """Remove volumes from a volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    volumes = parser.parse_array(volumes)
    

    ctx.logger.info("""volumeaccessgroupid = """+str(volumeaccessgroupid)+""";"""+"""volumes = """+str(volumes)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupResult = ctx.element.remove_volumes_from_volume_access_group(volume_access_group_id=volumeaccessgroupid, volumes=volumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""Creates a new volume access group. The new volume access group must be given a name when it is created. Entering initiators and volumes are optional when creating a volume access group. Once the group is created volumes and initiator IQNs can be added. Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication. """)
@click.option('--name',
              type=str,
              required=True,
              help="""Name of the volume access group. It is not required to be unique, but recommended. """)
@click.option('--initiators',
              type=str,
              required=False,
              help="""List of initiators to include in the volume access group. If unspecified, the access group will start out without configured initiators. """)
@click.option('--volumes',
              type=str,
              required=False,
              help="""List of volumes to initially include in the volume access group. If unspecified, the access group will start without any volumes. """)
@click.option('--virtualnetworkid',
              type=str,
              required=False,
              help="""The ID of the SolidFire Virtual Network ID to associate the volume access group with. """)
@click.option('--virtualnetworktags',
              type=str,
              required=False,
              help="""The ID of the VLAN Virtual Network Tag to associate the volume access group with. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def create(ctx,
           name,
           initiators = None,
           volumes = None,
           virtualnetworkid = None,
           virtualnetworktags = None,
           attributes = None):
    """Creates a new volume access group."""
    """The new volume access group must be given a name when it is created."""
    """Entering initiators and volumes are optional when creating a volume access group."""
    """Once the group is created volumes and initiator IQNs can be added."""
    """Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = parser.parse_array(initiators)

    volumes = parser.parse_array(volumes)

    virtualnetworkid = parser.parse_array(virtualnetworkid)

    virtualnetworktags = parser.parse_array(virtualnetworktags)
    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1) 
        attributes = dict(**kwargsDict)
    

    ctx.logger.info("""name = """+str(name)+""";"""+"""initiators = """+str(initiators)+""";"""+"""volumes = """+str(volumes)+""";"""+"""virtualnetworkid = """+str(virtualnetworkid)+""";"""+"""virtualnetworktags = """+str(virtualnetworktags)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _CreateVolumeAccessGroupResult = ctx.element.create_volume_access_group(name=name, initiators=initiators, volumes=volumes, virtual_network_id=virtualnetworkid, virtual_network_tags=virtualnetworktags, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifylunassignments', short_help="""The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.  LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.  Note: Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.  Caution: If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments. """)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              help="""Unique volume access group ID for which the LUN assignments will be modified. """)
@click.option('--lunassignments',
              type=str,
              required=True,
              help="""Provide in json format: The volume IDs with new assigned LUN values. """)
@pass_context
def modifylunassignments(ctx,
           volumeaccessgroupid,
           lunassignments):
    """The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged."""
    """"""
    """LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups."""
    """"""
    """Note: Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception."""
    """"""
    """Caution: If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(lunassignments is not None):
        try:
            kwargsDict = simplejson.loads(lunassignments)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1) 
        lunassignments = [LunAssignment(**argsOfInterest) for argsOfInterest in kwargsDict]
    

    ctx.logger.info("""volumeaccessgroupid = """+str(volumeaccessgroupid)+""";"""+"""lunassignments = """+str(lunassignments)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupLunAssignmentsResult = ctx.element.modify_volume_access_group_lun_assignments(volume_access_group_id=volumeaccessgroupid, lun_assignments=lunassignments)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyVolumeAccessGroupLunAssignmentsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListVolumeAccessGroups is used to return information about the volume access groups that are currently in the system. """)
@click.option('--startvolumeaccessgroupid',
              type=int,
              required=False,
              help="""The lowest VolumeAccessGroupID to return. This can be useful for paging. If unspecified, there is no lower limit (implicitly 0). """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of results to return. This can be useful for paging. """)
@pass_context
def list(ctx,
           startvolumeaccessgroupid = None,
           limit = None):
    """ListVolumeAccessGroups is used to return information about the volume access groups that are currently in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""startvolumeaccessgroupid = """+str(startvolumeaccessgroupid)+""";"""+"""limit = """+str(limit)+""";"""+"")
    try:
        _ListVolumeAccessGroupsResult = ctx.element.list_volume_access_groups(start_volume_access_group_id=startvolumeaccessgroupid, limit=limit)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListVolumeAccessGroupsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""Update initiators and add or remove volumes from a volume access group. A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is. If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.  Often, it is easier to use the convenience functions to modify initiators and volumes independently:  AddInitiatorsToVolumeAccessGroup RemoveInitiatorsFromVolumeAccessGroup AddVolumesToVolumeAccessGroup RemoveVolumesFromVolumeAccessGroup """)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--virtualnetworkid',
              type=str,
              required=False,
              help="""The ID of the SolidFire Virtual Network ID to associate the volume access group with. """)
@click.option('--virtualnetworktags',
              type=str,
              required=False,
              help="""The ID of the VLAN Virtual Network Tag to associate the volume access group with. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name of the volume access group. It is not required to be unique, but recommended. """)
@click.option('--initiators',
              type=str,
              required=False,
              help="""List of initiators to include in the volume access group. If unspecified, the access group's configured initiators will not be modified. """)
@click.option('--volumes',
              type=str,
              required=False,
              help="""List of volumes to initially include in the volume access group. If unspecified, the access group's volumes will not be modified. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def modify(ctx,
           volumeaccessgroupid,
           virtualnetworkid = None,
           virtualnetworktags = None,
           name = None,
           initiators = None,
           volumes = None,
           attributes = None):
    """Update initiators and add or remove volumes from a volume access group."""
    """A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is."""
    """If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed."""
    """"""
    """Often, it is easier to use the convenience functions to modify initiators and volumes independently:"""
    """"""
    """AddInitiatorsToVolumeAccessGroup"""
    """RemoveInitiatorsFromVolumeAccessGroup"""
    """AddVolumesToVolumeAccessGroup"""
    """RemoveVolumesFromVolumeAccessGroup"""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    virtualnetworkid = parser.parse_array(virtualnetworkid)

    virtualnetworktags = parser.parse_array(virtualnetworktags)

    initiators = parser.parse_array(initiators)

    volumes = parser.parse_array(volumes)
    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1) 
        attributes = dict(**kwargsDict)
    

    ctx.logger.info("""volumeaccessgroupid = """+str(volumeaccessgroupid)+""";"""+"""virtualnetworkid = """+str(virtualnetworkid)+""";"""+"""virtualnetworktags = """+str(virtualnetworktags)+""";"""+"""name = """+str(name)+""";"""+"""initiators = """+str(initiators)+""";"""+"""volumes = """+str(volumes)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupResult = ctx.element.modify_volume_access_group(volume_access_group_id=volumeaccessgroupid, virtual_network_id=virtualnetworkid, virtual_network_tags=virtualnetworktags, name=name, initiators=initiators, volumes=volumes, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('addinitiatorsto', short_help="""Add initiators to a volume access group. """)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--initiators',
              type=str,
              required=True,
              help="""List of initiators to add to the volume access group. """)
@pass_context
def addinitiatorsto(ctx,
           volumeaccessgroupid,
           initiators):
    """Add initiators to a volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = parser.parse_array(initiators)
    

    ctx.logger.info("""volumeaccessgroupid = """+str(volumeaccessgroupid)+""";"""+"""initiators = """+str(initiators)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupResult = ctx.element.add_initiators_to_volume_access_group(volume_access_group_id=volumeaccessgroupid, initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getlunassignments', short_help="""The GetVolumeAccessGroupLunAssignments is used to return information LUN mappings of a specified volume access group. """)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              help="""Unique volume access group ID used to return information. """)
@pass_context
def getlunassignments(ctx,
           volumeaccessgroupid):
    """The GetVolumeAccessGroupLunAssignments is used to return information LUN mappings of a specified volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""volumeaccessgroupid = """+str(volumeaccessgroupid)+""";"""+"")
    try:
        _GetVolumeAccessGroupLunAssignmentsResult = ctx.element.get_volume_access_group_lun_assignments(volume_access_group_id=volumeaccessgroupid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetVolumeAccessGroupLunAssignmentsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('addvolumesto', short_help="""Add volumes to a volume access group. """)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--volumes',
              type=str,
              required=True,
              help="""List of volumes to add to this volume access group. """)
@pass_context
def addvolumesto(ctx,
           volumeaccessgroupid,
           volumes):
    """Add volumes to a volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    volumes = parser.parse_array(volumes)
    

    ctx.logger.info("""volumeaccessgroupid = """+str(volumeaccessgroupid)+""";"""+"""volumes = """+str(volumes)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupResult = ctx.element.add_volumes_to_volume_access_group(volume_access_group_id=volumeaccessgroupid, volumes=volumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('removeinitiatorsfrom', short_help="""Remove initiators from a volume access group. """)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--initiators',
              type=str,
              required=True,
              help="""List of initiators to remove from the volume access group. """)
@pass_context
def removeinitiatorsfrom(ctx,
           volumeaccessgroupid,
           initiators):
    """Remove initiators from a volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = parser.parse_array(initiators)
    

    ctx.logger.info("""volumeaccessgroupid = """+str(volumeaccessgroupid)+""";"""+"""initiators = """+str(initiators)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupResult = ctx.element.remove_initiators_from_volume_access_group(volume_access_group_id=volumeaccessgroupid, initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getefficiency', short_help="""GetVolumeAccessGroupEfficiency is used to retrieve efficiency information about a volume access group. Only the volume access group provided as parameters in this API method is used to compute the capacity. """)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              help="""Specifies the volume access group for which capacity is computed. """)
@pass_context
def getefficiency(ctx,
           volumeaccessgroupid):
    """GetVolumeAccessGroupEfficiency is used to retrieve efficiency information about a volume access group. Only the volume access group provided as parameters in this API method is used to compute the capacity."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""volumeaccessgroupid = """+str(volumeaccessgroupid)+""";"""+"")
    try:
        _GetEfficiencyResult = ctx.element.get_volume_access_group_efficiency(volume_access_group_id=volumeaccessgroupid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""Delete a volume access group from the system. """)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              help="""The ID of the volume access group to delete. """)
@pass_context
def delete(ctx,
           volumeaccessgroupid):
    """Delete a volume access group from the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""volumeaccessgroupid = """+str(volumeaccessgroupid)+""";"""+"")
    try:
        _DeleteVolumeAccessGroupResult = ctx.element.delete_volume_access_group(volume_access_group_id=volumeaccessgroupid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DeleteVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

