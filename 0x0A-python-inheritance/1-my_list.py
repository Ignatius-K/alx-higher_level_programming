#!/usr/bin/python3

"""Module defining a modified list"""


class MyList(list):
    """MyList

    Desc:
        Modifies Python's List
    """

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
