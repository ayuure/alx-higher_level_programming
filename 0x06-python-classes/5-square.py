#!/usr/bin/python3
"""
This module provides utility functions for handling data.
"""
class Square:
    """
    A class for representing the calculation of area of a square.
    """
    def __init__(self, size = 0):
        self.__size = size
    @property    
    def size(self):
        """Get the size of the square."""
        return self.__size
    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size
    def my_print(self):
        """Print the square of # characters."""
        if self.__size == 0:
            print()
        theSq = "#" * (self.__size)
        for _ in range (self.__size):
            print(theSq)