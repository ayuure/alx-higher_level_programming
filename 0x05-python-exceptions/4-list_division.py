#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    arr = []
    for i in range(list_length):
        try:
            arr.append(my_list_1[i]/my_list_2[i])
        except ZeroDivisionError:
            print( "division by 0")
            arr.append(0) 
        except TypeError:
            print("wrong type")
            arr.append(0)
        except IndexError:
            print("out of range")
            arr.append(0)    
    return arr