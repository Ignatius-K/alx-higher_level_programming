#!/usr/bin/python3

"""Working with files"""


def read_file(filename=""):
    """Read a file

    Args:
        filename: The path to the file
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
