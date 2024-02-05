#!/usr/bin/python3
"""Class for square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """initializes size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def _str_(self):
        """informal string reepresentation of the square"""
        className = self._class.name_
        return "{:s} {:d}/{:d}".format(className, self._size, self._size)
