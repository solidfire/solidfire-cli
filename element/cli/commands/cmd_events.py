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

@click.group()
@pass_context
def cli(ctx):
    """Account methods."""
    ctx.sfapi = ctx.client

@cli.command('list', short_help="ListEvents")
@click.argument('max_events', type=int, required=False)
@click.argument('start_event_id', type=int, required=False)
@click.argument('end_event_id', type=int, required=False)
@click.argument('event_queue_type', type=str, required=False)
@pass_context
def list(ctx, max_events = None, start_event_id = None, end_event_id = None, event_queue_type = None):
    """ListEvents returns events detected on the cluster, sorted from oldest to newest."""
    ListEventsResult = ctx.element.list_events(max_events=max_events, start_event_id=start_event_id, end_event_id=end_event_id, event_queue_type=event_queue_type)
    print(ListEventsResult)

