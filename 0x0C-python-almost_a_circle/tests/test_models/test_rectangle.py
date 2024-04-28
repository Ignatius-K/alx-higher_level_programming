#!/usr/bin/python3

"""Test module for Rectangle"""

import unittest
import random
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle test case"""

    @classmethod
    def setUpClass(cls):
        cls.args = (3, 4)
        cls.kwargs = {"x": 2, "y": 4}

    def test_is_rectangle_created_with_width_and_height(self):
        """Test if rectangle is created with width and height"""
        rectangle = Rectangle(*self.args)
        self.assertEqual(rectangle.width, self.args[0])

    def test_is_created_with_x_and_y_coords(self):
        """Rectangle created with x and y coords"""
        rectangle = Rectangle(*self.args, **self.kwargs)
        self.assertEqual(rectangle.x, self.kwargs['x'])
        self.assertEqual(rectangle.y, self.kwargs['y'])

    def test_if_rectangle_can_be_given_id(self):
        """Rectangle object given an Id"""
        assigned_id = random.randint(111, 1111)
        rectangle = Rectangle(*self.args, id=assigned_id)
        self.assertEqual(rectangle.id, assigned_id)
