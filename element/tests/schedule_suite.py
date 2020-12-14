from click.testing import CliRunner

from element.cli import cli
from element.tests import mvipip

# For the connection commands we set it up so that the sdk returns a fake connection.
def test_schedule_modify_suite():
    runner = CliRunner()
    # First run the push
    result = runner.invoke(cli.cli, ['connection', 'push', '--mvip', mvipip.ip, "--username", "admin", "--password", "admin", "--name", "connectname"])
    assert result.exit_code == 0


    result = runner.invoke(cli.cli, ["schedule", "modify", "--name", "name", "--scheduleid", '4', "--recurring", False])
    assert result.exit_code == 0
    result = runner.invoke(cli.cli, ["Connection", "remove", "--name", "connectname"])

