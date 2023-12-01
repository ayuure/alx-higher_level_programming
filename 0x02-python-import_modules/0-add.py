#!/usr/bin/python3
""" use import to print out values
    format the int to strings
    """
import add_0
if __name__ == "__main__":
    a = 1
    b =2

    results = add_0.add(a,b)
    
    print("{} + {} = {}".format(a,b,results)+"\n")
