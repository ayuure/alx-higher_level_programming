#!/usr/bin/python3
"""
Function to write to a file and return the number of charaters
"""


def write_file(filename="", text=""):
    """Function used to write"""
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(text)
    with open(filename, mode='r', encoding="utf-8") as f:
        return len(f.read())
