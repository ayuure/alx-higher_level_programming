#!/usr/bin/python3
"""
    This is a class module
"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """init Rectangle class"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter for width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Setter for width of rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for height of rectangle"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """setter for height of rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
