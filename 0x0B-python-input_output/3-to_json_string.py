#!/usr/bin/python3

"""Working with JSON objects"""

import json


def to_json_string(my_obj):
    """Convert object to JSON string

    Args:
        my_obj (any): The object to Convert

    Return:
        (str): Object's JSON string representation
    """
    return (json.dumps(my_obj))
