import click

from element.cli import utils as cli_utils
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
from element.exceptions import *
import os
import csv
from solidfire.factory import ElementFactory


@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client


@cli.command('establish', short_help='Establish a new connection for this session.')
@click.option('--mvip', '-m',
              default=None,
              help="SolidFire MVIP",
              required=True)
@click.option('--login', '-l',
              default=None,
              help="SolidFire Cluster login",
              required=True)
@click.option('--password', '-p',
              default=None,
              help="SolidFire cluster password",
              required=True)
@click.option('--port', '-q',
              default=443,
              help="The port",
              required=False)
@click.option('--name', '-n',
              default=None,
              type=click.INT,
              help="The connection name",
              required=True)
@pass_context
def establish(ctx, mvip, login, password, port, name):
    # No two connections can have the same name.
    existingConnection = ctx.connections.get(name, None)
    if existingConnection is not None:
        raise SolidFireUsageException("That connection name is already in use. Try a different one.")

    # Now establish the connection. Also set it up as the default connection.
    ctx.connections[name] = dict()
    ctx.connections[name]["element"] = ElementFactory.create(mvip, login, password, port=port)
    ctx.connections[name]["cfg"] = {"mvip": mvip, "login": login, "password": password, "port": port, "name": name}

@cli.command('disconnect', short_help='This is the counterpart to establish. It deletes a connection from the session.')
@click.option('--name', '-n',
              default=None,
              type=click.INT,
              help="The connection name",
              required=True)
@pass_context
def disconnect(ctx, name):
    # Remove the connection from the dictionary, freeing up the name
    ctx.connections.pop(name, None)

@cli.command('load', short_help='Load a connection saved in connections.csv')
@click.option('--name', '-n',
              default=None,
              type=click.INT,
              help="The connection name",
              required=True)
@pass_context
def load(ctx, name):
    # First, we pull out all the connections we have saved away.
    connectionsCsvLocation = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..","..","connections.csv")
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))

    # Then we find the one we want and establish a connection to it.
    for connection in connections:
        if connection["name"] == name:
            try:
                establish(ctx,
                          connection["mvip"],
                          connection["login"],
                          connection["password"],
                          connection["port"],
                          connection["name"]
                          )
            except SolidFireUsageException:
                raise SolidFireUsageException("There is already a connection with that name in the existing session.")

@cli.command('save', short_help='Save a new connection from this session to the connections.csv file.')
@click.option('--name', '-n',
              default=None,
              type=click.INT,
              help="The connection name",
              required=True)
@pass_context
def save(ctx, name):
    # First, we get the connection from the session.
    existingConnection = ctx.connections.get(name, None)
    if existingConnection is None:
        raise SolidFireUsageException("No connection of that name.")

    # Next, we check to make sure the connection has a unique name.
    connectionsCsvLocation = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..","..","connections.csv")
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))
    for connection in connections:
        if connection["name"] == name:
            raise SolidFireUsageException("A connection has already been saved with that name.")

    # Finally, we pull out all the features of the connection and store them away.
    connections += [existingConnection["cfg"]]
    with open(connectionsCsvLocation, 'w') as f:
        w = csv.DictWriter(f, ["mvip","port","login","password","url"], lineterminator='\n')
        w.writeheader()
        for connection in connections:
            if connection is not None:
                w.writerow(connection)

@cli.command('remove', short_help='Remove a connection from the connections.csv file.')
@click.option('--name', '-n',
              default=None,
              type=click.INT,
              help="The connection name",
              required=True)
@pass_context
def remove(ctx, name):
    connectionsCsvLocation = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..","..","connections.csv")

    # First, get all the connections and delete the one we don't want.
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))
    newConnectionsList = [connection for connection in connections if connection["name"] != name]

    # Now we write it back
    with open(connectionsCsvLocation, 'w') as f:
        w = csv.DictWriter(f, ["mvip","port","login","password","url"], lineterminator='\n')
        w.writeheader()
        for connection in newConnectionsList:
            if connection is not None:
                w.writerow(connection)