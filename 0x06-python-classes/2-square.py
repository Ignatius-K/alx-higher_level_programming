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
            raise ValueError("Size must be >= 0")
        self.__size = size
