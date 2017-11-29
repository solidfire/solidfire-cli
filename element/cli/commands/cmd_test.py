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
    """list ping connectmvip listutilities connectensemble connectsvip """

@cli.command('list', short_help="""You can use the ListTests API method to return the tests that are available to run on a node. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def list(ctx):
    """You can use the ListTests API method to return the tests that are available to run on a node."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListTestsResult = ctx.element.list_tests()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListTestsResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListTestsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ping', short_help="""You can use the TestPing API method to validate the connection to all the nodes in a cluster on both 1G and 10G interfaces by using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--attempts',
              type=int,
              required=False,
              help="""Specifies the number of times the system should repeat the test ping. The default value is 5. """)
@click.option('--hosts',
              type=str,
              required=False,
              help="""Specifies a comma-separated list of addresses or hostnames of devices to ping. """)
@click.option('--totaltimeoutsec',
              type=int,
              required=False,
              help="""Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. """)
@click.option('--packetsize',
              type=int,
              required=False,
              help="""Specifies the number of bytes to send in the ICMP packet that is sent to each IP. The number must be less than the maximum MTU specified in the network configuration. """)
@click.option('--pingtimeoutmsec',
              type=int,
              required=False,
              help="""Specifies the number of milliseconds to wait for each individual ping response. The default value is 500 ms. """)
@click.option('--prohibitfragmentation',
              type=bool,
              required=False,
              help="""Specifies that the Do not Fragment (DF) flag is enabled for the ICMP packets. """)
@pass_context
def ping(ctx,
           # Optional main parameter
           attempts = None,
           # Optional main parameter
           hosts = None,
           # Optional main parameter
           totaltimeoutsec = None,
           # Optional main parameter
           packetsize = None,
           # Optional main parameter
           pingtimeoutmsec = None,
           # Optional main parameter
           prohibitfragmentation = None):
    """You can use the TestPing API method to validate the"""
    """connection to all the nodes in a cluster on both 1G and 10G interfaces by using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    
    
    
    
    
    

    ctx.logger.info(""": """"""attempts = """+str(attempts)+";" + """hosts = """+str(hosts)+";" + """totaltimeoutsec = """+str(totaltimeoutsec)+";" + """packetsize = """+str(packetsize)+";" + """pingtimeoutmsec = """+str(pingtimeoutmsec)+";" + """prohibitfragmentation = """+str(prohibitfragmentation)+""";"""+"")
    try:
        _TestPingResult = ctx.element.test_ping(attempts=attempts, hosts=hosts, total_timeout_sec=totaltimeoutsec, packet_size=packetsize, ping_timeout_msec=pingtimeoutmsec, prohibit_fragmentation=prohibitfragmentation)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestPingResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestPingResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('connectmvip', short_help="""The TestConnectMvip API method enables you to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--mvip',
              type=str,
              required=False,
              help="""If specified, tests the management connection of a different MVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. """)
@pass_context
def connectmvip(ctx,
           # Optional main parameter
           mvip = None):
    """The TestConnectMvip API method enables you to test the"""
    """management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""mvip = """+str(mvip)+""";"""+"")
    try:
        _TestConnectMvipResult = ctx.element.test_connect_mvip(mvip=mvip)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestConnectMvipResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestConnectMvipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('listutilities', short_help="""You can use the ListUtilities API method to return the operations that are available to run on a node.  Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@pass_context
def listutilities(ctx):
    """You can use the ListUtilities API method to return the operations that are available to run on a node. """
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    

    ctx.logger.info(""": """+""";"""+"")
    try:
        _ListUtilitiesResult = ctx.element.list_utilities()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_ListUtilitiesResult), indent=4))
        return
    else:
        cli_utils.print_result(_ListUtilitiesResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('connectensemble', short_help="""The TestConnectEnsemble API method enables you to verify connectivity with a specified database ensemble. By default, it uses the ensemble for the cluster that the node is associated with. Alternatively, you can provide a different ensemble to test connectivity with. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--ensemble',
              type=str,
              required=False,
              help="""Uses a comma-separated list of ensemble node cluster IP addresses to test connectivity. This parameter is optional. """)
@pass_context
def connectensemble(ctx,
           # Optional main parameter
           ensemble = None):
    """The TestConnectEnsemble API method enables you to verify connectivity with a specified database ensemble. By default, it uses the ensemble for the cluster that the node is associated with. Alternatively, you can provide a different ensemble to test connectivity with."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""ensemble = """+str(ensemble)+""";"""+"")
    try:
        _TestConnectEnsembleResult = ctx.element.test_connect_ensemble(ensemble=ensemble)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestConnectEnsembleResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestConnectEnsembleResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('connectsvip', short_help="""The TestConnectSvip API method enables you to test the storage connection to the cluster. The test pings the SVIP using ICMP packets, and when successful, connects as an iSCSI initiator. Note: This method is available only through the per-node API endpoint 5.0 or later. """, cls=SolidFireCommand)
@click.option('--svip',
              type=str,
              required=False,
              help="""If specified, tests the storage connection of a different SVIP. You do not need to use this value when testing the connection to the target cluster. This parameter is optional. """)
@pass_context
def connectsvip(ctx,
           # Optional main parameter
           svip = None):
    """The TestConnectSvip API method enables you to test the storage connection to the cluster. The test pings the SVIP using ICMP packets, and when successful, connects as an iSCSI initiator."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""

    

    cli_utils.establish_connection(ctx)
    
    

    ctx.logger.info(""": """"""svip = """+str(svip)+""";"""+"")
    try:
        _TestConnectSvipResult = ctx.element.test_connect_svip(svip=svip)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()
    if ctx.json:
        print(simplejson.dumps(simplejson.loads(_TestConnectSvipResult), indent=4))
        return
    else:
        cli_utils.print_result(_TestConnectSvipResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

