#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    str1 = ""
    for c in str:
        if i == n:
            i += 1
        else:
            str1 = str1 + c
            i += 1
    return str1
