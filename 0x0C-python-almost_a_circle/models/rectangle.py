#!/usr/bin/python3

"""Rectangle Type"""

from models.base import Base


class Rectangle(Base):
    """Rectangle subclass of Base"""

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
        self.__width = width

    @property
    def height(self):
        """Get height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """Set height"""
        self.__height = height

    @property
    def x(self):
        """Get x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """Set x"""
        self.__x = x

    @property
    def y(self):
        """Get y"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """Assign y"""
        self.__y = y
