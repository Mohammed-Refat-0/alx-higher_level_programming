#!/usr/bin/python3
"""is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from
    Args:
        obj (object)
        a_class (class)

    Returns:
        boolean
    """
    return (isinstance(obj, a_class))
