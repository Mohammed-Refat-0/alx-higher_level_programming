#!/usr/bin/python3
def find_peak(list_of_integers):
    if list_of_integers is None:
        return None
    sorted_list = list_of_integers.sort(descending=True)
    return sorted_list[0]
