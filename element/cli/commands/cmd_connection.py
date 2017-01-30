#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.

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

@cli.command('push', short_help="Pushes the connection onto connection.csv to save for later use.")
@pass_context
def push(ctx):
    # First, attempt to establish the connection. If that's not possible,
    # throw the error.
    try:
        ctx.element = ElementFactory.create(ctx.cfg["mvip"],ctx.cfg["login"],ctx.cfg["password"],ctx.cfg["version"],port=ctx.cfg["port"])
    except Exception as e:
        ctx.logger.error(e.__str__())
    if(ctx.cfg.get("name", "") is None):
        ctx.logger.error("Please provide a connection name.")
    connections = cli_utils.get_connections()
    connections = connections + [ctx.cfg]
    cli_utils.write_connections(connections)

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
    if name is None and index is None:
        ctx.logger.error("You must provide either the name or the index of the connection to remove.")
    connectionsCsvLocation = resource_filename(Requirement.parse("solidfire-cli"), "connections.csv")
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))

    # Filter by name
    if name is not None:
        connections = [connection for connection in connections if connection["name"]!=name]
    # Filter by index
    if index is not None:
        del connections[index]
    with open(connectionsCsvLocation, 'w') as f:
        w = csv.DictWriter(f, ["name","mvip","port","login","password","url"], lineterminator='\n')
        w.writeheader()
        for connection in connections:
            if connection is not None:
                w.writerow(connection)

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
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))
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
    connections = cli_utils.get_connections()
    goodConnections = []
    for connection in connections:
        try:
            ElementFactory.create(connection["mvip"],connection["login"],connection["password"],version=connection["version"],port=connection["port"])
            goodConnections += [connection]
        except Exception as e:
            print("Removing connection, ")
            cli_utils.print_result(connection, ctx.logger, as_json=ctx.json, as_pickle=ctx.pickle, depth=ctx.depth, filter_tree=ctx.filter_tree)
            print(e.__str__())
            print()
    cli_utils.write_connections(goodConnections)