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
    """modify create list getefficiency delete """

@cli.command('modify', short_help="""ModifyStorageContainer enables you to make changes to an existing virtual volume storage container. """, cls=SolidFireCommand)
@click.option('--storagecontainerid',
              type=str,
              required=True,
              prompt=True,
              help="""The unique ID of the virtual volume storage container to modify. """)
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""The new secret for CHAP authentication for the initiator. """)
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""The new secret for CHAP authentication for the target. """)
@pass_context
def modify(ctx,
           # Mandatory main parameter
           storagecontainerid,
           # Optional main parameter
           initiatorsecret = None,
           # Optional main parameter
           targetsecret = None):
    """ModifyStorageContainer enables you to make changes to an existing virtual volume storage container."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    

    ctx.logger.info(""": """"""storagecontainerid = """ + str(storagecontainerid)+";" + """initiatorsecret = """+str(initiatorsecret)+";" + """targetsecret = """+str(targetsecret)+""";"""+"")
    try:
        _ModifyStorageContainerResult = ctx.element.modify_storage_container(storage_container_id=storagecontainerid, initiator_secret=initiatorsecret, target_secret=targetsecret)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ModifyStorageContainerResult), indent=4))
        return
    else:
        cli_utils.print_result(_ModifyStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('create', short_help="""CreateStorageContainer enables you to create a Virtual Volume (VVol) storage container. Storage containers are associated with a SolidFire storage system account, and are used for reporting and resource allocation. Storage containers can only be associated with virtual volumes. You need at least one storage container to use the Virtual Volumes feature. """, cls=SolidFireCommand)
@click.option('--name',
              type=str,
              required=True,
              prompt=True,
              help="""The name of the storage container. Follows SolidFire account naming restrictions. """)
@click.option('--initiatorsecret',
              type=str,
              required=False,
              help="""The secret for CHAP authentication for the initiator. """)
@click.option('--targetsecret',
              type=str,
              required=False,
              help="""The secret for CHAP authentication for the target. """)
@click.option('--accountid',
              type=int,
              required=False,
              help="""Non-storage container account that will become a storage container. """)
@pass_context
def create(ctx,
           # Mandatory main parameter
           name,
           # Optional main parameter
           initiatorsecret = None,
           # Optional main parameter
           targetsecret = None,
           # Optional main parameter
           accountid = None):
    """CreateStorageContainer enables you to create a Virtual Volume (VVol) storage container. Storage containers are associated with a SolidFire storage system account, and are used for reporting and resource allocation. Storage containers can only be associated with virtual volumes. You need at least one storage container to use the Virtual Volumes feature."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    

    ctx.logger.info(""": """"""name = """ + str(name)+";" + """initiatorsecret = """+str(initiatorsecret)+";" + """targetsecret = """+str(targetsecret)+";" + """accountid = """+str(accountid)+""";"""+"")
    try:
        _CreateStorageContainerResult = ctx.element.create_storage_container(name=name, initiator_secret=initiatorsecret, target_secret=targetsecret, account_id=accountid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_CreateStorageContainerResult), indent=4))
        return
    else:
        cli_utils.print_result(_CreateStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('list', short_help="""ListStorageContainers enables you to retrieve information about all virtual volume storage containers known to the system. """, cls=SolidFireCommand)
@click.option('--storagecontainerids',
              type=str,
              required=False,
              help="""A list of storage container IDs for which to retrieve information. If you omit this parameter, the method returns information about all storage containers in the system. """)
@pass_context
def list(ctx,
           # Optional main parameter
           storagecontainerids = None):
    """ListStorageContainers enables you to retrieve information about all virtual volume storage containers known to the system."""

    

    cli_utils.establish_connection(ctx)
    

    storagecontainerids = parser.parse_array(storagecontainerids)
    

    ctx.logger.info(""": """"""storagecontainerids = """+str(storagecontainerids)+""";"""+"")
    try:
        _ListStorageContainersResult = ctx.element.list_storage_containers(storage_container_ids=storagecontainerids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListStorageContainersResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListStorageContainersResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getefficiency', short_help="""GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container. """, cls=SolidFireCommand)
@click.option('--storagecontainerid',
              type=str,
              required=True,
              prompt=True,
              help="""The ID of the storage container for which to retrieve efficiency information. """)
@pass_context
def getefficiency(ctx,
           # Mandatory main parameter
           storagecontainerid):
    """GetStorageContainerEfficiency enables you to retrieve efficiency information about a virtual volume storage container."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""storagecontainerid = """ + str(storagecontainerid)+""";"""+"")
    try:
        _GetStorageContainerEfficiencyResult = ctx.element.get_storage_container_efficiency(storage_container_id=storagecontainerid)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetStorageContainerEfficiencyResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetStorageContainerEfficiencyResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('delete', short_help="""DeleteStorageContainers enables you to remove up to 2000 Virtual Volume (VVol) storage containers from the system at one time. The storage containers you remove must not contain any VVols. """, cls=SolidFireCommand)
@click.option('--storagecontainerids',
              type=str,
              required=True,
              prompt=True,
              help="""A list of IDs of the storage containers to delete. You can specify up to 2000 IDs in the list. """)
@pass_context
def delete(ctx,
           # Mandatory main parameter
           storagecontainerids):
    """DeleteStorageContainers enables you to remove up to 2000 Virtual Volume (VVol) storage containers from the system at one time."""
    """The storage containers you remove must not contain any VVols."""

    

    cli_utils.establish_connection(ctx)
    

    storagecontainerids = parser.parse_array(storagecontainerids)
    

    ctx.logger.info(""": """"""storagecontainerids = """ + str(storagecontainerids)+""";"""+"")
    try:
        _DeleteStorageContainerResult = ctx.element.delete_storage_containers(storage_container_ids=storagecontainerids)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DeleteStorageContainerResult), indent=4))
        return
    else:
        cli_utils.print_result(_DeleteStorageContainerResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

