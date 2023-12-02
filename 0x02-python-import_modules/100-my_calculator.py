#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    if len (sys.argv) -1 != 3:
        print('Usage: {} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)

    elif sys.argv[2] in {"+", "-", "*", "/"}:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if sys.argv[2] == "+":
            print('{} + {} = {}'.format(a, b, add(a, b)))

        elif sys.argv[2] == "-":
            print('{} + {} = {}'.format(a, b, sub(a, b)))

        elif sys.argv[2] == "*":
            print('{} + {} = {}'.format(a, b, sub(a, b)))

        elif sys.argv[2] == "/":
            print('{} + {} = {}'.format(a, b, sub(a, b)))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)