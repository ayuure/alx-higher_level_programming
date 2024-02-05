#!/usr/bin/python3
"""This is a class"""


class MyInt(int):
    """+My int flips the logic of == and !="""
    def __init__(self, value):
        """ init method"""
        self.value = value

    def __eq__(self, other):
        """equal to method changed to !="""
        return self.value != other

    def __ne__(self, other):
        """not equal to method shanged to =="""
        return self.value == other
