#!/usr/bin/python3
"""
Function to retrun to py obj
"""

import json


def from_json_string(my_str):
    """ function for obj"""
    return json.loads(my_str)