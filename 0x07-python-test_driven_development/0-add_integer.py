#!/usr/bin/python3
"""TFunction to add int"""


def add_integer(a, b=98):
    """
    Add inter funtion that adds two float and or int values and returns the result
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')  
    return a + b