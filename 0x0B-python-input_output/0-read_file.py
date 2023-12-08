#!/usr/bin/python3
"""read_file function
"""


def read_file(filename=""):
    """print to stdout the content of a file
    Args:
        filename
    """
    with open(filename, 'r') as f:
        filecontent = f.read()
        print(filecontent, end="")
