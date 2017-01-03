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
from uuid import UUID


@click.group()
@pass_context
def cli(ctx):
    """CreateBackupTarget GetBackupTarget ListBackupTargets ModifyBackupTarget RemoveBackupTarget """
    ctx.sfapi = ctx.client

@cli.command('CreateBackupTarget', short_help="CreateBackupTarget")
@click.option('--name',
              type=str,
              required=True,
              help="""Name for the backup target. """)
@click.option('--attributes',
              type=dict,
              required=False,
              help="""List of Name/Value pairs in JSON object format. """)
@pass_context
def CreateBackupTarget(ctx,
           name,
           attributes = None):
    """CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created."""



    CreateBackupTargetResult = ctx.element.create_backup_target(name=name, attributes=attributes)
    cli_utils.print_result(CreateBackupTargetResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetBackupTarget', short_help="GetBackupTarget")
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique identifier assigned to the backup target. """)
@pass_context
def GetBackupTarget(ctx,
           backup_target_id):
    """GetBackupTarget allows you to return information about a specific backup target that has been created."""



    GetBackupTargetResult = ctx.element.get_backup_target(backup_target_id=backup_target_id)
    cli_utils.print_result(GetBackupTargetResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ListBackupTargets', short_help="ListBackupTargets")
@pass_context
def ListBackupTargets(ctx):
    """You can use ListBackupTargets to retrieve information about all backup targets that have been created."""



    ListBackupTargetsResult = ctx.element.list_backup_targets()
    cli_utils.print_result(ListBackupTargetsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ModifyBackupTarget', short_help="ModifyBackupTarget")
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique identifier assigned to the backup target. """)
@click.option('--name',
              type=str,
              required=False,
              help="""Name for the backup target. """)
@click.option('--attributes',
              type=dict,
              required=False,
              help="""List of Name/Value pairs in JSON object format. """)
@pass_context
def ModifyBackupTarget(ctx,
           backup_target_id,
           name = None,
           attributes = None):
    """ModifyBackupTarget is used to change attributes of a backup target."""



    ModifyBackupTargetResult = ctx.element.modify_backup_target(backup_target_id=backup_target_id, name=name, attributes=attributes)
    cli_utils.print_result(ModifyBackupTargetResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('RemoveBackupTarget', short_help="RemoveBackupTarget")
@click.option('--backup_target_id',
              type=int,
              required=True,
              help="""Unique target ID of the target to remove. """)
@pass_context
def RemoveBackupTarget(ctx,
           backup_target_id):
    """RemoveBackupTarget allows you to delete backup targets."""



    RemoveBackupTargetResult = ctx.element.remove_backup_target(backup_target_id=backup_target_id)
    cli_utils.print_result(RemoveBackupTargetResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

