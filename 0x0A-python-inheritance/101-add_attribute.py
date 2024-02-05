#!/usr/bin/python3

def add_attr(obj, attribute, value):
    """
    function to add attribute when called
    obj (any): The object to add an attribute to.
    attribute (str): The name of the attribute to add to obj.
    value (any): The value of att.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
