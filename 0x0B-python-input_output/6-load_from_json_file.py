#!/usr/bin/python3

"""Working with JSON"""

import json


def load_from_json_file(filename=""):
    """Load object from JSON

    Args:
        filename (str): The path to file

    Return:
        (any): The loaded object
    """
    with open(filename, "r", encoding="utf-8") as fp:
        return (json.load(fp))
