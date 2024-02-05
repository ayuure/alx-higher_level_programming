#!/usr/bin/python3
"""This is a bass class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class for bassGeo"""
    def __init__(self, width, height):
        """init method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area method"""
        return self.__width * self.__height

    def __str__(self):
        """str to print out"""
        className = self.__class__.__name__
        return '[{:s}] {:d}/{:d} '.format(className, self.__width, self.__height)
