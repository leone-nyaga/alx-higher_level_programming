#!/usr/bin/python3
# 8-uppercase.py

def uppercase(input_str):
    """Print a string in uppercase."""
    for char in input_str:
        uppercase_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
        print("{}".format(uppercase_char), end='')
