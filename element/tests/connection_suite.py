import click
from click.testing import CliRunner
from element.cli import cli
import os
import csv
from unittest.mock import MagicMock

# For the connection commands we set it up so that the sdk returns a fake connection.
def check_functionality():
    runner = CliRunner()
    # First run the push
    result = runner.invoke(cli.cli, ['--mvip', "10.117.61.44", "--login", "admin", "--password", "admin", "--name", "b","Connection", "PushConnection"])
    # Next, verify that it happened by opening up the csv file and checking.

    connectionsCsvLocation = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "connections.csv")
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))

    assert connections[-1]["mvip"] == "10.117.61.44"
    assert connections[-1]["login"] == "admin"
    assert connections[-1]["password"] == "admin"
    assert connections[-1]["name"] == "b"
    print("Push is working")

    result = runner.invoke(cli.cli, ["Connection", "RemoveConnection", "--name", "b"])
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))
    connectionsNamedb = [connection for connection in connections if connection["name"] == "b"]
    assert len(connectionsNamedb) == 0
    print("Remove is working")
    print("Functionality is good")



check_functionality()