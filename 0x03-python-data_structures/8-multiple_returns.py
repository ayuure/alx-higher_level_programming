#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    firstChar = ''
    if len(sentence) == 0:
        return ((None))
    else:
        length = len(sentence)
        firstChar = sentence[:1]
    return ((length, firstChar))