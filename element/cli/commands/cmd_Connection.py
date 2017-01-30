#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.

import click

import os
import csv
from element.cli.cli import pass_context
from element import exceptions
from pkg_resources import Requirement, resource_filename

@click.group()
@pass_context
def cli(ctx):
    """Connection management"""

@cli.command('push', short_help="Pushes the connection onto connection.csv to save for later use.")
@pass_context
def push(ctx):
    if(ctx.cfg.get("name", "") is None):
        ctx.logger.error("Please provide a connection name.")

    connectionsCsvLocation = resource_filename(Requirement.parse("solidfire-cli"), "connections.csv")
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))

    connections = connections + [ctx.cfg]
    with open(connectionsCsvLocation, 'w') as f:
        w = csv.DictWriter(f, ["name","mvip","port","login","password","url"], lineterminator='\n')
        w.writeheader()
        for connection in connections:
            if connection is not None:
                w.writerow(connection)

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
        raise exceptions.SolidFireUsageException("You must provide either the name or the index. Not both.")
    if name is None and index is None:
        raise exceptions.SolidFireUsageException("You must provide either the name or the index of the connection to remove.")
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