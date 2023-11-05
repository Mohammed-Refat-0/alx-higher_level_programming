#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = ()
    value = 0
    for i in 1:
        if tuple_a(i):
            value = value + tuple_a(i)
        if tuple_b(i):
            value = value + tuple_b(i)
        new.append(value)
        value = 0
    return new
