#!/usr/bin/python3
"""
This module provides utility functions for handling data.
"""
class Square:
    def __init__(self, size = 0):
        """
        A class for representing the calculation of area of a square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")