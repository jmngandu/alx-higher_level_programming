#!/usr/bin/python3
"""
used requests models
"""

if __name__ == '__main__':
    import requests
    import sys
    para = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=para)
    print(r.text)
