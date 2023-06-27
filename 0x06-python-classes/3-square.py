#!/usr/bin/python3
# 3-square.py

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, __size=0):
        """Initialize a new square.

        Args:
            __size (int): The __size of the new square.
        """
        if not isinstance(__size, int):
            raise TypeError("__size must be an integer")
        elif __size < 0:
            raise ValueError("__size must be >= 0")
        self.__size = __size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
