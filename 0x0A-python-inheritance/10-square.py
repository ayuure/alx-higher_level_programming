#!/usr/bin/python3
"""Class for square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""

    def _init_(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super()._init_(size, size)

    def area(self):
        """ "returns the area of the square"""
        return self.__size**2

    def _str_(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self._size, self._size)
