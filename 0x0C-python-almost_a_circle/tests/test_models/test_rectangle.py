#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_initialization(self):
        """
        Test if the Rectangle is initialized correctly.
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 1)

    def test_area(self):
        """
        Test if the area() method returns the correct area.
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """
        Test if the display() method prints the rectangle correctly.
        """
        rect = Rectangle(3, 2, 1, 1, 1)
        expected_output = " ###\n ###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        """
        Test if the update() method updates attributes correctly.
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        rect.update(2, 7, 8, 4, 6)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 7)
        self.assertEqual(rect.height, 8)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 6)

    def test_str(self):
        """
        Test if the __str__() method returns the correct string representation.
        """
        rect = Rectangle(5, 10, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_str)

if __name__ == '__main__':
    unittest.main()

