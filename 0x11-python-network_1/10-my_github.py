#!/usr/bin/python3

"""
takes GitHub credentials (username and password)
"""

if __name__ == '__main__':
    import sys
    import requests
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    info = (username, password)
    r = requests.get(url, auth=info)
    try:
        print(r.json()['id'])
    except Exception:
        print('None')
