#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list1 = my_list.copy()
    if len(my_list) <= idx or idx < 0:
        return list1
    else:
        list1[idx] = element
        return list1
