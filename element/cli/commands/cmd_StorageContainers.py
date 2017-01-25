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
    """List CreateStorageContainer GetStorageContainerEfficiency Delete ModifyStorageContainer """

@cli.command('List', short_help="""Gets information for all storage containers currently in the system. """)
@click.option('--storage_container_ids',
              type=str,
              required=False,
              help="""List of storage containers to get """)
@pass_context
def List(ctx,
           storage_container_ids = None):
    """Gets information for all storage containers currently in the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    storage_container_ids = parser.parse_array(storage_container_ids)

    ctx.logger.info("""storage_container_ids = """+str(storage_container_ids)+""";"""+"")
    try:
        _ListStorageContainersResult = ctx.element.list_storage_containers(storage_container_ids=storage_container_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ListStorageContainersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('CreateStorageContainer', short_help="""Creates a new VVols storage container. """)
@click.option('--name',
              type=str,
              required=True,
              help="""Name of the storage container. """)
@click.option('--initiator_secret',
              type=str,
              required=False,
              help="""The secret for CHAP authentication for the initiator """)
@click.option('--target_secret',
              type=str,
              required=False,
              help="""The secret for CHAP authentication for the target """)
@pass_context
def CreateStorageContainer(ctx,
           name,
           initiator_secret = None,
           target_secret = None):
    """Creates a new VVols storage container."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""name = """+str(name)+""";"""+"""initiator_secret = """+str(initiator_secret)+""";"""+"""target_secret = """+str(target_secret)+""";"""+"")
    try:
        _CreateStorageContainerResult = ctx.element.create_storage_container(name=name, initiator_secret=initiator_secret, target_secret=target_secret)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_CreateStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('GetStorageContainerEfficiency', short_help="""GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container. """)
@click.option('--storage_container_id',
              type=str,
              required=True,
              help="""The ID of the storage container for which to retrieve efficiency information. """)
@pass_context
def GetStorageContainerEfficiency(ctx,
           storage_container_id):
    """GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""storage_container_id = """+str(storage_container_id)+""";"""+"")
    try:
        _GetStorageContainerEfficiencyResult = ctx.element.get_storage_container_efficiency(storage_container_id=storage_container_id)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_GetStorageContainerEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Delete', short_help="""Deletes a storage container from the system. """)
@click.option('--storage_container_ids',
              type=str,
              required=True,
              help="""list of storageContainerID of the storage container to delete. """)
@pass_context
def Delete(ctx,
           storage_container_ids):
    """Deletes a storage container from the system."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    storage_container_ids = parser.parse_array(storage_container_ids)

    ctx.logger.info("""storage_container_ids = """+str(storage_container_ids)+""";"""+"")
    try:
        _DeleteStorageContainerResult = ctx.element.delete_storage_containers(storage_container_ids=storage_container_ids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_DeleteStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ModifyStorageContainer', short_help="""Modifies an existing storage container. """)
@click.option('--storage_container_id',
              type=str,
              required=True,
              help="""""")
@click.option('--initiator_secret',
              type=str,
              required=False,
              help="""""")
@click.option('--target_secret',
              type=str,
              required=False,
              help="""""")
@pass_context
def ModifyStorageContainer(ctx,
           storage_container_id,
           initiator_secret = None,
           target_secret = None):
    """Modifies an existing storage container."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""storage_container_id = """+str(storage_container_id)+""";"""+"""initiator_secret = """+str(initiator_secret)+""";"""+"""target_secret = """+str(target_secret)+""";"""+"")
    try:
        _ModifyStorageContainerResult = ctx.element.modify_storage_container(storage_container_id=storage_container_id, initiator_secret=initiator_secret, target_secret=target_secret)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(_ModifyStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

