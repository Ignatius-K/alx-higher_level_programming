#!/usr/bin/python3

"""Define a self-validating sqaure"""


class Square:
    """Self-validating square"""

    def __init__(self, size: int = 0, position=(0, 0)):
        """create square

        Args:
            size: square size
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """access square position"""
        return self.__position

    @position.setter
    def position(self, position):
        """set the square position

        Args:
            position (int, int): square position
        """
        if not (isinstance(position, tuple)
                and all(isinstance(coord, int) for coord in position)
                and all(coord >= 0 for coord in position)
                and len(position) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self) -> float:
        """area of the square

        Return:
            area of square
        """
        return (self.__size ** 2)

    def my_print(self) -> None:
        """modified print"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
