#!/usr/bin/python3
def no_c(my_string):
    newString = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        newString = newString + i
    return (newString)