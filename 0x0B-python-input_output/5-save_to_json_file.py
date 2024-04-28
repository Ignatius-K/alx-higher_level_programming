#!/usr/bin/python3

"""Working with JSON"""

import json


def save_to_json_file(my_obj, filename):
    """Save obj to JSON file

    Args:
        my_obj (any): The object to Save
        filename (str): The path to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
