import click
from click.testing import CliRunner
from element.cli import cli
from testfixtures import LogCapture
from element.cli import utils
import os
import csv

# Check the tree generator:
def check_api_error():
    runner = CliRunner()
    with LogCapture() as l:
        result = runner.invoke(cli.cli, ['--debug', '0', '-c', '0', 'Account', 'GetByID', '--account_id', '1000000'])
        l.check()
    print("Critical setting working.")
    with LogCapture() as l:
        result = runner.invoke(cli.cli, ['--debug', '1', '-c', '0', 'Account', 'GetByID', '--account_id', '1000000'])
        l.check(('element.cli.cli', "ERROR", "xUnknownAccount"))
    print("Error setting working.")
    with LogCapture() as l:
        result = runner.invoke(cli.cli, ['--debug', '2', '-c', '0', 'Account', 'GetByID', '--account_id', '1000000'])
        l.check(
            ('element.cli.cli', "INFO", "account_id = 1000000;"),
            ('element.cli.cli', "ERROR", "xUnknownAccount")
        )
    print("Info setting is working.")

check_api_error()