#!/usr/bin/python3
"""
Test with negative
"""


def text_indentation(text):
    """print a text on separate line when the following are encountered(. ? :)"""
    before =''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in text:
        before += i
        for j in ['.', '?', ':']:
            if i == j:
                print(before)
                print("")
                print("")
                before = ''