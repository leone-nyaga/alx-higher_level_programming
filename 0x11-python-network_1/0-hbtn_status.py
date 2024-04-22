#!/usr/bin/python3

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body))
