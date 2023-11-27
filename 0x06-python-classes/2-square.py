#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A Square class"""
    """attrubites: size"""

    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = size
