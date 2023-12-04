#!/usr/bin/python3
def lookup(obj):
    """A function that returns all avaliable attributes of an object

    Args:
        obj (object)

    Returns:
         list: list o an objects's attributes
    """
    return dir(obj)
