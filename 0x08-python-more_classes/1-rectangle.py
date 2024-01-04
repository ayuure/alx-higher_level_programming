#!/usr/bin/python3
"""
    This is a class module
"""
class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.__width = width     
        self.__height = height  
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
        try:
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            elif value < 0: 
                raise ValueError('width must be >= 0')
            else:
                self.__width = value
        except (TypeError, ValueError)as e:
            print(e)
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
        try:
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            elif value < 0: 
                raise ValueError('height must be >= 0')
            else:
                self.__height = value
        except (TypeError, ValueError) as e:
            print(e)
    def __repr__(self):
        return "{{'_Rectangle__height': {}, '_Rectangle__width': {}}}".format(self.__height, self.__width)