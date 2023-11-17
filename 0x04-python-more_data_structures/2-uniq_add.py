#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique_list = my_list.copy()
    unique_list = list(set(unique_list))
    for i in unique_list:
        sum = sum + i
    return sum
