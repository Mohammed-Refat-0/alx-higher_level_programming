#!/usr/bin/python3
"""write_files function
"""


def write_file(filename="", text=""):
    """overwrite file with text, and return number of written chars

    Args:
        filename (str, optional): file object
        text (str, optional): string

    Returns:
        _type_: number of written chars
    """
    with open(filename, 'w') as f:
        return (f.write(text))
