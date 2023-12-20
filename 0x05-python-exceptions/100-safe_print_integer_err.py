#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise ValueError("Exception: Unknown format code 'd' for object of type 'str'")
    except ValueError:
        return False
