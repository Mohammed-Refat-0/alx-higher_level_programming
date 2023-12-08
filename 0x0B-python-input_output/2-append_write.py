#!/usr/bin/python3
"""append_write function
"""


def append_write(filename="", text=""):
    """append file with text, and return number of written chars

    Args:
        filename (str, optional): file object
        text (str, optional): string

    Returns:
        _type_: number of written chars
    """
    with open(filename, 'a') as f:
        return (f.write(text))
