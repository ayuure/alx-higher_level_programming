#!/usr/bin/python3
def max_integer(my_list=[]):
    highest = 0
    for i in range(len(my_list)):
        if my_list[i] > highest:
            highest = my_list[i]
    return (highest)
