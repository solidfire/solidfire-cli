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
    """Modify Create List Remove Get """

@cli.command('Modify', short_help="""ModifyBackupTarget is used to change attributes of a backup target. """)
=======
    """Get Remove Modify Create List """

@cli.command('Get', short_help="""GetBackupTarget allows you to return information about a specific backup target that has been created. """)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique identifier assigned to the backup target. """)
<<<<<<< HEAD
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the backup target. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Modify(ctx,
           backup_target_id,
           name = None,
           attributes = None):
    """ModifyBackupTarget is used to change attributes of a backup target."""
=======
@pass_context
def Get(ctx,
           backup_target_id):
    """GetBackupTarget allows you to return information about a specific backup target that has been created."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
    ctx.logger.info("""backup_target_id = """+str(backup_target_id)+""";"""+"""name = """+str(name)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        ModifyBackupTargetResult = ctx.element.modify_backup_target(backup_target_id=backup_target_id, name=name, attributes=attributes)
=======
    ctx.logger.info("""backup_target_id = """+str(backup_target_id)+""";"""+"")
    try:
        GetBackupTargetResult = ctx.element.get_backup_target(backup_target_id=backup_target_id)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(ModifyBackupTargetResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Create', short_help="""CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created. """)
@click.option('--name',
              type=str,
              required=True,
              help="""Name for the backup target. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Create(ctx,
           name,
           attributes = None):
    """CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created."""
=======
    cli_utils.print_result(GetBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Remove', short_help="""RemoveBackupTarget allows you to delete backup targets. """)
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique target ID of the target to remove. """)
@pass_context
def Remove(ctx,
           backup_target_id):
    """RemoveBackupTarget allows you to delete backup targets."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

<<<<<<< HEAD
    ctx.logger.info("""name = """+str(name)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        CreateBackupTargetResult = ctx.element.create_backup_target(name=name, attributes=attributes)
=======
    ctx.logger.info("""backup_target_id = """+str(backup_target_id)+""";"""+"")
    try:
        RemoveBackupTargetResult = ctx.element.remove_backup_target(backup_target_id=backup_target_id)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(CreateBackupTargetResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""You can use ListBackupTargets to retrieve information about all backup targets that have been created. """)
@pass_context
def List(ctx):
    """You can use ListBackupTargets to retrieve information about all backup targets that have been created."""
=======
    cli_utils.print_result(RemoveBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Modify', short_help="""ModifyBackupTarget is used to change attributes of a backup target. """)
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique identifier assigned to the backup target. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the backup target. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Modify(ctx,
           backup_target_id,
           name = None,
           attributes = None):
    """ModifyBackupTarget is used to change attributes of a backup target."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

<<<<<<< HEAD
    ctx.logger.info("")
    try:
        ListBackupTargetsResult = ctx.element.list_backup_targets()
=======
    ctx.logger.info("""backup_target_id = """+str(backup_target_id)+""";"""+"""name = """+str(name)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        ModifyBackupTargetResult = ctx.element.modify_backup_target(backup_target_id=backup_target_id, name=name, attributes=attributes)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(ListBackupTargetsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Remove', short_help="""RemoveBackupTarget allows you to delete backup targets. """)
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique target ID of the target to remove. """)
@pass_context
def Remove(ctx,
           backup_target_id):
    """RemoveBackupTarget allows you to delete backup targets."""
=======
    cli_utils.print_result(ModifyBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Create', short_help="""CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created. """)
@click.option('--name',
              type=str,
              required=True,
              help="""Name for the backup target. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def Create(ctx,
           name,
           attributes = None):
    """CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
    ctx.logger.info("""backup_target_id = """+str(backup_target_id)+""";"""+"")
    try:
        RemoveBackupTargetResult = ctx.element.remove_backup_target(backup_target_id=backup_target_id)
=======
    ctx.logger.info("""name = """+str(name)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        CreateBackupTargetResult = ctx.element.create_backup_target(name=name, attributes=attributes)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(RemoveBackupTargetResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Get', short_help="""GetBackupTarget allows you to return information about a specific backup target that has been created. """)
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique identifier assigned to the backup target. """)
@pass_context
def Get(ctx,
           backup_target_id):
    """GetBackupTarget allows you to return information about a specific backup target that has been created."""
=======
    cli_utils.print_result(CreateBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""You can use ListBackupTargets to retrieve information about all backup targets that have been created. """)
@pass_context
def List(ctx):
    """You can use ListBackupTargets to retrieve information about all backup targets that have been created."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
<<<<<<< HEAD
        GetBackupTargetResult = ctx.element.get_backup_target(backup_target_id=backup_target_id)
=======
        ListBackupTargetsResult = ctx.element.list_backup_targets()
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(GetBackupTargetResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(ListBackupTargetsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.

