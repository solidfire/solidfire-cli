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
    """modify create list delete """

@cli.command('modify', short_help="""ModifyInitiators enables you to change the attributes of one or more existing initiators. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete it first with DeleteInitiators and create a new one with CreateInitiators. If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not modify any initiators (no partial completion is possible). """, cls=SolidFireCommand)
@click.option('--initiators',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["initiatorid", "alias", "volumeaccessgroupid", "attributes", ],
              required=True,
              help="""A list of objects containing characteristics of each initiator to modify. Values are: initiatorID: (Required) The ID of the initiator to modify. (Integer) alias: (Optional) A new friendly name to assign to the initiator. (String) attributes: (Optional) A new set of JSON attributes to assign to the initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which the initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer)  Has the following subparameters: --initiatorid --alias --volumeaccessgroupid --attributes """)
@click.option('--initiatorid',
              required=True,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] (Required) The numeric ID of the initiator to modify. (Integer) """,
              cls=SolidFireOption)
@click.option('--alias',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] (Optional) A new friendly name to assign to the initiator. (String) """,
              cls=SolidFireOption)
@click.option('--volumeaccessgroupid',
              required=False,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] (Optional) The ID of the volume access group to which the newly created initiator should be added. If the initiator was previously in a different volume access group, it is removed from the old volume access group. If this key is present but null, the initiator is removed from its current volume access group, but not placed in any new volume access group. (Integer) """,
              cls=SolidFireOption)
@click.option('--attributes',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] (Optional) A new set of JSON attributes assigned to this initiator. (JSON Object) """,
              cls=SolidFireOption)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           initiators,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           initiatorid,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           alias = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           volumeaccessgroupid = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           attributes = None):
    """ModifyInitiators enables you to change the attributes of one or more existing initiators. You cannot change the name of an existing"""
    """initiator. If you need to change the name of an initiator, delete it first with DeleteInitiators and create a new one with"""
    """CreateInitiators."""
    """If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not modify"""
    """any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    initiatorsArray = []
    if(initiators is not None):
        try:
            for i, _initiators in enumerate(initiators):
                attributes_json = None
                if attributes[i] != None:
                    attributes_json = simplejson.loads(attributes[i])
                initiatorsArray.append(ModifyInitiator(initiator_id=initiatorid[i], alias=alias[i], volume_access_group_id=volumeaccessgroupid[i], attributes=attributes_json, ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        _ModifyInitiatorsResult = ctx.element.modify_initiators(initiators=initiatorsArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyInitiatorsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups. If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible). """, cls=SolidFireCommand)
@click.option('--initiators',
              cls=SolidFireOption,
              is_flag=True,
              multiple=True,
              subparameters=["name", "alias", "volumeaccessgroupid", "attributes", ],
              required=True,
              help="""A list of objects containing characteristics of each new initiator. Values are: name: (Required) The name of the initiator (IQN or WWPN) to create. (String) alias: (Optional) The friendly name to assign to this initiator. (String) attributes: (Optional) A set of JSON attributes to assign to this initiator. (JSON Object) volumeAccessGroupID: (Optional) The ID of the volume access group into to which this newly created initiator will be added. (Integer)  Has the following subparameters: --name --alias --volumeaccessgroupid --attributes """)
@click.option('--name',
              required=True,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] (Required) The name of the initiator (IQN or WWPN) to create. (String) """,
              cls=SolidFireOption)
@click.option('--alias',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] (Optional) The friendly name to assign to this initiator. (String) """,
              cls=SolidFireOption)
@click.option('--volumeaccessgroupid',
              required=False,
              multiple=True,
              type=int,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] (Optional) The ID of the volume access group to which this newly created initiator will be added. (Integer) """,
              cls=SolidFireOption)
@click.option('--attributes',
              required=False,
              multiple=True,
              type=str,
              default=None,
              is_sub_parameter=True,
              help="""[subparameter] (Optional) A set of JSON attributes assigned to this initiator. (JSON Object) """,
              cls=SolidFireOption)
@pass_context
def create(ctx,
           # Mandatory main parameter
           initiators,
           # Mandatory subparameter of a mandatory main parameter (Not fully decomposed)
           name,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           alias = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           volumeaccessgroupid = None,
           # Non mandatory subparameter of a mandatory main parameter (not fully decomposed)
           attributes = None):
    """CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them"""
    """aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups."""
    """If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create"""
    """any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    initiatorsArray = []
    if(initiators is not None):
        try:
            for i, _initiators in enumerate(initiators):
                attributes_json = None
                if attributes[i] != None:
                    attributes_json = simplejson.loads(attributes[i])
                initiatorsArray.append(CreateInitiator(name=name[i], alias=alias[i], volume_access_group_id=volumeaccessgroupid[i], attributes=attributes_json, ))
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        _CreateInitiatorsResult = ctx.element.create_initiators(initiators=initiatorsArray)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateInitiatorsResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs). """, cls=SolidFireCommand)
@click.option('--startinitiatorid',
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
              help="""A list of initiator IDs to retrieve. You can provide a value for this parameter or the "startInitiatorID" parameter, but not both. """)
@pass_context
def list(ctx,
           # Optional main parameter
           startinitiatorid = None,
           # Optional main parameter
           limit = None,
           # Optional main parameter
           initiators = None):
    """ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

            

    initiators = parser.parse_array(initiators)
    

    ctx.logger.info("""startinitiatorid = """+str(startinitiatorid)+""";"""+"""limit = """+str(limit)+""";"""+"""initiators = """+str(initiators)+""";"""+"")
    try:
        _ListInitiatorsResult = ctx.element.list_initiators(start_initiator_id=startinitiatorid, limit=limit, initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListInitiatorsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups). If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible). """, cls=SolidFireCommand)
@click.option('--initiators',
              type=str,
              required=True,
              help="""An array of IDs of initiators to delete. """)
@pass_context
def delete(ctx,
           # Mandatory main parameter
           initiators):
    """DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access"""
    """groups)."""
    """If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any"""
    """initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()

    

    initiators = parser.parse_array(initiators)
    

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        _DeleteInitiatorsResult = ctx.element.delete_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteInitiatorsResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

