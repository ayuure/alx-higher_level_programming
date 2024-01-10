#!/usr/bin/python3
#!/usr/bin/python3
"""This is a bass class"""


class BaseGeometry():
    """class for bassGeo"""
    def area(self):
        """area of baseGeo"""
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """Validator"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0: 
            raise ValueError('{} must be greater than 0'.format(name))