#!/usr/bin/python3

"""Working with files"""


def write_file(filename="", text=""):
    """Write to a file

    Args:
        filename (str): The path to file
        text (str): The text to write to file

    Return:
        (int): Number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
