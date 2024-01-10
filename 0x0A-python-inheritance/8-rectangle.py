#!/usr/bin/python3
#!/usr/bin/python3
"""This is a bass class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class for bassGeo"""
    def __init__(self, width, height):
        """init method"""
        self._width = self.integer_validator(self, width)
        self._height = self.integer_validator(self, height)
        
