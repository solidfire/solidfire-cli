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
<<<<<<< HEAD
    """SetInfo GetRemoteLoggingHosts SetRemoteLoggingHosts GetInfo """

@cli.command('SetInfo', short_help="""SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed. """)
@click.option('--timeout',
              type=str,
              required=True,
              help="""Cluster authentication expiration period. Formatted in HH:mm:ss. For example: 01:30:00, 00:90:00, and 00:00:5400 can all be used to equal a 90 minute timeout period. Default is 30 minutes. """)
@pass_context
def SetInfo(ctx,
           timeout):
    """SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed."""
=======
    """GetInfo GetRemoteLoggingHosts SetRemoteLoggingHosts SetInfo """

@cli.command('GetInfo', short_help="""GetLoginSessionInfo is used to return the period of time a log in authentication is valid for both log in shells and the TUI. """)
@pass_context
def GetInfo(ctx):
    """GetLoginSessionInfo is used to return the period of time a log in authentication is valid for both log in shells and the TUI."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
    ctx.logger.info("""timeout = """+str(timeout)+""";"""+"")
    try:
        SetLoginSessionInfoResult = ctx.element.set_login_session_info(timeout=timeout)
=======
    ctx.logger.info("")
    try:
        GetLoginSessionInfoResult = ctx.element.get_login_session_info()
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(SetLoginSessionInfoResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(GetLoginSessionInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.



@cli.command('GetRemoteLoggingHosts', short_help="""GetRemoteLoggingHosts is used to retrieve the current list of log servers. """)
@pass_context
def GetRemoteLoggingHosts(ctx):
    """GetRemoteLoggingHosts is used to retrieve the current list of log servers."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    ctx.logger.info("")
    try:
        GetRemoteLoggingHostsResult = ctx.element.get_remote_logging_hosts()
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(GetRemoteLoggingHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



@cli.command('SetRemoteLoggingHosts', short_help="""RemoteLoggingHosts is used to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use the GetRemoteLoggingHosts to determine what the current logging hosts are and then use the SetRemoteLoggingHosts to set the desired list of current and new logging hosts. """)
@click.option('--logging_server_host',
              type=str,
              required=True,
              help="""Hostname or IP address of the log server. """)
@click.option('--logging_server_port',
              type=int,
              required=True,
              help="""Port number that the log server is listening on. """)
@pass_context
def SetRemoteLoggingHosts(ctx,
           logging_server_host,
           logging_server_port):
    """RemoteLoggingHosts is used to configure remote logging from the nodes in the storage cluster to a centralized log server or servers. Remote logging is performed over TCP using the default port 514. This API does not add to the existing logging hosts. Rather, it replaces what currently exists with new values specified by this API method. You can use the GetRemoteLoggingHosts to determine what the current logging hosts are and then use the SetRemoteLoggingHosts to set the desired list of current and new logging hosts."""
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



    remote_hosts = None
    if(remote_hosts is not None or False):
        kwargsDict = dict()
        kwargsDict["host"] = logging_server_host
        kwargsDict["port"] = logging_server_port

        remote_hosts = LoggingServer(**kwargsDict)

    remote_hosts = parser.parse_array(remote_hosts)

    ctx.logger.info("""remote_hosts = """+str(remote_hosts)+""";"""+"")
    try:
        SetRemoteLoggingHostsResult = ctx.element.set_remote_logging_hosts(remote_hosts=remote_hosts)
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

    cli_utils.print_result(SetRemoteLoggingHostsResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)



<<<<<<< HEAD
@cli.command('GetInfo', short_help="""GetLoginSessionInfo is used to return the period of time a log in authentication is valid for both log in shells and the TUI. """)
@pass_context
def GetInfo(ctx):
    """GetLoginSessionInfo is used to return the period of time a log in authentication is valid for both log in shells and the TUI."""
=======
@cli.command('SetInfo', short_help="""SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed. """)
@click.option('--timeout',
              type=str,
              required=True,
              help="""Cluster authentication expiration period. Formatted in HH:mm:ss. For example: 01:30:00, 00:90:00, and 00:00:5400 can all be used to equal a 90 minute timeout period. Default is 30 minutes. """)
@pass_context
def SetInfo(ctx,
           timeout):
    """SetLoginSessionInfo is used to set the period of time a log in authentication is valid. After the log in period elapses without activity on the system the authentication will expire. New log in credentials will be required for continued access to the cluster once the timeout period has elapsed."""
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    if ctx.element is None:
         ctx.logger.error("You must establish at least one connection and specify which you intend to use.")
         exit()



<<<<<<< HEAD
    ctx.logger.info("")
    try:
        GetLoginSessionInfoResult = ctx.element.get_login_session_info()
=======
    ctx.logger.info("""timeout = """+str(timeout)+""";"""+"")
    try:
        SetLoginSessionInfoResult = ctx.element.set_login_session_info(timeout=timeout)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.
    except common.ApiServerError as e:
        ctx.logger.error(e.message)
        exit()
    except BaseException as e:
        ctx.logger.error(e.__str__())
        exit()

<<<<<<< HEAD
    cli_utils.print_result(GetLoginSessionInfoResult, ctx.logger, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)
=======
    cli_utils.print_result(SetLoginSessionInfoResult, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
>>>>>>> Adds non-pickle json functionality so that set-networkconfig can use get-networkconfig's output.

