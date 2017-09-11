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
    """list create modify modifylunassignments getlunassignments getefficiency delete """

@cli.command('list', short_help="""ListVolumeAccessGroups enables you to return information about the volume access groups that are currently in the system. """, cls=SolidFireCommand)
@click.option('--startvolumeaccessgroupid',
              type=int,
              required=False,
              help="""The volume access group ID at which to begin the listing. If unspecified, there is no lower limit (implicitly 0). """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of results to return. This can be useful for paging. """)
@click.option('--volumeaccessgroups',
              type=str,
              required=False,
              help="""The list of ids of the volume access groups you wish to list """)
@pass_context
def list(ctx,
           # Optional main parameter
           startvolumeaccessgroupid = None,
           # Optional main parameter
           limit = None,
           # Optional main parameter
           volumeaccessgroups = None):
    """ListVolumeAccessGroups enables you to return"""
    """information about the volume access groups that are"""
    """currently in the system."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    volumeaccessgroups = parser.parse_array(volumeaccessgroups)
    

    ctx.logger.info(""": """"""startvolumeaccessgroupid = """+str(startvolumeaccessgroupid)+";" + """limit = """+str(limit)+";" + """volumeaccessgroups = """+str(volumeaccessgroups)+""";"""+"")
    try:
        _ListVolumeAccessGroupsResult = ctx.element.list_volume_access_groups(start_volume_access_group_id=startvolumeaccessgroupid, limit=limit, volume_access_groups=volumeaccessgroups)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListVolumeAccessGroupsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListVolumeAccessGroupsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""You can use CreateVolumeAccessGroup to create a new volume access group. When you create the volume access group, you need to give it a name, and you can optionally enter initiators and volumes. After you create the group, you can add volumes and initiator IQNs. Any initiator IQN that you add to the volume access group is able to access any volume in the group without CHAP authentication. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name for this volume access group. Not required to be unique, but recommended. """)
@click.option('--initiators',
              type=str,
              required=False,
              help="""List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. """)
@click.option('--volumes',
              type=str,
              required=False,
              help="""List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. """)
@click.option('--virtualnetworkid',
              type=str,
              required=False,
              help="""The ID of the SolidFire virtual network to associate the volume access group with. """)
@click.option('--virtualnetworktags',
              type=str,
              required=False,
              help="""The ID of the SolidFire virtual network to associate the volume access group with. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def create(ctx,
           # Mandatory main parameter
           name,
           # Optional main parameter
           initiators = None,
           # Optional main parameter
           volumes = None,
           # Optional main parameter
           virtualnetworkid = None,
           # Optional main parameter
           virtualnetworktags = None,
           # Optional main parameter
           attributes = None):
    """You can use CreateVolumeAccessGroup to create a new volume access group. When you create the volume access group, you need to give it a name, and you can optionally enter initiators and volumes. After you create the group, you can add volumes and initiator IQNs. Any initiator IQN that you add to the volume access group is able to access any volume in the group without CHAP authentication."""

    

    cli_utils.establish_connection(ctx)
    
    

    initiators = parser.parse_array(initiators)
    

    volumes = parser.parse_array(volumes)
    

    virtualnetworkid = parser.parse_array(virtualnetworkid)
    

    virtualnetworktags = parser.parse_array(virtualnetworktags)
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""name = """ + str(name)+";" + """initiators = """+str(initiators)+";" + """volumes = """+str(volumes)+";" + """virtualnetworkid = """+str(virtualnetworkid)+";" + """virtualnetworktags = """+str(virtualnetworktags)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _CreateVolumeAccessGroupResult = ctx.element.create_volume_access_group(name=name, initiators=initiators, volumes=volumes, virtual_network_id=virtualnetworkid, virtual_network_tags=virtualnetworktags, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateVolumeAccessGroupResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modify', short_help="""You can use ModifyVolumeAccessGroup to update initiators and add or remove volumes from a volume access group. If a specified initiator or volume is a duplicate of what currently exists, the volume access group is left as-is. If you do not specify a value for volumes or initiators, the current list of initiators and volumes is not changed. """, cls=SolidFireCommand)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume access group to modify. """)
@click.option('--virtualnetworkid',
              type=str,
              required=False,
              help="""The ID of the SolidFire virtual network to associate the volume access group with. """)
@click.option('--virtualnetworktags',
              type=str,
              required=False,
              help="""The ID of the SolidFire virtual network to associate the volume access group with. """)
