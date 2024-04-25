#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """ Finds the peak in a list of integers """
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    ma = int(length / 2)
    l = list_of_integers

    if ma - 1 < 0 and ma + 1 >= length:
        return l[ma]
    elif ma - 1 < 0:
        return l[ma] if l[ma] > l[ma + 1] else l[ma + 1]
    elif ma + 1 >= length:
        return l[ma] if l[ma] > l[ma - 1] else l[ma - 1]

    if l[ma - 1] < l[ma] > l[ma + 1]:
        return l[ma]

    if l[ma + 1] > l[ma - 1]:
        return find_peak(l[ma:])
    return find_peak(l[:ma])
