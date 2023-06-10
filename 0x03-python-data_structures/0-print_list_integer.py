#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """Print all integers of a list."""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