@click.option('--name',
              type=str,
              required=False,
              help="""The new name for this volume access group. Not required to be unique, but recommended. """)
@click.option('--initiators',
              type=str,
              required=False,
              help="""List of initiators to include in the volume access group. If unspecified, the access group's configured initiators are not modified. """)
@click.option('--volumes',
              type=str,
              required=False,
              help="""List of volumes to initially include in the volume access group. If unspecified, the access group's volumes are not modified. """)
@click.option('--deleteorphaninitiators',
              type=bool,
              required=False,
              help="""true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           volumeaccessgroupid,
           # Optional main parameter
           virtualnetworkid = None,
           # Optional main parameter
           virtualnetworktags = None,
           # Optional main parameter
           name = None,
           # Optional main parameter
           initiators = None,
           # Optional main parameter
           volumes = None,
           # Optional main parameter
           deleteorphaninitiators = None,
           # Optional main parameter
           attributes = None):
    """You can use ModifyVolumeAccessGroup to update initiators and add or remove volumes from a volume access group. If a specified initiator or volume is a duplicate of what currently exists, the volume access group is left as-is. If you do not specify a value for volumes or initiators, the current list of initiators and volumes is not changed."""

    

    cli_utils.establish_connection(ctx)
    
    

    virtualnetworkid = parser.parse_array(virtualnetworkid)
    

    virtualnetworktags = parser.parse_array(virtualnetworktags)
    
    

    initiators = parser.parse_array(initiators)
    

    volumes = parser.parse_array(volumes)
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""volumeaccessgroupid = """ + str(volumeaccessgroupid)+";" + """virtualnetworkid = """+str(virtualnetworkid)+";" + """virtualnetworktags = """+str(virtualnetworktags)+";" + """name = """+str(name)+";" + """initiators = """+str(initiators)+";" + """volumes = """+str(volumes)+";" + """deleteorphaninitiators = """+str(deleteorphaninitiators)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupResult = ctx.element.modify_volume_access_group(volume_access_group_id=volumeaccessgroupid, virtual_network_id=virtualnetworkid, virtual_network_tags=virtualnetworktags, name=name, initiators=initiators, volumes=volumes, delete_orphan_initiators=deleteorphaninitiators, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyVolumeAccessGroupResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifylunassignments', short_help="""The ModifyVolumeAccessGroupLunAssignments method enables you to define custom LUN assignments for specific volumes. This method changes only LUN values set on the lunAssignments parameter in the volume access group. All other LUN assignments remain unchanged. LUN assignment values must be unique for volumes in a volume access group. You cannot define duplicate LUN values within a volume access group. However, you can use the same LUN values again in different volume access groups.  Note: Correct LUN values are 0 through 16383. The system generates an exception if you pass a LUN value outside of this range. None of the specified LUN assignments are modified if there is an exception.  Caution: If you change a LUN assignment for a volume with active I/O, the I/O can be disrupted. You might need to change the server configuration before changing volume LUN assignments. """, cls=SolidFireCommand)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume access group for which the LUN assignments will be modified. """)
@click.option('--lunassignments',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["volumeid", "lun", ],
              required=True,
              help="""The volume IDs with new assigned LUN values.  Has the following subparameters: --volumeid --lun """)
@click.option('--volumeid',
              required=True,
              prompt=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] The volume ID assigned to the Lun. """,
              cls=SolidFireOption)
@click.option('--lun',
              required=True,
              prompt=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. """,
              cls=SolidFireOption)
@pass_context
def modifylunassignments(ctx,
           # Mandatory main parameter
           volumeaccessgroupid,
           # Mandatory main parameter
           lunassignments,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           volumeid,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           lun):
    """The ModifyVolumeAccessGroupLunAssignments"""
    """method enables you to define custom LUN assignments"""
    """for specific volumes. This method changes only LUN"""
    """values set on the lunAssignments parameter in the"""
    """volume access group. All other LUN assignments remain"""
    """unchanged. LUN assignment values must be unique for volumes in a volume access group. You cannot define duplicate LUN values within a volume access group. However, you can use the same LUN values again in different volume access groups. """
    """Note: Correct LUN values are 0 through 16383. The system generates an exception if you pass a LUN value outside of this range. None of the specified LUN assignments are modified if there is an exception. """
    """Caution: If you change a LUN assignment for a volume with active I/O, the I/O can be disrupted. You might need to change the server configuration before changing volume LUN assignments."""

    

    cli_utils.establish_connection(ctx)
    
    

    lunassignmentsArray = None
    if len(lunassignments) == 1 and volumeid[0] is None and lun[0] is None:
        lunassignmentsArray = []
    elif(lunassignments is not None and lunassignments != ()):
        lunassignmentsArray = []
        try:
            for i, _lunassignments in enumerate(lunassignments):
                lunassignmentsArray.append(LunAssignment(volume_id=volumeid[i], lun=lun[i], ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""volumeaccessgroupid = """ + str(volumeaccessgroupid)+";"+"""lunassignments = """ + str(lunassignmentsArray)+""";"""+"")
    try:
        _ModifyVolumeAccessGroupLunAssignmentsResult = ctx.element.modify_volume_access_group_lun_assignments(volume_access_group_id=volumeaccessgroupid, lun_assignments=lunassignmentsArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyVolumeAccessGroupLunAssignmentsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyVolumeAccessGroupLunAssignmentsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getlunassignments', short_help="""The GetVolumeAccessGroupLunAssignments method enables you to retrieve details on LUN mappings of a specified volume access group. """, cls=SolidFireCommand)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              prompt=True,
              help="""The unique volume access group ID used to return information. """)
@pass_context
def getlunassignments(ctx,
           # Mandatory main parameter
           volumeaccessgroupid):
    """The GetVolumeAccessGroupLunAssignments"""
    """method enables you to retrieve details on LUN mappings"""
    """of a specified volume access group."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""volumeaccessgroupid = """ + str(volumeaccessgroupid)+""";"""+"")
    try:
        _GetVolumeAccessGroupLunAssignmentsResult = ctx.element.get_volume_access_group_lun_assignments(volume_access_group_id=volumeaccessgroupid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetVolumeAccessGroupLunAssignmentsResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetVolumeAccessGroupLunAssignmentsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getefficiency', short_help="""GetVolumeAccessGroupEfficiency enables you to retrieve efficiency information about a volume access group. Only the volume access group you provide as the parameter in this API method is used to compute the capacity. """, cls=SolidFireCommand)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              prompt=True,
              help="""The volume access group for which capacity is computed. """)
@pass_context
def getefficiency(ctx,
           # Mandatory main parameter
           volumeaccessgroupid):
    """GetVolumeAccessGroupEfficiency enables you to"""
    """retrieve efficiency information about a volume access"""
    """group. Only the volume access group you provide as the"""
    """parameter in this API method is used to compute the"""
    """capacity."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""volumeaccessgroupid = """ + str(volumeaccessgroupid)+""";"""+"")
    try:
        _GetEfficiencyResult = ctx.element.get_volume_access_group_efficiency(volume_access_group_id=volumeaccessgroupid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetEfficiencyResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""DeleteVolumeAccessGroup enables you to delete a volume access group. """, cls=SolidFireCommand)
@click.option('--volumeaccessgroupid',
              type=int,
              required=True,
              prompt=True,
              help="""The ID of the volume access group to be deleted. """)
@click.option('--deleteorphaninitiators',
              type=bool,
              required=False,
              help="""true: Delete initiator objects after they are removed from a volume access group. false: Do not delete initiator objects after they are removed from a volume access group. """)
@click.option('--force',
              type=bool,
              required=False,
              help="""Adding this flag will force the volume access group to be deleted even though it has a Virtual Network ID or Tag. true: Volume access group will be deleted. false: Default. Do not delete the volume access group if it has a Virtual Network ID or Tag. """)
@pass_context
def delete(ctx,
           # Mandatory main parameter
           volumeaccessgroupid,
           # Optional main parameter
           deleteorphaninitiators = None,
           # Optional main parameter
           force = None):
    """DeleteVolumeAccessGroup enables you to delete a"""
    """volume access group."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    ctx.logger.info(""": """"""volumeaccessgroupid = """ + str(volumeaccessgroupid)+";" + """deleteorphaninitiators = """+str(deleteorphaninitiators)+";" + """force = """+str(force)+""";"""+"")
    try:
        _DeleteVolumeAccessGroupResult = ctx.element.delete_volume_access_group(volume_access_group_id=volumeaccessgroupid, delete_orphan_initiators=deleteorphaninitiators, force=force)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteVolumeAccessGroupResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteVolumeAccessGroupResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

