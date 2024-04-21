#!/usr/bin/python3

"""Define Rectangle geometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle

    Sub-class of BaseGeometry
    """

    def __init__(self, width, height):
        """Validates and initializes Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Print rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculate area of rectangle"""
        return (self.__height * self.__width)
