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
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import simplejson
from solidfire.models import *
from uuid import UUID
from element import exceptions


@click.group()
@pass_context
def cli(ctx):
    """Modify Create List Remove Get """

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
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    ModifyBackupTargetResult = ctx.element.modify_backup_target(backup_target_id=backup_target_id, name=name, attributes=attributes)
    cli_utils.print_result(ModifyBackupTargetResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



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
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(attributes is not None):
        kwargsDict = simplejson.loads(attributes)
        attributes = dict(**kwargsDict)

    CreateBackupTargetResult = ctx.element.create_backup_target(name=name, attributes=attributes)
    cli_utils.print_result(CreateBackupTargetResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""You can use ListBackupTargets to retrieve information about all backup targets that have been created. """)
@pass_context
def List(ctx):
    """You can use ListBackupTargets to retrieve information about all backup targets that have been created."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    ListBackupTargetsResult = ctx.element.list_backup_targets()
    cli_utils.print_result(ListBackupTargetsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Remove', short_help="""RemoveBackupTarget allows you to delete backup targets. """)
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique target ID of the target to remove. """)
@pass_context
def Remove(ctx,
           backup_target_id):
    """RemoveBackupTarget allows you to delete backup targets."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    RemoveBackupTargetResult = ctx.element.remove_backup_target(backup_target_id=backup_target_id)
    cli_utils.print_result(RemoveBackupTargetResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Get', short_help="""GetBackupTarget allows you to return information about a specific backup target that has been created. """)
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique identifier assigned to the backup target. """)
@pass_context
def Get(ctx,
           backup_target_id):
    """GetBackupTarget allows you to return information about a specific backup target that has been created."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")



    GetBackupTargetResult = ctx.element.get_backup_target(backup_target_id=backup_target_id)
    cli_utils.print_result(GetBackupTargetResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

