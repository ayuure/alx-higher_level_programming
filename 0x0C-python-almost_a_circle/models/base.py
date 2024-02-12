#!/usr/bin/python3
import json
import os
import csv

"""
base class that contains methods that will be inherited by other classes
"""


class Base:
    """Initialization of the class"""
    __nb_object = 0

    def __init__(self, id=None):
        """init method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """convents dictionary to json file"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json in a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON string to list of dictionaries"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **kwargs):
        """Create an instance with attributes set from keyword arguments"""
        instance = cls(**kwargs)
        return instance

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from CSV file"""
        from os import path
        filename = cls.__name__ + ".csv"
        if not path.isfile(filename):
            return []
        with open(filename, "r",  encoding="utf-8") as f:
            return [cls.create(**o) for o in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to CSV and write to file"""
        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', newline='') as f:
            writer = csv.writer(f)
            for obj in list_objs:
                writer.writerow(obj.to_csv())

    @classmethod
    def load_from_file_csv(cls):
        """ deserilizes object frm csv file """
        from models.rectangle import Rectangle
        from models.square import Square
        list_objs = []

        with open("{}.csv".format(cls.__name__), "r", newline="",
                  encoding="utf-8") as f:
            rd = csv.reader(f)
            for row in rd:
                row = [int(objs) for objs in row]
                if cls is Rectangle:
                    objs = {"id": row[0], "width": row[1], "height": row[2],
                            "x": row[3], "y": row[4]}
                else:
                    objs = {"id": row[0], "size": row[1], "x": row[2],
                            "y": row[3]}
                list_objs.append(cls.create(**objs))
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        ''' turtle graphics draws all the Rectangles and Squares '''
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)

        for item in list_rectangles + list_squares:
            img = turtle.Turtle()
            img.color((randrange(255), randrange(255), randrange(255)))
            img.pensize(1)
            img.penup()
            img.pendown()
            img.setpos((item.x + img.pos()[0], item.y - img.pos()[1]))
            img.pensize(10)
            for i in range(2):
                img.forward(item.width)
                img.left(90)
                img.forward(item.height)
                img.left(90)
            img.end_fill()
        time.sleep(5)
