#!/usr/bin/python3

"""Define Square"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Implement Square

    Subclass of Rectangle
    """

    def __init__(self, size):
        """Initialize a Square"""
        self.__size = size
        super().__init__(self.__size, self.__size)
