#!/usr/bin/python3
"""Function to check class and subclass"""
def inherits_from(obj, a_class):
    """returns true if it is"""
    return type(obj) is not a_class and issubclass(type(obj), a_class)