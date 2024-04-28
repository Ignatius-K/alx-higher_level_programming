#!/usr/bin/python3

"""Define Student Type"""


class Student:
    """The Student"""

    def __init__(self, first_name, last_name, age):
        """Create a Student

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert self to JSON

        Args:
            attrs (list<str> | None): List of required attributes

        Return:
            (dict): The obj's dict representation
        """
        temp_dict = {}
        allowed_types = [int, bool, str, list, dict]

        for attr_name in dir(self):
            if attr_name.startswith("__"):
                continue
            attr_val = self.__getattribute__(attr_name)
            if type(attr_val) not in allowed_types:
                continue
            if type(attrs) is list:
                if attr_name not in attrs:
                    continue
            temp_dict[attr_name] = attr_val

        return (temp_dict)

    def reload_from_json(self, json: dict):
        """Update instance based on JSON

        Args:
            json (dict): The updated attributes
        """
        for attr_name, attr_val in json.items():
            self.__setattr__(attr_name, attr_val)
