#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle is beautiful"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter method"""
        self.validate_input('width', value)
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height setter method"""
        self.validate_input('height', value)
        self.__height = value

    @property
    def x(self):
        """getter for x method"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """setter for x method"""
        self.validate_input('x', value, flag=False)
        self.__x = value

    @property
    def y(self):
        """getter for y method"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """setter for y method"""
        self.validate_input('y', value, flag=False)
        self.__y = value

    def validate_input(self, name, input, flag=True):
        """validation method"""
        if not isinstance(input, int):
            raise TypeError('{} must be an integer'.format(name))
        elif flag and input < 0:
            raise ValueError('{} must be > 0'.format(name))
        elif input < 0:
            raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        """area method"""
        return self.height * self.width

    def display(self):
        """display method"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """str overwrite method"""
        return'[{}] ({}) {}/{} - {}/{}'.format(__class__.__name__ , self.id, self.x
                                                ,self.y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update method"""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to dictionary method"""
        new_dic = {'id': self.id, 'width': self.width,
                   'height': self.height, 'x': self.x, 'y': self.y}
        return new_dic

    def to_csv(self):
        """Convert instance attributes to CSV-compatible format"""
        return [self.id, self.width, self.height, self.x, self.y]

    @classmethod
    def create(cls, **kwargs):
        """Create an instance with attributes set from keyword arguments"""
        instance = cls(**kwargs)  # Create an instance using keyword arguments
        return instance