def safe_print_list(my_list=[], x=0):
    count = 0
    i = 0
    while (i < x):
        try:
            print(mylist[i], end=" ")
            count = +1
            i = +1
        except IndexError:
            print("out of index error")
        finally:
            print()
            return count
