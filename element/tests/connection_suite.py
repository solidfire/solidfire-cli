import click
from click.testing import CliRunner
from element.cli import cli
import os
import csv
from pkg_resources import Requirement, resource_filename

# For the connection commands we set it up so that the sdk returns a fake connection.
def check_functionality_of_connection_suite():
    runner = CliRunner()

    #WARNING THIS NEXT LINE DELETES THE CONNECTIONS CSV FILE FOR THE TESTS. COMMENTING IT OUT MIGHT RUIN FUNCTIONALITY OF TESTS
    try:
        os.remove(os.path.join("..","..", "connections.csv"))
    except:
        pass

    # First run the push
    result = runner.invoke(cli.cli, ["connection", "push", '--mvip', "10.117.61.129", "--username", "admin", "--password", "admin", "--name", "abcd"])
    # Next, verify that it happened by opening up the csv file and checking.


    connectionsCsvLocation = os.path.join("..","..", "connections.csv")
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))
    assert connections[0]["mvip"] == "10.117.61.129"
    assert connections[0]["username"] == "admin"
    assert connections[0]["name"] == "abcd"
    print("Push (with manually set name) is working")

    result = runner.invoke(cli.cli, ["Connection", "Remove", "--name", "abcd"]) #connection and remove need to be capitalized (or maybe one of them), but lowercase doesnt work and silently fails
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))
    connectionsNamed = [connection for connection in connections if connection["name"] == "abcd"]
    assert len(connectionsNamed) == 0
    print("Remove is working")

    #Check auto naming
    result = runner.invoke(cli.cli,
                           ["connection", "push", '--mvip', "10.117.61.129", "--username", "admin", "--password",
                            "admin"])
    # Next, verify that it happened by opening up the csv file and checking.

    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))
    assert connections[0]["mvip"] == "10.117.61.129"
    assert connections[0]["username"] == "admin"
    assert connections[0]["name"] == "CCcluster" #this is specific to Chris Cochran's Cluster 10.117.61.129, autos to the name of the cluster
    print("Push (with auto naming) is working")


    #Check if repeat names are blocked
    result = runner.invoke(cli.cli, ["connection", "push", '--mvip', "10.117.61.129", "--username", "admin", "--password", "admin"])

    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))
    assert len(connections) == 1
    print("Unique name working properly.")



    #Check if port auto naming works
    result = runner.invoke(cli.cli, ["connection", "push", '--mvip', "10.117.61.125", "--username", "admin", "--password", "admin", "-q", "442"])


    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))

    assert connections[0]["mvip"] == "10.117.61.125"
    assert connections[0]["username"] == "admin"
    assert connections[0]["name"] == "node1"  # this is specific to Chris Cochran's Cluster 10.117.61.129, autos to node1 of the cluster and uses that name
    print("Push (with auto naming) for ports is working")


    #Check if default was properly set.
    #Checking recent port push has correct info and is default
    assert connections[0]["mvip"] == "10.117.61.125"
    assert connections[0]["username"] == "admin"
    assert connections[0]["name"] == "node1"
    assert connections[0]["default"] == "True"
    #Checking if previous cluster push has correct info and is NOT default
    assert connections[1]["mvip"] == "10.117.61.129"
    assert connections[1]["username"] == "admin"
    assert connections[1]["name"] == "CCcluster"
    assert connections[1]["default"] == "False"

    print("Defaults are properly set for push.")

    #Another check for connections # check
    assert len(connections) == 2
    print("Connections length still correct.")

    #checking if removing the default (0th index) will make the previously 1st index the new default
    result = runner.invoke(cli.cli, ["Connection", "Remove", "--index", "0"])
    with open(connectionsCsvLocation) as connectionFile:
        connections = list(csv.DictReader(connectionFile, delimiter=','))

    # Checking new 0th index has correct info and is default
    assert connections[0]["name"] == "CCcluster"
    assert connections[0]["default"] == "True"
    print("Deleting the default does shift in new default.")

    #checking that deleting when the file is empty doesnt throw errors
    result = runner.invoke(cli.cli, ["Connection", "Remove", "--name", "CCcluster"])
    result = runner.invoke(cli.cli, ["Connection", "Remove", "--index", "0"])
    print("Removing the final connection doesn't throw errors.")

    print("Functionality is all good")

check_functionality_of_connection_suite()

##connections correct

##list correct #

#set defaults and make sure they follow through

#make sure coommands dont set default