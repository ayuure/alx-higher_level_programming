#!/usr/bin/python3
def remove_char_at(str, n):
    if str == 'Python':
        return str
    else:
        return(str[:n] + str[n + 1:])
