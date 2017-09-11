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
    """modify create list remove get """

@cli.command('modify', short_help="""ModifyBackupTarget enables you to change attributes of a backup target. """, cls=SolidFireCommand)
@click.option('--backuptargetid',
              type=int,
              required=True,
              prompt=True,
              help="""The unique target ID for the target to modify. """)
@click.option('--name',
              type=str,
              required=False,
              help="""The new name for the backup target. """)
@click.option('--attributes',
              type=str,
              required=False,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           backuptargetid,
           # Optional main parameter
           name = None,
           # Optional main parameter
           attributes = None):
    """ModifyBackupTarget enables you to change attributes of a backup target."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""backuptargetid = """ + str(backuptargetid)+";" + """name = """+str(name)+";" + """attributes = """+str(kwargsDict)+""";"""+"")
    try:
        _ModifyBackupTargetResult = ctx.element.modify_backup_target(backup_target_id=backuptargetid, name=name, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyBackupTargetResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateBackupTarget enables you to create and store backup target information so that you do not need to re-enter it each time a backup is created. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the backup target. """)
@click.option('--attributes',
              type=str,
              required=True,
              help="""List of name-value pairs in JSON object format.  Has the following subparameters: """)
@pass_context
def create(ctx,
           # Mandatory main parameter
           name,
           # Mandatory main parameter
           attributes):
    """CreateBackupTarget enables you to create and store backup target information so that you do not need to re-enter it each time a backup is created."""

    

    cli_utils.establish_connection(ctx)
    
    

    kwargsDict = None
    if(attributes is not None and attributes != ()):
        try:
            kwargsDict = simplejson.loads(attributes)
        except Exception as e:
            ctx.logger.error(e.__str__())
            exit(1)
    

    ctx.logger.info(""": """"""name = """ + str(name)+";"+"""attributes = """ + str(kwargsDict)+""";"""+"")
    try:
        _CreateBackupTargetResult = ctx.element.create_backup_target(name=name, attributes=kwargsDict)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateBackupTargetResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""You can use ListBackupTargets to retrieve information about all backup targets that have been created. """, cls=SolidFireCommand)
@pass_context
def list(ctx):
    """You can use ListBackupTargets to retrieve information about all backup targets that have been created."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListBackupTargetsResult = ctx.element.list_backup_targets()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListBackupTargetsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListBackupTargetsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('remove', short_help="""RemoveBackupTarget allows you to delete backup targets. """, cls=SolidFireCommand)
@click.option('--backuptargetid',
              type=int,
              required=True,
              prompt=True,
              help="""The unique target ID of the target to remove. """)
@pass_context
def remove(ctx,
           # Mandatory main parameter
           backuptargetid):
    """RemoveBackupTarget allows you to delete backup targets."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""backuptargetid = """ + str(backuptargetid)+""";"""+"")
    try:
        _RemoveBackupTargetResult = ctx.element.remove_backup_target(backup_target_id=backuptargetid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_RemoveBackupTargetResult), indent=4))
        return
    else:
        cli_utils.print_result(_RemoveBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('get', short_help="""GetBackupTarget enables you to return information about a specific backup target that you have created. """, cls=SolidFireCommand)
@click.option('--backuptargetid',
              type=int,
              required=True,
              prompt=True,
              help="""The unique identifier assigned to the backup target. """)
@pass_context
def get(ctx,
           # Mandatory main parameter
           backuptargetid):
    """GetBackupTarget enables you to return information about a specific backup target that you have created."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""backuptargetid = """ + str(backuptargetid)+""";"""+"")
    try:
        _GetBackupTargetResult = ctx.element.get_backup_target(backup_target_id=backuptargetid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetBackupTargetResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetBackupTargetResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

