#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.

from __future__ import unicode_literals

import click

import os
import csv
from element.cli.cli import pass_context
from pkg_resources import Requirement, resource_filename
import simplejson
from element.cli import utils as cli_utils
from solidfire.factory import ElementFactory

@click.group()
@pass_context
def cli(ctx):
    """Connection management"""

@cli.command('push', short_help="Pushes the connection onto connections.csv to save for later use. This is located at "+resource_filename(Requirement.parse("solidfire-cli"), "connections.csv")
)
@click.option('--mvip', '-m',
              default=None,
              help="SolidFire MVIP",
              required=False,
              prompt=True)
@click.option('--username', '-u',
              default=None,
              help="SolidFire cluster username",
              required=False)
@click.option('--password', '-p',
              default=None,
              help="SolidFire cluster password",
              required=False)
@click.option('--version', '-v',
              default = None,
              help='The version you would like to connect on',
              required=False)
@click.option('--name', '-n',
              default = None,
              help="The name you want to associate with the connection'.",
              required=False,
              prompt=False)
@click.option('--port', '-q',
              default = None,
              help="The port you wish to connect on",
              required=False)
@click.option('--verifyssl', '-s',
              default = None,
              help="Enable this to check ssl connection for errors especially when using a hostname. It is invalid to set this to true when using an IP address in the target.",
              required=False,
              is_flag=True)
@click.option('--timeout', '-t',
              default = None,
              help="The request timeout in seconds",
              required=False)
@pass_context
def push(ctx, mvip, username, password, version, port, name, verifyssl, timeout):
    # First, attempt to establish the connection. If that's not possible,
    # throw the error.

    if mvip and ctx.mvip and mvip != ctx.mvip:
        ctx.logger.error("Please only provide the mvip once. The two you provided are different.")
        exit(1)
    if username and ctx.username and username != ctx.username:
        ctx.logger.error("Please only provide the username once. The two you provided are different.")
        exit(1)
    if password and ctx.password and password != ctx.password:
        ctx.logger.error("Please only provide the password once. The two you provided are different.")
        exit(1)
    if name and ctx.name and name != ctx.name:
        ctx.logger.error("Please only provide the name once. The two you provided are different.")
        exit(1)

    if ctx.mvip is None and mvip is None:
        ctx.logger.error("Please provide the mvip. It is a required parameter.")
        exit(1) #Should never be hit, but leaving it in just in case.

    if ctx.mvip is None:
        ctx.mvip = mvip
    if ctx.username is None:
        ctx.username = username
    if ctx.password is None:
        ctx.password = password
    if version is not None:
        ctx.version = str(float(version))
    if port is not None:
        ctx.port = port
    if timeout is not None:
        ctx.timeout = timeout
    if verifyssl is not None:
        ctx.verifyssl = verifyssl
    if ctx.name is None:
        ctx.name = name

    # Verify that the connection exists or get the extra info.
    cli_utils.establish_connection(ctx)

    if ctx.name is None: #if user has not specified a name
        if (str(ctx.port) == "443"): #port 443 is a cluster
            ctx.name = ctx.element.get_cluster_info().cluster_info.name
        elif (str(ctx.port) == "442"): #port 442 is node
            ctx.name = ctx.element.get_config().config.cluster.name
    connections = cli_utils.get_connections(ctx)
    # First, ensure that no other connections have the same name:
    sameName = [connection for connection in connections if connection["name"]==ctx.name]
    if sameName != []:
        ctx.logger.error("A connection with that name already exists. Please try another.")
        exit(1)

    if(ctx.username is not None and ctx.password is not None):
        ctx.username = cli_utils.encrypt(ctx.username)
        ctx.password = cli_utils.encrypt(ctx.password)

    connections = connections + [{'mvip': ctx.mvip,
                                  'username': "b'"+ctx.username.decode('utf-8')+"'",
                                  'password': "b'"+ctx.password.decode('utf-8')+"'",
                                  'port': ctx.port,
                                  'url': 'https://%s:%s' % (ctx.mvip, ctx.port),
                                  'version': ctx.version,
                                  'name': ctx.name,
                                  'verifyssl': ctx.verifyssl,
                                  'timeout': ctx.timeout}]

    cli_utils.write_connections(ctx, connections)

@cli.command('remove', short_help="Removes a given connection")
@click.option('--name', '-n',
              type=str,
              required=False,
              help="""The name of the connection you wish to remove.""")
@click.option('--index', '-i',
              type=int,
              required=False,
              help="""The index of the connection you wish to remove - 0 is the oldest, 1 is the second oldest, and -1 is the newest.""")
@pass_context
def remove(ctx, name=None, index=None):
    if name is not None and index is not None:
        ctx.logger.error("You must provide either the name or the index. Not both.")
        exit(1)
    if name is None and index is None:
        ctx.logger.error("You must provide either the name or the index of the connection to remove.")
        exit(1)

    connections = cli_utils.get_connections(ctx)
    if index is not None and index > (len(connections) - 1):
        ctx.logger.error("Your connection index is greater than the maximum index of your connections stack.")

    # Filter by name
    if name is not None:
        connections = [connection for connection in connections if connection["name"]!=name]
    # Filter by index
    if index is not None:
        del connections[index]
    cli_utils.write_connections(ctx, connections)

@cli.command('list', short_help="Lists the stored connection info")
@click.option('--name', '-n',
              type=str,
              required=False,
              help="""The name of the connection you wish to view.""")
@click.option('--index', '-i',
              type=int,
              required=False,
              help="""The index of the connection you wish to view - 0 is the oldest, 1 is the second oldest, and -1 is the newest.""")
@pass_context
def list(ctx, name=None, index=None):
    connectionsCsvLocation = resource_filename(Requirement.parse("solidfire-cli"), "connections.csv")
    connections = cli_utils.get_connections(ctx)
    print(connectionsCsvLocation)
    if(name is None and index is None):
        cli_utils.print_result(connections, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
    if(name is None and index is not None):
        cli_utils.print_result(connections[int(index)], ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
    if(name is not None and index is None):
        connections = [connection for connection in connections if connection["name"]==name]
        cli_utils.print_result(connections, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)

@cli.command('prune', short_help="If something changes in your cluster, a connection which may have been valid before may not be valid now. To find and remove those connections, use prune.")
@pass_context
def prune(ctx):
    connections = cli_utils.get_connections(ctx)
    goodConnections = []
    for connection in connections:
        if not all (k in connection.keys() for k in ["mvip", "username", "password", "version", "port", "name"]):
            print("Removing connection, ")
            cli_utils.print_result(connection, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
            print("Connection info did not contain the following fields: mvip, username, password, version, port, and url")
            print()
            continue
        try:
            ElementFactory.create(connection["mvip"],cli_utils.decrypt(connection["username"]),cli_utils.decrypt(connection["password"]),version=connection["version"],port=connection["port"])
            goodConnections += [connection]
        except Exception as e:
            print("Removing connection, ")
            cli_utils.print_result(connection, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
            print(e.__str__())
            print()
    cli_utils.write_connections(ctx, goodConnections)