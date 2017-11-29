from click.testing import CliRunner

from element.cli import cli


# For the connection commands we set it up so that the sdk returns a fake connection.
def schedule_modify_suite():
    runner = CliRunner()
    # First run the push
    result = runner.invoke(cli.cli, ['-m', "10.117.61.60", "-u", "admin", "-p", "admin", "-n", "10.117.61.60", "connection", "push"])
    assert result.exit_code == 0


    result = runner.invoke(cli.cli, ["Schedule", "Modify", "-n", "10.117.61.60", "--scheduleid", 48, "--recurring", False])
    assert result.exit_code == 0

schedule_modify_suite()