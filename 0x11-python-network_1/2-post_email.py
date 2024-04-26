#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    ur = sys.argv[1]
    val = {"email": sys.argv[2]}
    da = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(ur, da)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
