def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            print(i, end=" ")
            count = +1
        except IndexError:
            print("out of index error")
        finally:
            print()
            return count
