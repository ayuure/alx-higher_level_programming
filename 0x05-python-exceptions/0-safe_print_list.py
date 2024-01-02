#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    val = 0
    try:
        for i in range(x):
            print('{}'.format(my_list[i]), end='')
            val += 1
    except IndexError:
        pass
    print('')
    return val
