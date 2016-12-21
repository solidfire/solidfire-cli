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

@cli.command('get', short_help="GetVirtualVolumeUnsharedChunks")
@click.option('--virtual_volume_id',
              type=UUID,
              required=True,
              help="The ID of the Virtual Volume. ")
@click.option('--base_virtual_volume_id',
              type=UUID,
              required=True,
              help="The ID of the Virtual Volume to compare against. ")
@click.option('--segment_start',
              type=int,
              required=True,
              help="Start Byte offset. ")
@click.option('--segment_length',
              type=int,
              required=True,
              help="Length of the scan segment in bytes. ")
@click.option('--chunk_size',
              type=int,
              required=True,
              help="Number of bytes represented by one bit in the bitmap. ")
@click.option('--calling_virtual_volume_host_id',
              type=UUID,
              required=False,
              help="")
@pass_context
def get(ctx, virtual_volume_id, base_virtual_volume_id, segment_start, segment_length, chunk_size, calling_virtual_volume_host_id = None):
    """GetVirtualVolumeAllocatedBitmap scans a VVol segment and returns the number of """
    """chunks not shared between two volumes. This call will return results in less """
    """than 30 seconds. If the specified VVol and the base VVil are not related, an """
    """error is thrown. If the offset/length combination is invalid or out fo range """
    """an error is thrown."""
    VirtualVolumeUnsharedChunkResult = ctx.element.get_virtual_volume_unshared_chunks(virtual_volume_id=virtual_volume_id, base_virtual_volume_id=base_virtual_volume_id, segment_start=segment_start, segment_length=segment_length, chunk_size=chunk_size, calling_virtual_volume_host_id=calling_virtual_volume_host_id)
    print(json.dumps(json.loads(jsonpickle.encode(VirtualVolumeUnsharedChunkResult)),indent=4))

