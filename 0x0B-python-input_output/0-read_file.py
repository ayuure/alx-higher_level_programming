#!/usr/bin/python3
"""
Read content from a file
"""
def read_file(filename=""):
    """Function to read from a file"""
    with open(filename, mode='r', encoding="utf-8") as f:
        f_content = f.read()
        print(f_content, end='')
