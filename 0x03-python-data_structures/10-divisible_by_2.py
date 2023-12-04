#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return_list = []
    for items in my_list:
        if items % 2 == 0:
            return_list.append(True)
        else:
            return_list.append(False)
    return (return_list)