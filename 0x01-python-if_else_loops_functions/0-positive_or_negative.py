#!/usr/bin/python3
import random
if __name__ == "__main__":
    number = random.randint(-10, 10)
    if number > 0:
        print("{} is a positive integer.".format(number))
    elif number == 0:
        print("{} is zero.".format(number))
    else:
        print("{} is a negative integer.".format(number))

