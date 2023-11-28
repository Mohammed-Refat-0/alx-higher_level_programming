#!/usr/bin/python3
"""Defines a Recatabgle Square"""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.height = height

    @property
    """width attribuite"""
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    """height attribuite"""
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
