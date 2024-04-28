#!/usr/bin/python3

"""Ease working with Classes"""


def class_to_json(obj):
    """Convert class to json

    Args:
        obj (any): The object

    Return:
        (dict): The simple obj representation
    """
    temp_dict = {}
    allowed_types = [int, str, list, dict, bool]

    for attr_name in dir(obj):
        if attr_name.startswith("__"):
            continue
        attr_val = obj.__getattribute__(attr_name)
        if type(attr_val) not in allowed_types:
            continue

        temp_dict[attr_name] = attr_val

    return (temp_dict)


if __name__ == "__main__":
    class MyClass:
        num = 9
        txt = "Hello"
        lst = [2, 4, "fsd", 2.4]

        def __init__(self, num):
            self.__num = num

    myClass = MyClass(90)
    print(class_to_json(myClass))
