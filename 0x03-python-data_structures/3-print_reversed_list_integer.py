#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    for vals in range(len(my_list)):
        print('{}'.format(my_list[i]))
        i = i - 1