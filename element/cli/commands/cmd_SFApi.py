#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright &copy; 2014-2016 NetApp, Inc. All Rights Reserved.
#
# DO NOT EDIT THIS CODE BY HAND! It has been generated with jsvcgen.
#

import click

from element.cli import utils as cli_utils
from element.cli import parser
from element.cli.cli import pass_context
from element.solidfire_element_api import SolidFireRequestException
from element import utils
import jsonpickle
import simplejson
from solidfire.models import *
from uuid import UUID
from element import exceptions


@click.group()
@pass_context
def cli(ctx):
    """Invoke """

@cli.command('Invoke', short_help="""This will invoke any API method supported by the SolidFire API for the version and port the connection is using. Returns a nested hashtable of key/value pairs that contain the result of the invoked method. """)
@click.option('--method',
              type=str,
              required=True,
              help="""The name of the method to invoke. This is case sensitive. """)
@click.option('--parameters',
              type=str,
              required=False,
              help="""Provide in json format: An object, normally a dictionary or hashtable of the key/value pairs, to be passed as the params for the method being invoked. """)
@pass_context
def Invoke(ctx,
           method,
           parameters = None):
    """This will invoke any API method supported by the SolidFire API for the version and port the connection is using."""
    """Returns a nested hashtable of key/value pairs that contain the result of the invoked method."""
    if ctx.element is None:
         raise exceptions.SolidFireUsageException("You must establish at least one connection and specify which you intend to use.")


    if(parameters is not None):
        kwargsDict = simplejson.loads(parameters)
        parameters = dict(**kwargsDict)

    str = ctx.element.invoke_sfapi(method=method, parameters=parameters)
    cli_utils.print_result(str, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

