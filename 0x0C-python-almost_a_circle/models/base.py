#!/usr/bin/python3
"""contain Base class
"""


class Base:
    """base of all other classes in this project.
    to manage id attribute in all future classes
    and to avoid duplicating the same code and bugs
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            __nb_objects = __nb_objects + 1
            self.id = __nb_objects
