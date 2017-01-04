import click
from click.testing import CliRunner
from element.cli import cli
from unittest.mock import MagicMock

# For the connection commands we set it up so that the sdk returns a fake connection.
def check_push():
    runner = CliRunner()
    # First run the push
    result = runner.invoke(cli.cli, ['--mvip', "10.117.61.44", "--login", "admin", "--password", "admin", "--pushconnection", "--name", "a", "Volume", "ListVolumes"])
    # Next, verify that it happened by opening up the csv file and checking.

    print(result.output)

check_push()