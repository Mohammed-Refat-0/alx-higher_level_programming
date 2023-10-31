#!/usr/bin/python3
def uppercase(str):
    list = []
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            list.append(ord(i) - 32)
        else:
            list.append(ord(i))
    for i in range(len(list)):
        print("{}".format(chr(i)), end="")
        print()
