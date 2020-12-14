import jsonpickle
import click
from click.testing import CliRunner
from element.cli import cli
import os
import csv
from pkg_resources import Requirement, resource_filename
# This MVIP will be given to all test cases
ip = '10.117.66.46'
def createconnection():
    runner = CliRunner()
    # First run the push
    result = runner.invoke(cli.cli, ['connection', 'push', '--mvip', ip, "--username", "admin", "--password", "admin", "--name", "connect"])
    #create connection with ip we want will get saved in cannections .csv
def removeconnection():
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["Connection", "remove", "--name", "connect"])
    #connection will get removed

