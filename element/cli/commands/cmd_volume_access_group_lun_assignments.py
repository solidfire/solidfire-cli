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

@cli.command('modify', short_help="ModifyVolumeAccessGroupLunAssignments")
@click.option('--volume_access_group_id',
              type=int,
              required=True,
              help="Unique volume access group ID for which the LUN assignments will be modified. ")
@click.option('--lun_assignments',
              type=LunAssignment,
              required=True,
              help="The volume IDs with new assigned LUN values. ")
@pass_context
def modify(ctx, volume_access_group_id, lun_assignments):
    """The ModifytVolumeAccessGroupLunAssignments is used to define custom LUN assignments for specific volumes. Only LUN values set on the lunAssignments parameter will be changed in the volume access group. All other LUN assignments will remain unchanged."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """LUN assignment values must be unique for volumes in a volume access group. An exception will be seen if LUN assignments are duplicated in a volume access group. However, the same LUN values can be used again in different volume access groups."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Note:&lt;/b&gt; Correct LUN values are 0 - 16383. An exception will be seen if an incorrect LUN value is passed. None of the specified LUN assignments will be modified if there is an exception."""
    """&lt;br/&gt;&lt;br/&gt;"""
    """&lt;b&gt;Caution:&lt;/b&gt; If a LUN assignment is changed for a volume with active I/O, the I/O could be disrupted. Changes to the server configuration may be required in order to change volume LUN assignments."""
    ModifyVolumeAccessGroupLunAssignmentsResult = ctx.element.modify_volume_access_group_lun_assignments(volume_access_group_id=volume_access_group_id, lun_assignments=lun_assignments)
    print(json.dumps(json.loads(jsonpickle.encode(ModifyVolumeAccessGroupLunAssignmentsResult)),indent=4))

