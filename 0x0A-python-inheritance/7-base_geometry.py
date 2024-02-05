#!/usr/bin/python3
"""This is a bass class"""


class BaseGeometry():
    """class for bassGeo"""
    def area(self):
        """area of baseGeo"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validator for integer"""
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        elif value <= 0:
            raise ValueError(name + ' must be greater than 0')
