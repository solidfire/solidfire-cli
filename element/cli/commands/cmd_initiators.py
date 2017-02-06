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
    """modify create list delete """

@cli.command('modify', short_help="""ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators. If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible). """)
@click.option('--initiators',
              type=str,
              required=True,
              help="""Provide in json format: A list of Initiator objects containing characteristics of each initiator to modify. """)
@pass_context
def modify(ctx,
           initiators):
    """ModifyInitiators enables you to change the attributes of an existing initiator. You cannot change the name of an existing initiator. If you need to change the name of an initiator, delete the existing initiator with DeleteInitiators and create a new one with CreateInitiators."""
    """If ModifyInitiators fails to change one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(initiators is not None):
        try:
            kwargsDict = simplejson.loads(initiators)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
        try:
            initiators = [ModifyInitiator(**argsOfInterest) for argsOfInterest in kwargsDict]
        except:
            ctx.logger.error("""The format of the json you passed in did not match the required format of the special json. Either correct your format by referring to the README.md or use sfcli sfapi invoke if you'd rather directly interface with the json-rpc.""")
    

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        _ModifyInitiatorsResult = ctx.element.modify_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups. If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible). """)
@click.option('--initiators',
              type=str,
              required=True,
              help="""Provide in json format: A list of Initiator objects containing characteristics of each new initiator """)
@pass_context
def create(ctx,
           initiators):
    """CreateInitiators enables you to create multiple new initiator IQNs or World Wide Port Names (WWPNs) and optionally assign them aliases and attributes. When you use CreateInitiators to create new initiators, you can also add them to volume access groups."""
    """If CreateInitiators fails to create one of the initiators provided in the parameter, the method returns an error and does not create any initiators (no partial completion is possible)."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(initiators is not None):
        try:
            kwargsDict = simplejson.loads(initiators)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
        try:
            initiators = [CreateInitiator(**argsOfInterest) for argsOfInterest in kwargsDict]
        except:
            ctx.logger.error("""The format of the json you passed in did not match the required format of the special json. Either correct your format by referring to the README.md or use sfcli sfapi invoke if you'd rather directly interface with the json-rpc.""")
    

    ctx.logger.info("""initiators = """+str(initiators)+""";"""+"")
    try:
        _CreateInitiatorsResult = ctx.element.create_initiators(initiators=initiators)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListInitiators enables you to list initiator IQNs or World Wide Port Names (WWPNs). """)
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
              help="""A list of initiator IDs to retrieve. You can supply this parameter or the "startInitiatorID" parameter, but not both. """)
@pass_context
def list(ctx,
           startinitiatorid = None,
           limit = None,
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

    cli_utils.print_result(_ListInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups). If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible). """)
@click.option('--initiators',
              type=str,
              required=True,
              help="""An array of IDs of initiators to delete. """)
@pass_context
def delete(ctx,
           initiators):
    """DeleteInitiators enables you to delete one or more initiators from the system (and from any associated volumes or volume access groups)."""
    """If DeleteInitiators fails to delete one of the initiators provided in the parameter, the system returns an error and does not delete any initiators (no partial completion is possible)."""
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

    cli_utils.print_result(_DeleteInitiatorsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

