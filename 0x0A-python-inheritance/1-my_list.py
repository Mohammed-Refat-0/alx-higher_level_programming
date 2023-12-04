#!/usr/bin/python3
"""
contains MyList class
"""


class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """prints sorted list in ascending order"""
        print(sorted(self))
