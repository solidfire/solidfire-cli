import click
from click.testing import CliRunner
from element.cli import cli
import jsonpickle
import random
import os
import csv
from solidfire.models import *
from unittest.mock import MagicMock
from element.tests import mvipip

def rand_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(length))

def test_check_strange_inputs():
    # First, make a new account. Set the CHAPSecret to confirm that CHAPSecrets work. This exercises a CHAPSecret parameter
    runner = CliRunner()
    mvipip.createconnection()
    account_name = rand_string(15)
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "Add", '--username', 'testnewaccount', '--initiatorsecret', "solidfire1234"])
    account = jsonpickle.decode(result.output)
    accid=account['result']['accountID']
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "GetByID", '--accountid', accid])
    fullAccount = jsonpickle.decode(result.output)

    # Verify that CHAPSecret is working.
    assert fullAccount['result']['account']['initiatorSecret'] == "solidfire1234"

    # Next, make two volumes
    result = runner.invoke(cli.cli, ['-c','0','-j',"volume", "create", '--name', 'testnewaccount', "--accountid", accid, "--totalsize", "1000000000", "--enable512e", "True"])
    volume1 = jsonpickle.decode(result.output)
    result = runner.invoke(cli.cli, ['-c','0','-j',"volume", "create", '--name', 'testnewaccount', "--accountid", accid, "--totalsize", "1000000000", "--enable512e", "True"])
    volume2 = jsonpickle.decode(result.output)

    # Now we modify the QoS settings on Volume1 in order to test the functionality of a complex param type:
    result = runner.invoke(cli.cli, ['-c','0','-j',"volume", "modify", '--volumeid', volume1['result']['volumeID'], '--miniops', "100"])

    # Now we get the volumes from the given account to make sure they're there and that the QoS Change took.:
    result = runner.invoke(cli.cli, ['-c','0','-j',"volume", "list", '--accounts', str(accid)])
    volumes_list = jsonpickle.decode(result.output)
    assert len(volumes_list['result']['volumes']) == 2
    newVolume1 = [volume for volume in volumes_list['result']['volumes'] if volume['volumeID'] == volume1['result']['volumeID']][0]
    assert newVolume1['qos']['minIOPS'] == 100

    # Now we delete and purge them. This exercises the use of an array.
    result = runner.invoke(cli.cli, ['-c','0','-j',"volume", "delete", '--volumeid', str(volume1['result']['volumeID'])])
    result = runner.invoke(cli.cli, ['-c','0','-j',"volume", "delete", '--volumeid', str(volume2['result']['volumeID'])])
    result = runner.invoke(cli.cli, ['-c','0','-j',"volume", "purgedeleted", '--volumeid', str(volume1['result']['volumeID'])])
    result = runner.invoke(cli.cli, ['-c','0','-j',"volume", "purgedeleted", '--volumeid', str(volume2['result']['volumeID'])])

    # Finally, we check to make sure they're gone.
    result = runner.invoke(cli.cli, ['-c','0','-j',"volume", "list", '--accounts', str(accid)])
    volumes_list = jsonpickle.decode(result.output)
    assert len(volumes_list['result']['volumes']) == 0

    # Now tear down the account.
    result = runner.invoke(cli.cli, ['-c','0','-j',"Account", "remove", '--accountid', str(accid)])

    # Now, to test a supercomplex parameter, we need to make a volume access group and set the attributes via json:
    result = runner.invoke(cli.cli, ['-c','0','-j',"volumeaccessgroup","create","--name", "DISPOSABLE", '--attributes', '{\"blah\":\"blah\"}'])
    volume_access_group = jsonpickle.decode(result.output)
    assert volume_access_group['result']['volumeAccessGroup']['attributes']["blah"] == "blah"
    result = runner.invoke(cli.cli, ['-c','0','-j',"volumeaccessgroup", "delete", '--volumeaccessgroupid', volume_access_group['result']['volumeAccessGroupID']])
    mvipip.removeconnection()
