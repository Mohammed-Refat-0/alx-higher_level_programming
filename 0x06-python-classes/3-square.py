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
            TypeError:
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            elif type(size) is not int:
                raise TypeError("size must be an integer")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = size

        def area(self):
            """calcalute square area
            Returns:
                _type_: int area of sqaure
            """
            return self.size ** 2
