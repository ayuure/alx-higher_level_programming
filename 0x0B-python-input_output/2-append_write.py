#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
    with open(filename, mode='r', encoding='utf-8') as f:
        return len(f.read())