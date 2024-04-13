#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer method

        Note:
            max_integer(element_list: list) -> (int | float)
    """

    def test_not_list(self):
        """Test when element_list is not list type"""

        sample_elements = "Not a list"
        self.assertRaises(TypeError, max_integer(sample_elements))

    def test_empty_list(self):
        """Test when list is empty, expect None"""

        sample_elements = []
        self.assertIsNone(max_integer(sample_elements))

    def test_expected_output(self):
        """Test with sample data"""

        sample_value_elements = {
            1: [1],
            10: [1, 2, 4, 10],
            0.5: [0.1, 0.49, 0.5]
        }
        for (key, value) in sample_value_elements.items():
            self.assertEqual(key, max_integer(value))

    def test_some_elements_not_number(self):
        """Test when some elements not int or float type"""

        sample_value_elements = [23, "Hello", {}]
        with self.assertRaises(TypeError):
            max_integer(sample_value_elements)
