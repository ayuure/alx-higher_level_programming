#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    num = 0
    length = 0
    lenghtx = 0
    xval = x
    for val in my_list:
        length += 1
    try:
        lenghtx = x
        while x > 0:
            x -= 1
            num *= 10
            num += my_list[i]
            i += 1
        print("{}".format(num))
    except TypeError:
        i = 0
        num = 0
        lenghtx = 0
        while xval > 0:
            if isinstance(my_list[i], int):
                lenghtx += 1
                num *= 10
                num += my_list[i]
            i += 1
            xval -= 1
        print("{}".format(num))
    return lenghtx

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))