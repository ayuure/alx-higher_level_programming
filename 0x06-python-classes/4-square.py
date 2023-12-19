#!/usr/bin/python3
"""
This module provides utility functions for handling data.
"""
class Square:
    """
    A class for representing the calculation of area of a square.
    """
    def __init__(self, size=0):
        self.__size = size
    def size(self):
        """
        A area for representing the calculation of area of a square.
        """
        return self.__size
    def size(self, value):
        """
        A self value method for representing the calculation of area of a square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """
    A area for representing the calculation of area of a square.
    """
        return self.__size * self.__size