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
    """ListUtilities List ConnectMvip ConnectSvip ConnectEnsemble Ping """

@cli.command('ListUtilities', short_help="""The ListUtilities API method is used to return the tests that are available to run on a node. Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@pass_context
def ListUtilities(ctx):
    """The ListUtilities API method is used to return the tests that are available to run on a node."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        ListUtilitiesResult = ctx.element.list_utilities()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListUtilitiesResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('List', short_help="""The ListTests API method is used to return the tests that are available to run on a node. Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@pass_context
def List(ctx):
    """The ListTests API method is used to return the tests that are available to run on a node."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        ListTestsResult = ctx.element.list_tests()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(ListTestsResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ConnectMvip', short_help="""The TestConnectMvip API method is used to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity. Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@click.option('--mvip',
              type=str,
              required=False,
              help="""Optionally, use to test the management connection of a different MVIP. This is not needed to test the connection to the target cluster. """)
@pass_context
def ConnectMvip(ctx,
           mvip = None):
    """The TestConnectMvip API method is used to test the management connection to the cluster. The test pings the MVIP and executes a simple API method to verify connectivity."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""mvip = """+str(mvip)+""";"""+"")
    try:
        TestConnectMvipResult = ctx.element.test_connect_mvip(mvip=mvip)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(TestConnectMvipResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ConnectSvip', short_help="""The TestConnectSvip API method is used to test the storage connection to the cluster. The test pings the SVIP using ICMP packets and when successful connects as an iSCSI initiator. Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@click.option('--svip',
              type=str,
              required=False,
              help="""Optionally, use to test the storage connection of a different SVIP. This is not needed to test the connection to the target cluster. """)
@pass_context
def ConnectSvip(ctx,
           svip = None):
    """The TestConnectSvip API method is used to test the storage connection to the cluster. The test pings the SVIP using ICMP packets and when successful connects as an iSCSI initiator."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""svip = """+str(svip)+""";"""+"")
    try:
        TestConnectSvipResult = ctx.element.test_connect_svip(svip=svip)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(TestConnectSvipResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('ConnectEnsemble', short_help="""The TestConnectEnsemble API method is used to verify connectivity with a sepcified database ensemble. By default it uses the ensemble for the cluster the node is associated with. Alternatively you can provide a different ensemble to test connectivity with. Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@click.option('--ensemble',
              type=str,
              required=False,
              help="""A comma-separated list of ensemble node CIPs for connectivity testing """)
@pass_context
def ConnectEnsemble(ctx,
           ensemble = None):
    """The TestConnectEnsemble API method is used to verify connectivity with a sepcified database ensemble. By default it uses the ensemble for the cluster the node is associated with. Alternatively you can provide a different ensemble to test connectivity with."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""ensemble = """+str(ensemble)+""";"""+"")
    try:
        TestConnectEnsembleResult = ctx.element.test_connect_ensemble(ensemble=ensemble)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(TestConnectEnsembleResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('Ping', short_help="""The TestPing API method is used to validate the connection to all nodes in the cluster on both 1G and 10G interfaces using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration. Note: This method is available only through the per-node API endpoint 5.0 or later. """)
@click.option('--attempts',
              type=int,
              required=False,
              help="""Specifies the number of times the system should repeat the test ping. Default is 5. """)
@click.option('--hosts',
              type=str,
              required=False,
              help="""Specify address or hostnames of devices to ping. """)
@click.option('--total_timeout_sec',
              type=int,
              required=False,
              help="""Specifies the length of time the ping should wait for a system response before issuing the next ping attempt or ending the process. """)
@click.option('--packet_size',
              type=int,
              required=False,
              help="""Specify the number of bytes to send in the ICMP packet sent to each IP. Number be less than the maximum MTU specified in the network configuration. """)
@click.option('--ping_timeout_msec',
              type=int,
              required=False,
              help="""Specify the number of milliseconds to wait for each individual ping response. Default is 500ms. """)
@pass_context
def Ping(ctx,
           attempts = None,
           hosts = None,
           total_timeout_sec = None,
           packet_size = None,
           ping_timeout_msec = None):
    """The TestPing API method is used to validate the connection to all nodes in the cluster on both 1G and 10G interfaces using ICMP packets. The test uses the appropriate MTU sizes for each packet based on the MTU settings in the network configuration."""
    """Note: This method is available only through the per-node API endpoint 5.0 or later."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("""attempts = """+str(attempts)+""";"""+"""hosts = """+str(hosts)+""";"""+"""total_timeout_sec = """+str(total_timeout_sec)+""";"""+"""packet_size = """+str(packet_size)+""";"""+"""ping_timeout_msec = """+str(ping_timeout_msec)+""";"""+"")
    try:
        TestPingResult = ctx.element.test_ping(attempts=attempts, hosts=hosts, total_timeout_sec=total_timeout_sec, packet_size=packet_size, ping_timeout_msec=ping_timeout_msec)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(TestPingResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

