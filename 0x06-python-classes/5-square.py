#!/usr/bin/python3

"""Define a self-validating sqaure"""


class Square:
    """Self-validating square"""

    def __init__(self, size: int = 0):
        """create square

        Args:
            size: square size
        """
        self.size = size

    @property
    def size(self) -> int:
        """get size

        Return:
            size of square
        """
        return (self.__size)

    @size.setter
    def size(self, size: int):
        """set square size
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

    def my_print(self) -> None:
        """print my square"""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
        print("")
