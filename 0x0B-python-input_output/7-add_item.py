#!/usr/bin/python3

"""Working with JSON"""

import sys
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

filename = "add_item.json"

if __name__ == "__main__":
    temp_container = []
    for (index, arg) in enumerate(sys.argv):
        if index == 0:
            continue
        temp_container.append(arg)

    try:
        saved_list = load_from_json_file(filename)
    except FileNotFoundError:
        saved_list = []

    saved_list.extend(temp_container)
    save_to_json_file(saved_list, filename)
