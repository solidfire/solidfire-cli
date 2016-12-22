#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import json

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('remove', short_help="RemoveAccount")
@click.option('--account_id',
              type=int,
              required=True,
              help="AccountID for the account to remove. ")
@pass_context
def remove(ctx, account_id):
    """Used to remove an existing account."""
    """All Volumes must be deleted and purged on the account before it can be removed."""
    """If volumes on the account are still pending deletion, RemoveAccount cannot be used until DeleteVolume to delete and purge the volumes."""
    RemoveAccountResult = ctx.element.remove_account(account_id=account_id)
    keyPaths = {"username": True}
    print(keyPaths)
    cli_utils.print_result_as_tree(cli_utils.filter_objects(RemoveAccountResult, keyPaths))
    #print(json.dumps(json.loads(jsonpickle.encode(RemoveAccountResult)),indent=4))

