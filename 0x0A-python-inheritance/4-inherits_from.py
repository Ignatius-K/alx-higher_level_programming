#!/usr/bin/python3

"""Module defines util checking object instantiation"""


def inherits_from(obj, a_class):
    """check if object's class is subclass of a class

    Args:
        obj: The object
        a_class: The class

    Return:
        True: If obj's class is subclass of a_class
        False: Otherwise
    """
    type_of_obj = type(obj)
    if issubclass(type_of_obj, a_class) and (type_of_obj is not a_class):
        return (True)
    return (False)
