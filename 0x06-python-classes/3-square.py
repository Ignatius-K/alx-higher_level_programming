#!/usr/bin/python3

"""Define a self-validating sqaure"""


class Square:
    """Self-validating square"""

    def __init__(self, size: int = 0):
        """create square

        Args:
            size: square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> float:
        """area of the square

        Return:
            area of square
        """
        return (self.__size ** 2)
