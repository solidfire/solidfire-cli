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
    """getipmiinfo getipmiconfig """

@cli.command('getipmiinfo', short_help="""GetIpmiInfo enables you to display a detailed reporting of sensors (objects) for node fans, intake and exhaust temperatures, and power supplies that are monitored by the system. """, cls=SolidFireCommand)
@pass_context
def getipmiinfo(ctx):
    """GetIpmiInfo enables you to display a detailed reporting of sensors (objects) for node fans, intake and exhaust temperatures, and power supplies that are monitored by the system."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _GetIpmiInfoResult = ctx.element.get_ipmi_info()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetIpmiInfoResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetIpmiInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getipmiconfig', short_help="""GetIpmiConfig enables you to retrieve hardware sensor information from sensors that are in your node. """, cls=SolidFireCommand)
@click.option('--chassistype',
              type=str,
              required=False,
              help="""Displays information for each node chassis type. Valid values are: all: Returns sensor information for each chassis type. {chassis type}: Returns sensor information for a specified chassis type. """)
@pass_context
def getipmiconfig(ctx,
           # Optional main parameter
           chassistype = None):
    """GetIpmiConfig enables you to retrieve hardware sensor information from sensors that are in your node."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""chassistype = """+str(chassistype)+""";"""+"")
    try:
        _GetIpmiConfigResult = ctx.element.get_ipmi_config(chassis_type=chassistype)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_GetIpmiConfigResult), indent=4))
        return
    else:
        cli_utils.print_result(_GetIpmiConfigResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

