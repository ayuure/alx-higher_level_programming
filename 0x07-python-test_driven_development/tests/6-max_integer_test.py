#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for test"""
    def test_MaxInger(self):
        """Test for max int"""
        result = max_integer([1, 5, 10, 3, 6])
        self.assertEqual(result, 10)

    def test_negative(self):
        """Test with negative"""
        result = max_integer([-1, -3, -6])
        self.assertEqual(result, -1)

    def test_onevalue(self):
        """Test with one value"""
        result= max_integer([0])
        self.assertEqual(result, 0)

    def test_none(self):
        """Test by passing no value"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_withNoneInt(self):
        """Test by passing a string"""
        val = [1,3,4,5, "hi", 3, 6]
        with self.assertRaises(TypeError):
            max_integer(val)


if __name__ == '__main__':
    unittest.main()