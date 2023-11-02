#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_arg = len(argv)
    if len_arg == 1:
        print("0 arguments.")
    elif len_arg == 2:
        print("1 argument:")
    elif len_arg > 2:
        print(f"{(len_arg - 1):d} arguments:")
    if len_arg > 1:
        for i in range(1, len_arg):
            print(f"{i:d}: {argv[i]:s}")
