import click
from click.testing import CliRunner
from element.cli import cli
from unittest.mock import MagicMock

# For the connection commands we set it up so that the sdk returns a fake connection.
def check_push():
    runner = CliRunner()
    #result = runner.invoke(cli.cli, ["--help"])
    result = runner.invoke(cli.cli, ['--mvip', "10.117.61.44", "--login", "admin", "--password", "admin", "--pushconnection", True, "--name", "a", "Volume", "ListVolumes"])
    print(result.output)

check_push()