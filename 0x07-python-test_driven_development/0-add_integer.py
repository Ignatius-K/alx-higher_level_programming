#!/usr/bin/python3

"""Arithmetic module

    Methods:
        add_integer
"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: the first integers
        b: the second integers

    Return:
        (int) sum of a and b
    """
    return (check_and_validate(a, 'a') + check_and_validate(b, 'b'))


def check_and_validate(arg, arg_name):
    """Checks the argument

        Args:
            arg (any): argument to validate

        Return:
            validated argument

        Raises:
            TypeError: if argument not int or float
    """
    if not (isinstance(arg, int) or isinstance(arg, float)):
        raise TypeError(f"{arg_name} must be an integer")
    return (int(arg))
