#!/usr/bin/python3
"""My Custom Square Module"""

class Square:
    """My Square Class Definition"""
    def __init__(self, size=0):
        """Instantiate a new square object"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")