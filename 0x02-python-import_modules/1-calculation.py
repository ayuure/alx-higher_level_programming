#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calFunc
    """print various things"""
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calFunc.add(a, b)))
    print("{} - {} = {}".format(a, b, calFunc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calFunc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calFunc.div(a, b)))
