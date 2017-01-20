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
    """Create List Delete Modify """

@cli.command('Create', short_help="""CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups. If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible). """)
@click.option('--create_initiator_name',
              type=str,
              required=True,
              help="""(Required) The name of the initiator (IQN or WWPN) to create. (String) """)
@click.option('--create_initiator_alias',
              type=str,
              required=False,
              help="""(Optional) The friendly name to assign to this initiator. (String) """)
@click.option('--create_initiator_volume_access_group_id',
              type=int,
              required=False,
              help="""(Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer) """)
@click.option('--create_initiator_attributes',
              type=dict,
              required=False,
              help="""(Optional) A set of JSON attributes assigned to this initiator. (JSON Object) """)
@pass_context
def Create(ctx,
           create_initiator_name,
           create_initiator_alias = None,
           create_initiator_volume_access_group_id = None,
           create_initiator_attributes = None):
    """CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups."""
    """If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = None
    if(initiators is not None or False):
        kwargsDict = dict()
        kwargsDict["name"] = create_initiator_name
        kwargsDict["alias"] = create_initiator_alias
        kwargsDict["volume_access_group_id"] = create_initiator_volume_access_group_id
        kwargsDict["attributes"] = create_initiator_attributes

        initiators = CreateInitiator(**kwargsDict)

    initiators = parser.parse_array(initiators)

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        CreateInitiatorsResult = ctx.element.create_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(CreateInitiatorsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs). """)
@click.option('--start_initiator_id',
              type=int,
              required=False,
              help="""The initiator ID at which to begin the listing. You can supply this parameter or the "initiators" parameter, but not both. """)
@click.option('--limit',
              type=int,
              required=False,
              help="""The maximum number of initiator objects to return. """)
@click.option('--initiators',
              type=str,
              required=False,
              help="""A list of initiator IDs to retrieve. You can supply this parameter or the "startInitiatorID" parameter, but not both. """)
@pass_context
def List(ctx,
           start_initiator_id = None,
           limit = None,
           initiators = None):
    """ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = parser.parse_array(initiators)

    ctx.logger.info("""start_initiator_id = """+str(start_initiator_id)+""";"""+"""limit = """+str(limit)+""";"""+"""initiators = """+str(initiators)+""";"""+"")
    try:
        ListInitiatorsResult = ctx.element.list_initiators(start_initiator_id=start_initiator_id, limit=limit, initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListInitiatorsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Delete', short_help="""DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups). If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible). """)
@click.option('--initiators',
              type=str,
              required=True,
              help="""An array of IDs of initiators to delete. """)
@pass_context
def Delete(ctx,
           initiators):
    """DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups)."""
    """If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = parser.parse_array(initiators)

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        DeleteInitiatorsResult = ctx.element.delete_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(DeleteInitiatorsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Modify', short_help="""ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators. If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible). """)
@click.option('--modify_initiator_initiator_id',
              type=int,
              required=True,
              help="""(Required) The numeric ID of the initiator to modify. (Integer) """)
@click.option('--modify_initiator_alias',
              type=str,
              required=False,
              help="""(Optional) A new friendly name to assign to the initiator. (String) """)
@click.option('--modify_initiator_volume_access_group_id',
              type=int,
              required=False,
              help="""(Optional) The ID of the volume access group into to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) """)
@click.option('--modify_initiator_attributes',
              type=dict,
              required=False,
              help="""(Optional) A new set of JSON attributes assigned to this initiator. (JSON Object) """)
@pass_context
def Modify(ctx,
           modify_initiator_initiator_id,
           modify_initiator_alias = None,
           modify_initiator_volume_access_group_id = None,
           modify_initiator_attributes = None):
    """ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators."""
    """If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    initiators = None
    if(initiators is not None or False):
        kwargsDict = dict()
        kwargsDict["initiator_id"] = modify_initiator_initiator_id
        kwargsDict["alias"] = modify_initiator_alias
        kwargsDict["volume_access_group_id"] = modify_initiator_volume_access_group_id
        kwargsDict["attributes"] = modify_initiator_attributes

        initiators = ModifyInitiator(**kwargsDict)

    initiators = parser.parse_array(initiators)

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        ModifyInitiatorsResult = ctx.element.modify_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ModifyInitiatorsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

