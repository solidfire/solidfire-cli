import click
from click.testing import CliRunner
from element.cli import cli
import jsonpickle
import random
import os
import csv
from unittest.mock import MagicMock

def rand_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(length))

def check_array_input():
    # First, make a new account.
    print("hi")
    runner = CliRunner()
    account_name = rand_string(15)
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "Add", '--username', account_name])
    account = jsonpickle.decode(result.output)

    # Next, make two volumes


    # Now tear down the account.
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "Remove", '--account_id', account.account_id])
    print(result.output)
    # Next, verify that it happened by opening up the csv file and checking.

check_array_input()