#!/usr/bin/python3

"""Rectangle Type"""

from models.base import Base


class Rectangle(Base):
    """Rectangle subclass of Base"""

    __display_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates a Rectangle

        Args:
            width (int): The rectangle width
            height (int): The rectangle height
            x (int)
            y (int)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """Set width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """Set height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """Set x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get y"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """Assign y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """calculate rectangle area"""
        return (self.__width * self.__height)

    def display(self):
        """Display rectangle"""
        for row in range(self.__height):
            for column in range(self.__width):
                print(self.__display_symbol, end="")
            print("")
