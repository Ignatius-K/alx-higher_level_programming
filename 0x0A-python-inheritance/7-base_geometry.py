#!/usr/bin/python3

"""Defines BaseGeometry type"""


class BaseGeometry:
    """Define BaseGeometry type"""

    def area(self):
        """Do something

        Raises:
            Exception: If area not yet implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name (str): Name of attribute
            value (int): Value of attribute

        Raises:
            TypeError: If ``value`` is not integer
            ValueError: If ``value`` is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
