#!/usr/bin/python3
"""append text to a file"""


def append_write(filename="", text=""):
    """Function to append text to a file"""
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
    with open(filename, mode='r', encoding='utf-8') as f:
        return len(f.read())