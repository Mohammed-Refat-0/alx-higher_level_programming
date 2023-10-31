#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = abs(number) % 10
    if number < 0:
        lastdigit = -lastdigit
    print(f"Last digit of {number:d} is {lastdigit:d} and is ", end="")
    if lastdigit > 5:
        print("greater than 5")
    elif lastdigit == 0:
        print("0")
    else:
        print("less than 6 and not 0")
    return (lastdigit)
