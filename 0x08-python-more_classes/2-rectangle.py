#!/usr/bin/python3

'''Rectangle module'''


class Rectangle:
    '''Define Rectangle'''

    def __init__(self, width: int = 0, height: int = 0):
        '''Initialize new Rectangle

        Args:
            width (default = 0): width of Rectangle
            height (default = 0): height of Rectangle
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        """get rectangle's width"""
        return (self.__width)

    @width.setter
    def width(self, width: int):
        """Width of an integer

        Args:
            width: width of Rectangle

        Raises:
            TypeError: if width is not integer
            ValueError: if width not >= 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self) -> int:
        """get height of rectangle

        Return:
            int: rectangle's height
        """
        return (self.__height)

    @height.setter
    def height(self, height: int):
        """set height of rectangle

        Args:
            height: height of rectangle

        Raises:
            TypeError: if height not integer
            ValueError: if height not >= 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """calculate area of rectangle

        Return:
            int: area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """claculate perimeter of rectangle

        Note:
            if width or height is 0, then perimeter is 0

        Return:
            int: perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * self.__height * self.__width)
