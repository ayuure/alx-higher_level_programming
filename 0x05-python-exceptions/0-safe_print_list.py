#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    i = 0
    num = 0

    for vals in my_list:
        length += 1

    try:
        while x > 0:
            num *= 10
            x -= 1
            num += my_list[i]
            i += 1
    except Exception:
        i = 0
        num = 0
        while i < length:
            num = num * 10
            num += my_list[i]
            i += 1
    return num