#!/usr/bin/python3

"""Module defining util for checking if obj is exactly instance of a class"""


def is_same_class(obj, a_class):
    """check if obj is instance of a_class

    Args:
        obj: Instantiated object
        a_class: Class we are checking

    Return:
        True if obj is instance of a_class else False
    """
    return (True if isinstance(obj, a_class) else False)
