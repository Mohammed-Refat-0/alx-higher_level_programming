#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_tuple = ()
    for i in range(2):
        val_a = tuple_a[i] if i < len(tuple_a) else 0 + tuple_b[i] if i < len(tuple_b) else 0
        val_b = tuple_b[i] if i < len(tuple_b) else 0 + tuple_a[i] if i < len(tuple_a) else 0
        sum_tuple += (val_a, val_b)
    return sum_tuple
