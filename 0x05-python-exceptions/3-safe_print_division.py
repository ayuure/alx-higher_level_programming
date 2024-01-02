#!/usr/bin/python3
def safe_print_division(a, b):
    sum = 0
    try:
        sum = a / b
    except ZeroDivisionError:
        sum = None
    finally:
        print("Inside result: {:d}".format(sum))
    return sum
