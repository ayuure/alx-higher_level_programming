#!/usr/bin/python3
"""class for square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter method"""
        return self.height

    @size.setter
    def size(self, value):
        """setter method"""
        self.validate_input("size", value)
        self.width = value
        self.height = value

    def __str__(self):
        """override"""
        return '[{}] ({}) {}/{} - {}'.format(__class__.__name__,
                                              self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """update class"""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dict method"""
        new_dic = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return new_dic

    def to_csv(self):
        """Convert instance attributes to CSV-compatible format"""
        return [self.id, self.size, self.x, self.y]

    @classmethod
    def create(cls, **kwargs):
        """Create an instance with attributes set from keyword arguments"""
        instance = cls(**kwargs)  # Create an instance using keyword arguments
        return instance