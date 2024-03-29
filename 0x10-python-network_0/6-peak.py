#!/usr/bin/python3
"""contains find_peak fn"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if list_of_integers is None or list_of_integers == []:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
