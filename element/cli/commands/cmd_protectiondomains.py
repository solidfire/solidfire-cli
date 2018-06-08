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
    """listprotectiondomainlevels """

@cli.command('listprotectiondomainlevels', short_help="""ListProtectionDomainLevels returns the Tolerance and Resiliencty of the cluster from the perspective of each of the supported ProtectionDomainTypes. """, cls=SolidFireCommand)
@pass_context
def listprotectiondomainlevels(ctx):
    """ListProtectionDomainLevels returns the Tolerance and Resiliencty of the cluster from the perspective of each of the supported ProtectionDomainTypes."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListProtectionDomainLevelsResult = ctx.element.list_protection_domain_levels()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListProtectionDomainLevelsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListProtectionDomainLevelsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

