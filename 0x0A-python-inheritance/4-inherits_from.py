#!/usr/bin/python3
"""inherits_from
"""


def inherits_from(obj, a_class):
    """  returns True if the object is an instance of a class that
    inherited from the specified class
    Args:
        obj (object)
        a_class (class)

    Returns:
        boolean
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
