#!/usr/bin/python3
import random
if __name__ == "__main__":
    number = random.randint(-10, 10)
    if number > 0:
        print("The randomly generated number {} is a positive integer.".format(number))
    elif number == 0:
        print("The randomly generated number {} is zero.".format(number))
    else:
        print("The randomly generated number {} is a negative integer.".format(number))

