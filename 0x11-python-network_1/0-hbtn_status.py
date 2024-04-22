#!/usr/bin/python3

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print("- Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
