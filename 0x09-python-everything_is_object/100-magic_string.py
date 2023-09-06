#!/usr/bin/python3
# 100-magic_string

def magic_string():
    s = "BestSchool"
    return "\n".join([s * i for i in range(1, 6)])
