#!/usr/bin/python3

"""Module defines util checking object instantiation"""


def inherits_from(obj, a_class):
    """check if object's class is subclass of a class

    Args:
        obj: The object
        a_class: The class

    Return:
        True if obj's class is subclass of a_class else False
    """
    return (True if issubclass(type(obj), a_class) else False)
