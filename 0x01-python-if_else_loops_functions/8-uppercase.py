#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        val = ord(str[i])
        if 97 <= val < 123:
            val = val - 32
        print("{:c}".format(val), end='')
