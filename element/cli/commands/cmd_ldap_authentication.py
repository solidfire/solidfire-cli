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

@cli.command('test', short_help="TestLdapAuthentication")
@click.option('--username',
              type=str,
              required=True,
              help="The username to be tested. ")
@click.option('--password',
              type=str,
              required=True,
              help="The password for the username to be tester. ")
@click.option('--ldap_configuration',
              type=LdapConfiguration,
              required=False,
              help="An ldapConfiguration object to be tested. If this parameter is provided, the API call will test the provided configuration even if LDAP authentication is currently disabled. ")
@pass_context
def test(ctx, username, password, ldap_configuration = None):
    """The TestLdapAuthentication is used to verify the currently enabled LDAP authentication configuration settings are correct. If the configuration settings are correct, the API call returns a list of the groups the tested user is a member of."""
    TestLdapAuthenticationResult = ctx.element.test_ldap_authentication(username=username, password=password, ldap_configuration=ldap_configuration)
    print(json.dumps(json.loads(jsonpickle.encode(TestLdapAuthenticationResult)),indent=4))

