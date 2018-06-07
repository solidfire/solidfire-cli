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
    """getsshinfo getclustersshinfo disableclusterssh enableclusterssh enablessh disablessh """

@cli.command('getsshinfo', short_help="""Returns SSH status for the targeted node. """, cls=SolidFireCommand)
@pass_context
def getsshinfo(ctx):
    """Returns SSH status for the targeted node."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetSshInfoResult = ctx.element.get_ssh_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetSshInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetSshInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getclustersshinfo', short_help="""Returns SSH status for the cluster. """, cls=SolidFireCommand)
@pass_context
def getclustersshinfo(ctx):
    """Returns SSH status for the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetClusterSshInfoResult = ctx.element.get_cluster_ssh_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetClusterSshInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetClusterSshInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('disableclusterssh', short_help="""Disables SSH on all nodes in the cluster. """, cls=SolidFireCommand)
@pass_context
def disableclusterssh(ctx):
    """Disables SSH on all nodes in the cluster."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _DisableClusterSshResult = ctx.element.disable_cluster_ssh()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DisableClusterSshResult), indent=4))
        return
    else:
        cli_utils.print_result(_DisableClusterSshResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enableclusterssh', short_help="""Enables SSH on all nodes in the cluster. Overwrites previous duration. """, cls=SolidFireCommand)
@click.option('--duration',
              type=str,
              required=True,
              prompt=True,
              help="""The duration on how long SSH will be enable on the cluster. Follows format "HH:MM:SS.MS". """)
@pass_context
def enableclusterssh(ctx,
           # Mandatory main parameter
           duration):
    """Enables SSH on all nodes in the cluster."""
    """Overwrites previous duration."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""duration = """ + str(duration)+""";"""+"")
    try:
        _EnableClusterSshResult = ctx.element.enable_cluster_ssh(duration=duration)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_EnableClusterSshResult), indent=4))
        return
    else:
        cli_utils.print_result(_EnableClusterSshResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('enablessh', short_help="""Enables SSH on the targeted node. This does not effect the cluster-wide SSH timeout duration. The node is not exempt from the SSH shut off by the global timeout. """, cls=SolidFireCommand)
@pass_context
def enablessh(ctx):
    """Enables SSH on the targeted node."""
    """This does not effect the cluster-wide SSH timeout duration."""
    """The node is not exempt from the SSH shut off by the global timeout."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _EnableSshResult = ctx.element.enable_ssh()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_EnableSshResult), indent=4))
        return
    else:
        cli_utils.print_result(_EnableSshResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('disablessh', short_help="""Disables SSH on the targeted node. This does not effect the cluster-wide SSH timeout duration. The node is not exempt from the SSH shut off by the global timeout. """, cls=SolidFireCommand)
@pass_context
def disablessh(ctx):
    """Disables SSH on the targeted node."""
    """This does not effect the cluster-wide SSH timeout duration."""
    """The node is not exempt from the SSH shut off by the global timeout."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _DisableSshResult = ctx.element.disable_ssh()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_DisableSshResult), indent=4))
        return
    else:
        cli_utils.print_result(_DisableSshResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

