#!/usr/bin/python3
"""contain Square class
"""

from models.base import Rectangle


class Rectangle(Base):
    """Square class inherit from Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor for square
        """
        super().__init__(id, size, x, y)

    @property
    def size(self):
        """
            returns the size square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            setter for size
        """
        self.width = value
        self.height = value
