#!/usr/bin/python3

"""Working with files"""


def append_write(filename="", text=""):
    """Append to file

    Args:
        filename (str): The file to append to
        text (str): The text to write

    Return:
        (int): Number of characters written
    """
    with open(filename, "a+", encoding="utf-8"):
        return (f.write(text))
