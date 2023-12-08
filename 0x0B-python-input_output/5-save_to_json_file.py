#!/usr/bin/python3
"""save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation:

    Args:
        my_obj (_type_): python object
        filename (_type_): file object
    """
    json_str = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(json_str)
