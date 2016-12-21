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

@cli.command('set', short_help="SetSnmpTrapInfo")
@click.argument('trap_recipients', type=SnmpTrapRecipient, required=True)
@click.argument('cluster_fault_traps_enabled', type=bool, required=True)
@click.argument('cluster_fault_resolved_traps_enabled', type=bool, required=True)
@click.argument('cluster_event_traps_enabled', type=bool, required=True)
@pass_context
def set(ctx, trap_recipients, cluster_fault_traps_enabled, cluster_fault_resolved_traps_enabled, cluster_event_traps_enabled):
    """SetSnmpTrapInfo is used to enable and disable the generation of SolidFire SNMP notifications (traps) and to specify the set of network host computers that are to receive the notifications. The values passed with each SetSnmpTrapInfo method replaces all values set in any previous method to SetSnmpTrapInfo."""
    SetSnmpTrapInfoResult = ctx.element.set_snmp_trap_info(trap_recipients=trap_recipients, cluster_fault_traps_enabled=cluster_fault_traps_enabled, cluster_fault_resolved_traps_enabled=cluster_fault_resolved_traps_enabled, cluster_event_traps_enabled=cluster_event_traps_enabled)
    print(SetSnmpTrapInfoResult)

