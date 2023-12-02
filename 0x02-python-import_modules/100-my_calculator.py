#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    if len(sys.argv) -1 != 3:
        print('{} <a> <operator> <b>'.format(sys.argv[0]))