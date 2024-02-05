#!/usr/bin/python3
"""This is a base class"""


class BaseGeometry():
    """class for bassGeo"""
    def area(self):
        """area of baseGeo"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validator for integer"""
        if not isinstance(value, int):
            raise TypeError('{:s} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
