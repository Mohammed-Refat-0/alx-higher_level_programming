#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = mylist[0]
    for i in range(len(my_list)):
        if i > max:
            max = i
    return max