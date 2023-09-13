#!/usr/bin/python3
# 0-read_file

"""
function that reads  text file
"""


def read_file(filename=""):
    """reads text file (UTF8) and prints it to stdout
    Returns none
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
