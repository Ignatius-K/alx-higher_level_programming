#!/usr/bin/python3

'''Rectangle module'''


class Rectangle:
    '''Define Rectangle

    Args:
        number_of_instances (int): Rectangle instances
        print_symbol (any): symbol to print rectangle
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width: int = 0, height: int = 0):
        '''Initialize new Rectangle

        Note:
            Keep count of the rectangle instances

        Args:
            width (default = 0): width of Rectangle
            height (default = 0): height of Rectangle
        '''
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """gets bigger rectangle

        Note:
            If both rectangles are equal, first rectangle is returned

        Args:
            rect_1: first rectangle
            rect_2: second rectangle

        Return:
            rectangle: bigger rectange
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

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
        return (2 * (self.__height + self.__width))

    def __str__(self) -> str:
        """retangle representation

        Note:
            if width or height is 0, then representation is ""

        Return:
            str: rectangle representation
        """
        if self.__height == 0 or self.__width == 0:
            return ""
        repr = ""
        for i in range(self.__height):
            repr += str(self.print_symbol) * self.__width
            if (i < self.__height - 1):
                repr += "\n"
        return (repr)

    def __repr__(self):
        """rectangle dev representation

        Return:
            str: string repr
        """
        return f"Rectangle({self.__width:d}, {self.__height:d})"

    def __del__(self):
        """deletes a rectangle

        Note:
            prints Bye message
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
