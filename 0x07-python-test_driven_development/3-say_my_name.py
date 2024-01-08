#!/usr/bin/python3
"""
say my name say my name
"""


def say_my_name(first_name, last_name=None):
    """say my name prints out names"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if last_name is not None and not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    
    if last_name is None:
        last_name = ""

    print('My name is {} {}'.format(first_name, last_name))
