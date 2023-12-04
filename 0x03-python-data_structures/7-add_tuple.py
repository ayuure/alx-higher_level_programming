#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = [0,0]
    j = [0,0]
    sum1 = 0
    sum2 = 0
    if len(tuple_a) == 1:
        i[0] = tuple_a[0]
    if len(tuple_a) >= 2:
        i[0] = tuple_a[0]
        i[1] = tuple_a[1]
    if len(tuple_a) == 2:
        i[0] = tuple_a[0]
        i[1] = tuple_a[1]
    if len(tuple_b) == 1:
        j[0] = tuple_b[0]
    if len(tuple_b) >= 2:
        j[0] = tuple_b[0]
        j[1] = tuple_b[1]
    if len(tuple_b) == 2:
        j[0] = tuple_b[0]
        j[1] = tuple_b[1]
    
    sum1 = i[0] + j[0]
    sum2 = i[1] + j[1]
    new_tuple = (sum1, sum2)
    return (new_tuple)