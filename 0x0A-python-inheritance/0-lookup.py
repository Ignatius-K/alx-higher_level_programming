#!/usr/bin/python3

"""Module defining a util function ``lookup`` """


def lookup(obj):
    """lookup

    Args:
        obj: Any object

    Return:
        obj's attributes
    """
    return (obj.__dir__())

