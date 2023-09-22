#!/usr/bin/python3
"""
Unit tests for the Base class.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_id_assignment(self):
        """
        Test if the IDs are assigned correctly when creating Base instances.
        """
        # Create instances of Base with and without explicit IDs
        obj1 = Base()
        obj2 = Base(42)

        # Check if the IDs were assigned correctly
        self.assertEqual(obj1.id, 1, "First object should have ID 1")
        self.assertEqual(obj2.id, 42, "Second object should have ID 42")

if __name__ == '__main__':
    unittest.main()

