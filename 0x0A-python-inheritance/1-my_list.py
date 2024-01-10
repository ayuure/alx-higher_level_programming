#!/usr/bin/python3
"""
Module 1-my_list
"""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
