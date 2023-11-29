#!/usr/bin/python3
def add_integer(a, b=98):
    """function that add two integers

    Args:
        a (int,float): 
        b (int, optional): Defaults to 98.

    Raises:
        TypeError: if a or b not in [int, float] type

    Returns:
        _type_: addition int of a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
