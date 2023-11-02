#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4.pyc
    list = dir(hidden_4.pyc)
    for i in range(len(list)):
        if list[i][0:2] != "__":
            print(list[i])
