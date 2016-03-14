#!/usr/bin/env/python

import re


def string_to_bytes(val):
    """Converts a string with suffix to integer/bytes."""
    conversion_map = {'Gi': 1024 ** 3, 'Ti': 1024 ** 4,
                      'G': 1000 ** 3, 'T': 1000 ** 4,
                      'GB': 1000 ** 3, 'TB': 1000 ** 4}
    if val.isdigit():
        return val

    parsed_val = filter(None, re.split(r'(\d+)', val))
    if len(parsed_val) != 2:
        raise
    if parsed_val[1] in conversion_map.keys():
        return int(parsed_val[0]) * conversion_map[parsed_val[1]]
    else:
        raise


def kv_string_to_dict(kv_string):
    new_dict = {}
    items = kv_string.split(',')
    for item in items:
        kvs = item.split('=')
        new_dict[kvs[0]] = kvs[1]
    return new_dict
