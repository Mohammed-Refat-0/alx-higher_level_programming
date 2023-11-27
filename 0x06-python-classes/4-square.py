#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A Square class"""

    def __init__(self, size=0):
        """
        Args:
            size (int, optional): size of square. Defaults to 0.

        Raises:
            ValueError: if value < 0
            TypeError: if type not int
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """calcalute square area
        Returns:
            _type_: int area of sqaure
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
