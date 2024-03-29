#!/usr/bin/python3
"""
This is a class
"""


class Student():
    """
    class the converts to a dict
    """
    def __init__(self, first_name, last_name, age):
        """
        initilization function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        filter to make sure attr is in the class
        """

        if attrs is None:
            return self.__dict__
        else:
            return{attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        changing the attr
        """
        for key, value in json.items():
            setattr(self, key, value)
