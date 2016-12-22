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

@cli.command('list', short_help="ListEvents")
@click.option('--max_events',
              type=int,
              required=False,
              help="Specifies the maximum number of events to return. ")
@click.option('--start_event_id',
              type=int,
              required=False,
              help="Identifies the beginning of a range of events to return. ")
@click.option('--end_event_id',
              type=int,
              required=False,
              help="Identifies the end of a range of events to return. ")
@click.option('--event_queue_type',
              type=str,
              required=False,
              help="")
@pass_context
def list(ctx, max_events = None, start_event_id = None, end_event_id = None, event_queue_type = None):
    """ListEvents returns events detected on the cluster, sorted from oldest to newest."""
    ListEventsResult = ctx.element.list_events(max_events=max_events, start_event_id=start_event_id, end_event_id=end_event_id, event_queue_type=event_queue_type)
    cli_utils.print_result(ListEventsResult, as_json=ctx.json, depth=ctx.depth, filter_tree=ctx.filter_tree)

