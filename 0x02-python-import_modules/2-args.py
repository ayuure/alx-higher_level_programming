#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    
    if length == 0:
        print("0 arguments.")

    elif length == 1:
        print('1 argument: {}'.format(sys.argv[1]))

    elif length > 1:
        for i in range (length):
            print('{}: {}'.format(i,sys.argv[i]))
