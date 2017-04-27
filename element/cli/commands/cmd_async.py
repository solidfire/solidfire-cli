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
    """listresults getresult """

@cli.command('listresults', short_help="""You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system. Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult to query any of the asyncHandles returned by ListAsyncResults. """, cls=SolidFireCommand)
@click.option('--asyncresulttypes',
              type=str,
              required=False,
              help="""An optional list of types of results. You can use this list to restrict the results to only these types of operations. Possible values are: BulkVolume: Copy operations between volumes, such as backups or restores. Clone: Volume cloning operations. DriveRemoval: Operations involving the system copying data from a drive in preparation to remove it from the cluster. RtfiPendingNode: Operations involving the system installing compatible software on a node before adding it to the cluster """)
@pass_context
def listresults(ctx,
           # Optional main parameter
           asyncresulttypes = None):
    """You can use ListAsyncResults to list the results of all currently running and completed asynchronous methods on the system."""
    """Querying asynchronous results with ListAsyncResults does not cause completed asyncHandles to expire; you can use GetAsyncResult"""
    """to query any of the asyncHandles returned by ListAsyncResults."""

    

    cli_utils.establish_connection(ctx)
    

    asyncresulttypes = parser.parse_array(asyncresulttypes)
    

    ctx.logger.info(""": """"""asyncresulttypes = """+str(asyncresulttypes)+""";"""+"")
    try:
        _ListAsyncResultsResult = ctx.element.list_async_results(async_result_types=asyncresulttypes)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListAsyncResultsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListAsyncResultsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('getresult', short_help="""You can use GetAsyncResult to retrieve the result of asynchronous method calls. Some method calls require some time to run, and might not be finished when the system sends the initial response. To obtain the status or result of the method call, use GetAsyncResult to poll the asyncHandle value returned by the method. GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual data returned for the operation depends on the original method call and the return data is documented with each method. """, cls=SolidFireCommand)
@click.option('--asynchandle',
              type=int,
              required=True,
              prompt=True,
              help="""A value that was returned from the original asynchronous method call. """)
@click.option('--keepresult',
              type=bool,
              required=False,
              help="""If true, GetAsyncResult does not remove the asynchronous result upon returning it, enabling future queries to that asyncHandle. """)
@pass_context
def getresult(ctx,
           # Mandatory main parameter
           asynchandle,
           # Optional main parameter
           keepresult = None):
    """You can use GetAsyncResult to retrieve the result of asynchronous method calls. Some method calls require some time to run, and"""
    """might not be finished when the system sends the initial response. To obtain the status or result of the method call, use"""
    """GetAsyncResult to poll the asyncHandle value returned by the method."""
    """GetAsyncResult returns the overall status of the operation (in progress, completed, or error) in a standard fashion, but the actual"""
    """data returned for the operation depends on the original method call and the return data is documented with each method."""

    

    cli_utils.establish_connection(ctx)
    
    
    

    ctx.logger.info(""": """"""asynchandle = """ + str(asynchandle)+";" + """keepresult = """+str(keepresult)+""";"""+"")
    try:
        _dict = ctx.element.get_async_result(async_handle=asynchandle, keep_result=keepresult)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_dict), indent=4))
        return
    else:
        cli_utils.print_result(_dict, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

