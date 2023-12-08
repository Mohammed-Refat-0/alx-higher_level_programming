#!/usr/bin/python3
""" to_json_string function
"""
import json


def to_json_string(my_obj):
    """ return json repersentation of data

    Args:
        my_obj (_type_): string
    """
    return (json.dumps(my_obj))
