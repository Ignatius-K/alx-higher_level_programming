#!/usr/bin/python3

"""Test module for base.py"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test the Base class"""

    def setUp(self):
        self.base = Base()

    def test_if_id_is_assigned(self):
        """Test whether id is assigned"""
        self.assertIsNotNone(self.base.id)

    def test_if_id_is_incremented(self):
        """Test if id increments"""
        base2 = Base()
        self.assertEqual(base2.id - self.base.id, 1)
        del base2

    def test_assigned_id(self):
        """Test assigned Id"""
        assigned_id = 120
        base = Base(assigned_id)
        self.assertEqual(base.id, assigned_id)

    def tearDown(self):
        del self.base
