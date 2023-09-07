#!/usr/bin/python3

"""Unittest for max_integer([..])

"""

import unittest
from my_module import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 5, 8, 12]), 12)
        self.assertEqual(max_integer([100, 200, 50, 75]), 200)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-10, -5, -8, -12]), -5)
        self.assertEqual(max_integer([-100, -200, -50, -75]), -50)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3]), 2)
        self.assertEqual(max_integer([10, -5, 8, -12]), 10)
        self.assertEqual(max_integer([-100, 200, -50, 75]), 200)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([3, 1, 3, 2]), 3)

if __name__ == '__main__':
    unittest.main()
