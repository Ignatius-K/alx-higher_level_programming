#!/usr/bin/python3

"""Working with files"""

import json


def from_json_string(my_str=""):
    """Convert JSON string to object

    Args:
        my_str (str): The JSON string to Convert

    Return:
        (any): The object
    """
    return (json.loads(my_str))
