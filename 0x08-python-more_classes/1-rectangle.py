#!/usr/bin/python3
"""
    This is a class module
"""
class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, height=0, width=0):
        self._width = width     
        self._height = height  
    @property
    def width(self):
        """
        Getter for width
        """
        return(self._width)
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
                self._width = value
        except (TypeError, ValueError)as e:
            print(e)
    @property
    def height(self):
        """
        Getter for height of rectangle
        """
        return(self._width)
    @height.setter
    def height(self, value):
        """
        setter for height of rectangle
        """
        try:
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            elif value < 0: 
                raise ValueError('width must be >= 0')
            else:
                self._height = value
        except (TypeError, ValueError) as e:
            print(e)