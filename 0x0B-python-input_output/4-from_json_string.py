#!/usr/bin/python3
""" from_json_string function
"""
import json


def from_json_string(my_str):
    """ return object data repersentation (python) from json string
    repersentation

    Args:
        my_obj (_type_): json representation
    """
    return (json.loads(my_str))
