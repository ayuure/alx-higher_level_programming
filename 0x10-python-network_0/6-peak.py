#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    ma = int(length / 2)
    la = list_of_integers

    if ma - 1 < 0 and ma + 1 >= length:
        return la[ma]
    elif ma - 1 < 0:
        return la[ma] if la[ma] > la[ma + 1] else la[ma + 1]
    elif ma + 1 >= length:
        return la[ma] if la[ma] > la[ma - 1] else la[ma - 1]

    if la[ma - 1] < la[ma] > la[ma + 1]:
        return la[ma]

    if la[ma + 1] > la[ma - 1]:
        return find_peak(la[ma:])
    return find_peak(la[:ma])
