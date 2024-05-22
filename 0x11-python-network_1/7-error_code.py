#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""

import requests
from sys import argv

if __name__ == '__main__':

    url = argv[1]

    try:
        result = requests.get(url)
        result.raise_for_status()
        print(result.text)
    except:
        print('Error code: {}'.format(result.status_code))
