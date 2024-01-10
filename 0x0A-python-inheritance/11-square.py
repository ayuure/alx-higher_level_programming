#!/usr/bin/python3
"""This is a class for square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size):
        """initializes size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

def __str__(self):
    """print out format"""
    return('[{:s}] {:d}/{:d}'.format(self.__class__.__name__, self.__size, self.__size))