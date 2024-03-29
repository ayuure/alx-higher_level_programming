#!/usr/bin/python3
"""
    This is a class module
"""


class Rectangle:
    """
    Rectangle class that gets the area
    """

    def __init__(self, width=0, height=0):
        """
    init Rectangle class
    """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Getter for width
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """
        Setter for width of rectangle
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter for height of rectangle
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """
        setter for height of rectangle
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
