#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in a_dictionary:
        if i == key:
            a_dictionary[i] = value
        if i != key:
            a_dictionary[key] = value
    for x,y in a_dictionary.items():
        print('{}: {}'.format(x, y))