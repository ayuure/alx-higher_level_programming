#!/usr/bin/python3
"""This is a class"""


class Student():
    """class the converts to a dict"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """filter to make sure attr is in the class"""
        if attrs is None:
            return{
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                    }
        else:
            return{
                attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)
            }
