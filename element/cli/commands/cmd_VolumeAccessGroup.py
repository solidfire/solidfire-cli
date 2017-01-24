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
    """ModifyLunAssignments List Modify Delete AddVolumesTo RemoveInitiatorsFrom AddInitiatorsTo GetLunAssignments GetEfficiency RemoveVolumesFrom Create """

@cli.command('ModifyLunAssignments', short_help="""The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged.  LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups.  Note: Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception.  Caution: If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments. """)
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="""Unique volume access group ID for which the LUN assignments will be modified. """)
@click.option('--lun_assignment_volume_id',
              type=int,
              required=True,
              help="""The volume ID assigned to the Lun. """)
@click.option('--lun_assignment_lun',
              type=int,
              required=True,
              help="""Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. """)
@pass_context
def ModifyLunAssignments(ctx,
           volume_access_group_id,
           lun_assignment_volume_id,
           lun_assignment_lun):
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



    lun_assignments = None
    if(volume_access_group_id is not None or lun_assignments is not None or False):
        kwargsDict = dict()
        kwargsDict["volume_id"] = lun_assignment_volume_id
        kwargsDict["lun"] = lun_assignment_lun

        lun_assignments = LunAssignment(**kwargsDict)

    lun_assignments = parser.parse_array(lun_assignments)

    ctx.logger.info("""volume_access_group_id = """+str(volume_access_group_id)+""";"""+"""lun_assignments = """+str(lun_assignments)+""";"""+"")
    try:
        ModifyVolumeAccessGroupLunAssignmentsResult = ctx.element.modify_volume_access_group_lun_assignments(volume_access_group_id=volume_access_group_id, lun_assignments=lun_assignments)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ModifyVolumeAccessGroupLunAssignmentsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""ListVolumeAccessGroups is used to return information about the volume access groups that are currently in the system. """)
@click.option('--start_volume_access_group_id',
              type=int,
              required=False,
              help="""The lowest VolumeAccessGroupID to return. This can be useful for paging. If unspecified, there is no lower limit (implicitly 0). """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of results to return. This can be useful for paging. """)
@pass_context
def List(ctx,
           start_volume_access_group_id = None,
           limit = None):
    """ListVolumeAccessGroups is used to return information about the volume access groups that are currently in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""start_volume_access_group_id = """+str(start_volume_access_group_id)+""";"""+"""limit = """+str(limit)+""";"""+"")
    try:
        ListVolumeAccessGroupsResult = ctx.element.list_volume_access_groups(start_volume_access_group_id=start_volume_access_group_id, limit=limit)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListVolumeAccessGroupsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Modify', short_help="""Update initiators and add or remove volumes from a volume access group. A specified initiator or volume that duplicates an existing volume or initiator in a volume access group is left as-is. If a value is not specified for volumes or initiators, the current list of initiators and volumes are not changed.  Often, it is easier to use the convenience functions to modify initiators and volumes independently:  AddInitiatorsToVolumeAccessGroup RemoveInitiatorsFromVolumeAccessGroup AddVolumesToVolumeAccessGroup RemoveVolumesFromVolumeAccessGroup """)
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--virtual_network_id',
              type=str,
              required=False,
              help="""The ID of the SolidFire Virtual Network ID to associate the volume access group with. """)
