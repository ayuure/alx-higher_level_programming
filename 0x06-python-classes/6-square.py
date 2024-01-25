#!/usr/bin/python3
'''Find the area, print out the sqaure and et the positon'''


class Square:
    '''Find the area, print out the sqaure and at a the positon'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        '''area of the square'''
        return self.__size * self.__size

    @property
    def size(self):
        '''getter size of square'''
        return self.__size

    @size.setter
    def size(self, size):
        '''setter size of the square'''
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def my_print(self):
        """print square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print('-' * self.position[0] + '#' * self.size)

    @property
    def position(self):
        """getter position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter position"""
        self.__position = value
        if not isinstance(value, tuple) and len(value) == 2:
            if not all(isinstance(x, int) and x > 0 for x in value):
                raise TypeError('position must be a tuple of 2 positive integers')

    def __str__(self):
        """str magic dune formater"""
        result = ''
        if self.size == 0:
            result += '\n'
        else:
            for _ in range(self.position[1]):
                result += '\n'
            for _ in range(self.size):
                result += ' ' * self.position[0] + '#' * self.size + '\n'
        return result.strip()