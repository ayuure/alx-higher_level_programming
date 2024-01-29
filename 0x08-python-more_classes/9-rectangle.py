#!/usr/bin/python3
"""
    This is a class module
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
    init Rectangle class
    """
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """
    getter for height Rectangle class
    """
        return self.__height

    @height.setter
    def height(self, value):
        """
    setter for Rectangle class
    """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """
    getter for Rectangle class
    """
        return self.__width

    @width.setter
    def width(self, value):
        """
    setter for Rectangle class
    """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """
    area of Rectangle class
    """
        return self.__width*self.__height

    def perimeter(self):
        """
    perimeter of Rectangle class
    """
        perimeter = 2*(self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """
    print out Rectangle class
    """
        val = ''
        if self.__width == 0 or self.__height == 0:
            return val
        for _ in range(self.__height):
            val += str(self.print_symbol ) * self.__width + '\n'
        return val.strip()
    
    def __repr__(self):
        """
    repr print out of Rectangle class
    """
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """
    delete Rectangle class
    """
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
    static method of Rectangle class
    """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
    class method of Rectangle class
    """
        return cls(width=size, height=size)