@click.option('--virtual_network_tags',
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
def Modify(ctx,
           volume_access_group_id,
           virtual_network_id = None,
           virtual_network_tags = None,
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



    virtual_network_id = parser.parse_array(virtual_network_id)

    virtual_network_tags = parser.parse_array(virtual_network_tags)

    initiators = parser.parse_array(initiators)

    volumes = parser.parse_array(volumes)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""volume_access_group_id = """+str(volume_access_group_id)+""";"""+"""virtual_network_id = """+str(virtual_network_id)+""";"""+"""virtual_network_tags = """+str(virtual_network_tags)+""";"""+"""name = """+str(name)+""";"""+"""initiators = """+str(initiators)+""";"""+"""volumes = """+str(volumes)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        ModifyVolumeAccessGroupResult = ctx.element.modify_volume_access_group(volume_access_group_id=volume_access_group_id, virtual_network_id=virtual_network_id, virtual_network_tags=virtual_network_tags, name=name, initiators=initiators, volumes=volumes, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Delete', short_help="""Delete a volume access group from the system. """)
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="""The ID of the volume access group to delete. """)
@pass_context
def Delete(ctx,
           volume_access_group_id):
    """Delete a volume access group from the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_access_group_id = """+str(volume_access_group_id)+""";"""+"")
    try:
        DeleteVolumeAccessGroupResult = ctx.element.delete_volume_access_group(volume_access_group_id=volume_access_group_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(DeleteVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('AddVolumesTo', short_help="""Add volumes to a volume access group. """)
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--volumes',
              type=str,
              required=True,
              help="""List of volumes to add to this volume access group. """)
@pass_context
def AddVolumesTo(ctx,
           volume_access_group_id,
           volumes):
    """Add volumes to a volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    volumes = parser.parse_array(volumes)

    ctx.logger.info("""volume_access_group_id = """+str(volume_access_group_id)+""";"""+"""volumes = """+str(volumes)+""";"""+"")
    try:
        ModifyVolumeAccessGroupResult = ctx.element.add_volumes_to_volume_access_group(volume_access_group_id=volume_access_group_id, volumes=volumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveInitiatorsFrom', short_help="""Remove initiators from a volume access group. """)
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--initiators',
              type=str,
              required=True,
              help="""List of initiators to remove from the volume access group. """)
@pass_context
def RemoveInitiatorsFrom(ctx,
           volume_access_group_id,
           initiators):
    """Remove initiators from a volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = parser.parse_array(initiators)

    ctx.logger.info("""volume_access_group_id = """+str(volume_access_group_id)+""";"""+"""initiators = """+str(initiators)+""";"""+"")
    try:
        ModifyVolumeAccessGroupResult = ctx.element.remove_initiators_from_volume_access_group(volume_access_group_id=volume_access_group_id, initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('AddInitiatorsTo', short_help="""Add initiators to a volume access group. """)
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--initiators',
              type=str,
              required=True,
              help="""List of initiators to add to the volume access group. """)
@pass_context
def AddInitiatorsTo(ctx,
           volume_access_group_id,
           initiators):
    """Add initiators to a volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = parser.parse_array(initiators)

    ctx.logger.info("""volume_access_group_id = """+str(volume_access_group_id)+""";"""+"""initiators = """+str(initiators)+""";"""+"")
    try:
        ModifyVolumeAccessGroupResult = ctx.element.add_initiators_to_volume_access_group(volume_access_group_id=volume_access_group_id, initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetLunAssignments', short_help="""The GetVolumeAccessGroupLunAssignments is used to return information LUN mappings of a specified volume access group. """)
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="""Unique volume access group ID used to return information. """)
@pass_context
def GetLunAssignments(ctx,
           volume_access_group_id):
    """The GetVolumeAccessGroupLunAssignments is used to return information LUN mappings of a specified volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_access_group_id = """+str(volume_access_group_id)+""";"""+"")
    try:
        GetVolumeAccessGroupLunAssignmentsResult = ctx.element.get_volume_access_group_lun_assignments(volume_access_group_id=volume_access_group_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetVolumeAccessGroupLunAssignmentsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetEfficiency', short_help="""GetVolumeAccessGroupEfficiency is used to retrieve efficiency information about a volume access group. Only the volume access group provided as parameters in this API method is used to compute the capacity. """)
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="""Specifies the volume access group for which capacity is computed. """)
@pass_context
def GetEfficiency(ctx,
           volume_access_group_id):
    """GetVolumeAccessGroupEfficiency is used to retrieve efficiency information about a volume access group. Only the volume access group provided as parameters in this API method is used to compute the capacity."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""volume_access_group_id = """+str(volume_access_group_id)+""";"""+"")
    try:
        GetEfficiencyResult = ctx.element.get_volume_access_group_efficiency(volume_access_group_id=volume_access_group_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveVolumesFrom', short_help="""Remove volumes from a volume access group. """)
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--volumes',
              type=str,
              required=True,
              help="""List of volumes to remove from this volume access group. """)
@pass_context
def RemoveVolumesFrom(ctx,
           volume_access_group_id,
           volumes):
    """Remove volumes from a volume access group."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    volumes = parser.parse_array(volumes)

    ctx.logger.info("""volume_access_group_id = """+str(volume_access_group_id)+""";"""+"""volumes = """+str(volumes)+""";"""+"")
    try:
        ModifyVolumeAccessGroupResult = ctx.element.remove_volumes_from_volume_access_group(volume_access_group_id=volume_access_group_id, volumes=volumes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Create', short_help="""Creates a new volume access group. The new volume access group must be given a name when it is created. Entering initiators and volumes are optional when creating a volume access group. Once the group is created volumes and initiator IQNs can be added. Any initiator IQN that is successfully added to the volume access group is able to access any volume in the group without CHAP authentication. """)
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
@click.option('--virtual_network_id',
              type=str,
              required=False,
              help="""The ID of the SolidFire Virtual Network ID to associate the volume access group with. """)
@click.option('--virtual_network_tags',
              type=str,
              required=False,
              help="""The ID of the VLAN Virtual Network Tag to associate the volume access group with. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Create(ctx,
           name,
           initiators = None,
           volumes = None,
           virtual_network_id = None,
           virtual_network_tags = None,
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

    virtual_network_id = parser.parse_array(virtual_network_id)

    virtual_network_tags = parser.parse_array(virtual_network_tags)
    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ctx.logger.info("""name = """+str(name)+""";"""+"""initiators = """+str(initiators)+""";"""+"""volumes = """+str(volumes)+""";"""+"""virtual_network_id = """+str(virtual_network_id)+""";"""+"""virtual_network_tags = """+str(virtual_network_tags)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        CreateVolumeAccessGroupResult = ctx.element.create_volume_access_group(name=name, initiators=initiators, volumes=volumes, virtual_network_id=virtual_network_id, virtual_network_tags=virtual_network_tags, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CreateVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

