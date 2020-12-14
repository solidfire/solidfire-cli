import click
from click.testing import CliRunner
from element.cli import cli
import os
import csv
from pkg_resources import Requirement, resource_filename
from element.tests import mvipip

# For the connection commands we set it up so that the sdk returns a fake connection.
def test_check_functionality_of_connection_suite():
    runner = CliRunner()
    # First run the push
    result = runner.invoke(cli.cli, ['connection', 'push', '--mvip', mvipip.ip, "--username", "admin", "--password", "admin", "--name", "name"])
    # Next, verify that it happened by opening up the csv file and checking.

    connectionsCsvLocation = resource_filename(Requirement.parse("solidfire-cli"), "connections.csv")
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))

    assert connections[-1]["mvip"] == mvipip.ip
    assert connections[-1]["username"] is not None
    assert connections[-1]["password"] is not None
    assert connections[-1]["name"] == "name"
    print("Push is working")

    result = runner.invoke(cli.cli, ["Connection", "remove", "--name", "name"])
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))
    connectionsNamedb = [connection for connection in connections if connection["name"] == "name"]
    assert len(connectionsNamedb) == 0
    print("Remove is working")
    print("Functionality is good")

#check_functionality_of_connection_suite()
