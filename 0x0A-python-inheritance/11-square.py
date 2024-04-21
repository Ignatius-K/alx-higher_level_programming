
#!/usr/bin/python3

"""Define Square"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Implement Square

    Subclass of Rectangle
    """

    def __init__(self, size):
        """Initialize a Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Rectangle print format"""
        return (f"[Square] {self.__size}/{self.__size}")
