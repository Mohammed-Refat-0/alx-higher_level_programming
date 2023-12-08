#!/usr/bin/python3
"""load_from_json_file
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
        filename (_type_): json file
    """
    with open(filename, 'r') as f:
        return json.load(f)
