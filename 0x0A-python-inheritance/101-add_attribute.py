#!/usr/bin/python3

def add_attr(obj, attribute, value):
    """function to add attribute when called"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)