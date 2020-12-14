import click
from click.testing import CliRunner
from element.cli import cli
from testfixtures import LogCapture
from element.cli import utils
import os
import csv
from element.tests import mvipip

# Check the tree generator:
def test_check_api_error():
    runner = CliRunner()
    mvipip.createconnection()
    with LogCapture() as l :
        result = runner.invoke(cli.cli, ['--debug', '0', '-c', '0', 'Account', 'GetByID', '--accountid', '1000000'])
        l.clear()
        l.check()
    print("Critical setting working.")
    with LogCapture() as l:
        result = runner.invoke(cli.cli, ['--debug', '1', '-c', '0', 'Account', 'GetByID', '--accountid', '1000000'])
        l.records = l.records[-1:] #Eliminating info level logs and capturing only desired result
        l.check(('element.cli.cli', 'ERROR', 'xUnknownAccount'))
    print("Error setting working.")
    with LogCapture() as l:
        result = runner.invoke(cli.cli, ['--debug', '2', '-c', '0', 'Account', 'GetByID', '--accountid', '1000000'])
        l.records = l.records[-1:] #Eliminating info level logs and capturing only desired result 
        l.check(('element.cli.cli', 'ERROR', 'xUnknownAccount'))
    print("Info setting is working.")
    mvipip.removeconnection()

