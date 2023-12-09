#!/usr/bin/python3
"""contain Rectangle class
"""

from base import Base


class Rectangle(Base):
    """Rectangle class inherit from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """getter for area of rectangle
        Returns:
            area
        """
        return (self.__height * self.__width)

    def display(self):
        """print rectangle with  '#' char in stdout
        """
        for k in range(self.y):
            print('')
        if self.area == 0:
            print('')
        else:

            for i in range(self.height):
                print(' ' * self.x, end='')
                print('#' * self.width, end='')
                print('')

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    @property
    def width(self):
        """
            getter function for __width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for width.
            Args:
                value (int)
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for __height
        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height
        Args:
            value (int): int, grater than zero
        Raises:
            TypeError:
            ValueError:
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

        @property
        def x(self):
            """getter for x
            Returns:
                x
            """
            return self.__x

        @x.setter
        def x(self, value):
            """setter for x
            Args:
                value (int): grater than or equal zero
            Raises:
                TypeError:
                ValueError:
            """
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """getter for y
            Returns:
                y
            """
            return self.__y

        @y.setter
        def y(Self, value):
            """setter for y
            Args:
                value (int): grater than or equal zero
            Raises:
                TypeError:
                ValueError:
            """
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
