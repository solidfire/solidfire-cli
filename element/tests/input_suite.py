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
    runner = CliRunner()
    account_name = rand_string(15)
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "Add", '--username', account_name])
    account = jsonpickle.decode(result.output)

    # Next, make two volumes
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "Create", '--name', rand_string(15), "--account_id", account.account_id, "--total_size", "1000000000", "--enable512e", True])
    volume1 = jsonpickle.decode(result.output)
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "Create", '--name', rand_string(15), "--account_id", account.account_id, "--total_size", "1000000000", "--enable512e", True])
    volume2 = jsonpickle.decode(result.output)

    # Now we get the volumes from the given account to make sure they're there:
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "List", '--accounts', account.account_id])
    volumes_list = jsonpickle.decode(result.output)
    assert len(volumes_list.volumes) == 2

    # Now we delete and purge them. This exercises the use of an array.
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "Delete", '--volume_ids', ','.join([str(volume1.volume_id), str(volume2.volume_id)])])
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "PurgeDeleted", '--volume_ids', ','.join([str(volume1.volume_id), str(volume2.volume_id)])])

    # Finally, we check to make sure they're gone.
    result = runner.invoke(cli.cli, ['-c','0','-j',"Volume", "List", '--accounts', account.account_id])
    volumes_list = jsonpickle.decode(result.output)
    assert len(volumes_list.volumes) == 0

    # Now tear down the account.
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "Remove", '--account_id', account.account_id])

check_array_input()