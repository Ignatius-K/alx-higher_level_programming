#!/usr/bin/python3

def islower(c):
    """
    check if c is lowercase

    Parameters:
        c (str): one-character string

    Return:
        True if c is lowercase else False
    """

    if (ord(c) > 96) and (ord(c) < 123):
        return True
    return False
