#!/usr/bin/python3

"""Module defining util for checking instance of"""


def is_kind_of_class(obj, a_class):
    """check if obj is instance of a_class

    Args:
        obj: object
        a_class: class

    Return:
        True if obj is instance of a_class else False
    """
    return (True if isinstance(obj, a_class) else False)
