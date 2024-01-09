#!/usr/bin/python3
"""
This is a function
"""


def class_to_json(obj):
    """this is a function for something"""
    if not hasattr(object, '__dict__'):
        raise ValueError('Object is not an instance of a class')
    
    result = {}

    for key, value in obj.__dict__.items():
        if isinstance (value, (list, dict, str, int, bool)):
            result[key] = value
    
    return result