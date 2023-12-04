#!/usr/bin/python3
"""
Contains lookup function
"""


def lookup(obj):
    """return list of all attribuites of an objet

    Args:
        obj (object):

    Returns:
        list
    """
    return dir(obj)
