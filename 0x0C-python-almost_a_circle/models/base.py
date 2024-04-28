#!/usr/bin/python3

"""Define the Base Type"""


class Base:
    """Base Shape"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Create a Base object

        Args:
            id (None | int): The Id of the object

        Notes:
            - If Id is None, then the object_number is assigned
        """
        if id is not None:
            self.id = id
            return
        self.__class__.__nb_objects += 1
        self.id = self.__class__.__nb_objects

    # def __del__(self):
    #     """Destroy a Base object"""
    #     self.__class__.__nb_objects -= 1
