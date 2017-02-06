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
    """modify create list remove get """

@cli.command('modify', short_help="""ModifyBackupTarget is used to change attributes of a backup target. """)
@click.option('--backuptargetid',
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
def modify(ctx,
           backuptargetid,
           name = None,
           attributes = None):
    """ModifyBackupTarget is used to change attributes of a backup target."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
        try:
            attributes = dict(**kwargsDict)
        except:
            ctx.logger.error("""The format of the json you passed in did not match the required format of the special json. Either correct your format by referring to the README.md or use sfcli sfapi invoke if you'd rather directly interface with the json-rpc.""")
    

    ctx.logger.info("""backuptargetid = """+str(backuptargetid)+""";"""+"""name = """+str(name)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _ModifyBackupTargetResult = ctx.element.modify_backup_target(backup_target_id=backuptargetid, name=name, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created. """)
@click.option('--name',
              type=str,
              required=True,
              help="""Name for the backup target. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""Provide in json format: List of Name/Value pairs in JSON object format. """)
@pass_context
def create(ctx,
           name,
           attributes = None):
    """CreateBackupTarget allows you to create and store backup target information so that you do not need to re-enter it each time a backup is created."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    if(attributes is not None):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
        try:
            attributes = dict(**kwargsDict)
        except:
            ctx.logger.error("""The format of the json you passed in did not match the required format of the special json. Either correct your format by referring to the README.md or use sfcli sfapi invoke if you'd rather directly interface with the json-rpc.""")
    

    ctx.logger.info("""name = """+str(name)+""";"""+"""attributes = """+str(attributes)+""";"""+"")
    try:
        _CreateBackupTargetResult = ctx.element.create_backup_target(name=name, attributes=attributes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""You can use ListBackupTargets to retrieve information about all backup targets that have been created. """)
@pass_context
def list(ctx):
    """You can use ListBackupTargets to retrieve information about all backup targets that have been created."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("")
    try:
        _ListBackupTargetsResult = ctx.element.list_backup_targets()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListBackupTargetsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""RemoveBackupTarget allows you to delete backup targets. """)
@click.option('--backuptargetid',
              type=int,
              required=True,
              help="""Unique target ID of the target to remove. """)
@pass_context
def remove(ctx,
           backuptargetid):
    """RemoveBackupTarget allows you to delete backup targets."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""backuptargetid = """+str(backuptargetid)+""";"""+"")
    try:
        _RemoveBackupTargetResult = ctx.element.remove_backup_target(backup_target_id=backuptargetid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_RemoveBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('get', short_help="""GetBackupTarget allows you to return information about a specific backup target that has been created. """)
@click.option('--backuptargetid',
              type=int,
              required=True,
              help="""Unique identifier assigned to the backup target. """)
@pass_context
def get(ctx,
           backuptargetid):
    """GetBackupTarget allows you to return information about a specific backup target that has been created."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""backuptargetid = """+str(backuptargetid)+""";"""+"")
    try:
        _GetBackupTargetResult = ctx.element.get_backup_target(backup_target_id=backuptargetid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

