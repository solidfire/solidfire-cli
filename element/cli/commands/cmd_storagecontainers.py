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
<<<<<<< HEAD
    """modifystoragecontainer list getstoragecontainerefficiency createstoragecontainer delete """

@cli.command('modifystoragecontainer', short_help="""Modifies an existing storage container. """)
@click.option('--storagecontainerid',
              type=str,
              required=True,
              help="""""")
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""""")
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""""")
@pass_context
def modifystoragecontainer(ctx,
           storagecontainerid,
           initiatorsecret = None,
           targetsecret = None):
    """Modifies an existing storage container."""
=======
    """list delete createstoragecontainer getstoragecontainerefficiency modifystoragecontainer """

@cli.command('list', short_help="""Gets information for all storage containers currently in the system. """)
@click.option('--storagecontainerids',
              type=str,
              required=False,
              help="""List of storage containers to get """)
@pass_context
def list(ctx,
           storagecontainerids = None):
    """Gets information for all storage containers currently in the system."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    storagecontainerids = parser.parse_array(storagecontainerids)
    

<<<<<<< HEAD
    ctx.logger.info("""storagecontainerid = """+str(storagecontainerid)+""";"""+"""initiatorsecret = """+str(initiatorsecret)+""";"""+"""targetsecret = """+str(targetsecret)+""";"""+"")
    try:
        _ModifyStorageContainerResult = ctx.element.modify_storage_container(storage_container_id=storagecontainerid, initiator_secret=initiatorsecret, target_secret=targetsecret)
=======
    ctx.logger.info("""storagecontainerids = """+str(storagecontainerids)+""";"""+"")
    try:
        _ListStorageContainersResult = ctx.element.list_storage_containers(storage_container_ids=storagecontainerids)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_ModifyStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""Gets information for all storage containers currently in the system. """)
@click.option('--storagecontainerids',
              type=str,
              required=False,
              help="""List of storage containers to get """)
@pass_context
def list(ctx,
           storagecontainerids = None):
    """Gets information for all storage containers currently in the system."""
=======
    cli_utils.print_result(_ListStorageContainersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""Deletes a storage container from the system. """)
@click.option('--storagecontainerids',
              type=str,
              required=True,
              help="""list of storageContainerID of the storage container to delete. """)
@pass_context
def delete(ctx,
           storagecontainerids):
    """Deletes a storage container from the system."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    storagecontainerids = parser.parse_array(storagecontainerids)
    

    ctx.logger.info("""storagecontainerids = """+str(storagecontainerids)+""";"""+"")
    try:
<<<<<<< HEAD
        _ListStorageContainersResult = ctx.element.list_storage_containers(storage_container_ids=storagecontainerids)
=======
        _DeleteStorageContainerResult = ctx.element.delete_storage_containers(storage_container_ids=storagecontainerids)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_ListStorageContainersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstoragecontainerefficiency', short_help="""GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container. """)
@click.option('--storagecontainerid',
              type=str,
              required=True,
              help="""The ID of the storage container for which to retrieve efficiency information. """)
@pass_context
def getstoragecontainerefficiency(ctx,
           storagecontainerid):
    """GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container."""
=======
    cli_utils.print_result(_DeleteStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createstoragecontainer', short_help="""Creates a new VVols storage container. """)
@click.option('--name',
              type=str,
              required=True,
              help="""Name of the storage container. """)
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""The secret for CHAP authentication for the initiator """)
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""The secret for CHAP authentication for the target """)
@pass_context
def createstoragecontainer(ctx,
           name,
           initiatorsecret = None,
           targetsecret = None):
    """Creates a new VVols storage container."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

<<<<<<< HEAD
    ctx.logger.info("""storagecontainerid = """+str(storagecontainerid)+""";"""+"")
    try:
        _GetStorageContainerEfficiencyResult = ctx.element.get_storage_container_efficiency(storage_container_id=storagecontainerid)
=======
    ctx.logger.info("""name = """+str(name)+""";"""+"""initiatorsecret = """+str(initiatorsecret)+""";"""+"""targetsecret = """+str(targetsecret)+""";"""+"")
    try:
        _CreateStorageContainerResult = ctx.element.create_storage_container(name=name, initiator_secret=initiatorsecret, target_secret=targetsecret)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_GetStorageContainerEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('createstoragecontainer', short_help="""Creates a new VVols storage container. """)
@click.option('--name',
              type=str,
              required=True,
              help="""Name of the storage container. """)
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""The secret for CHAP authentication for the initiator """)
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""The secret for CHAP authentication for the target """)
@pass_context
def createstoragecontainer(ctx,
           name,
           initiatorsecret = None,
           targetsecret = None):
    """Creates a new VVols storage container."""
=======
    cli_utils.print_result(_CreateStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getstoragecontainerefficiency', short_help="""GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container. """)
@click.option('--storagecontainerid',
              type=str,
              required=True,
              help="""The ID of the storage container for which to retrieve efficiency information. """)
@pass_context
def getstoragecontainerefficiency(ctx,
           storagecontainerid):
    """GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

<<<<<<< HEAD
    ctx.logger.info("""name = """+str(name)+""";"""+"""initiatorsecret = """+str(initiatorsecret)+""";"""+"""targetsecret = """+str(targetsecret)+""";"""+"")
    try:
        _CreateStorageContainerResult = ctx.element.create_storage_container(name=name, initiator_secret=initiatorsecret, target_secret=targetsecret)
=======
    ctx.logger.info("""storagecontainerid = """+str(storagecontainerid)+""";"""+"")
    try:
        _GetStorageContainerEfficiencyResult = ctx.element.get_storage_container_efficiency(storage_container_id=storagecontainerid)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_CreateStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""Deletes a storage container from the system. """)
@click.option('--storagecontainerids',
              type=str,
              required=True,
              help="""list of storageContainerID of the storage container to delete. """)
@pass_context
def delete(ctx,
           storagecontainerids):
    """Deletes a storage container from the system."""
=======
    cli_utils.print_result(_GetStorageContainerEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('modifystoragecontainer', short_help="""Modifies an existing storage container. """)
@click.option('--storagecontainerid',
              type=str,
              required=True,
              help="""""")
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""""")
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""""")
@pass_context
def modifystoragecontainer(ctx,
           storagecontainerid,
           initiatorsecret = None,
           targetsecret = None):
    """Modifies an existing storage container."""
>>>>>>> Fixes the modifylunassignments bug
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()


    

    ctx.logger.info("""storagecontainerid = """+str(storagecontainerid)+""";"""+"""initiatorsecret = """+str(initiatorsecret)+""";"""+"""targetsecret = """+str(targetsecret)+""";"""+"")
    try:
<<<<<<< HEAD
        _DeleteStorageContainerResult = ctx.element.delete_storage_containers(storage_container_ids=storagecontainerids)
=======
        _ModifyStorageContainerResult = ctx.element.modify_storage_container(storage_container_id=storagecontainerid, initiator_secret=initiatorsecret, target_secret=targetsecret)
>>>>>>> Fixes the modifylunassignments bug
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(_DeleteStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(_ModifyStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Fixes the modifylunassignments bug

