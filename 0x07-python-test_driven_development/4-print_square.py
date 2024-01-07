#!/usr/bin/python3
"""
print square
"""


def print_square(size):
    """print a square n number of times"""
    if size < 0:
        raise ValueError('size must be >= 0')
    if not isinstance(size, (int, float)):
        raise TypeError('size must be an integer')
    s = "#"
    for i in range(size):
        print(s *size)