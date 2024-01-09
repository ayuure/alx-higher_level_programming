#!/usr/bin/python3
"""
function to load from json
"""

import json


def load_from_json_file(filename):
    """Load and write to file"""
    with open(filename, mode='r', encoding="utf-8") as rf:
        data = json.load(rf)
        return data