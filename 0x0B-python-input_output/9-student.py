#!/usr/bin/python3
"""This is a class"""

class Student():
    """Student class to is converted to json"""
    first_name = ''
    last_name = ''
    age = 0
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Serization function"""
        return{
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
            }