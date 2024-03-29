#!/usr/bin/python3
"""
    This is a class module
"""


class Rectangle:
    """
    Rectangle class
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
    init Rectangle class
    """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
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
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        """
        perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def print_str(self):
        """
        print of rectangle
        """
        str_ = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            str_ += "#" * self.__width + '\n'
        return str_.rstrip('\n')

    def __str__(self):
        """
        print of rectangle
        """
        return self.print_str()

    def __repr__(self):
        """
        print of rectangle here
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
