#!/usr/bin/python3
"""This is a class"""


class MyInt(int):

    def __int__(self, value):
        self.value =  value
    def __eq__(self, other):
        return self.value != other
    def __ne__(self, other):
        return self.value == other
