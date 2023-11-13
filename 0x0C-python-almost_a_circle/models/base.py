#!/usr/bin/python3
"""This module defines the `Base Class` for this project
It is the `base or parent` of all classes in the following tasks
The goal is to manage `id` attribute in all future classes
and to avoid duplicating the same code (by extension, same bugs)
"""


import json
import csv
import turtle


class Base:
    """This is the `base` class for the future clases of this project
    it manages id attribute of the future clasess and prevents duplicates
    of same code
    """
    __nb_objects = 0  # tracks number of objects

    def __init__(self, id=None):
        """this is instantiates the class attributes"""
        if id is not None:  # assigns given id if id is not none
            self.id = id
        else:
            Base.__nb_objects += 1  # else increments no of objs
            self.id = Base.__nb_objects  # sets id to be nb objs

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        list_dictionaries is a list of dictionaries
        if list_dictionaries is None or empty, and empty str is returned
        else, JSON str representation of list_dictionaries is returned
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        # otherwise return JSON str represent...
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        json_string is a string representing a list of dictionaries
        if json_string is None or empty, an empty list is returned
        else the json_string
        """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)  # deserializes back to python object

    @classmethod
    def save_to_file(cls, list_objs):
        """writes a JSON string representation of list_objs to a file
        list_objs is a list of instances who inherits of Base
        e.g list of Rectangle, or list of Square instances
        if list_objs is None, an empty list is saved
        the staticmethod to_json_string is to be used
        the file is overwritten if already exists
        filename must be  <Class name>.json - e.g Rectangle.json
        """
        # convert the list instances to a serializable list
        if list_objs is None or len(list_objs) == 0:
            list_objs = []
        else:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        # open the file
        filename = f"{cls.__name__}.json"
        json_str = cls.to_json_string(list_objs)

        # write the JSON representation to file
        with open(filename, "w") as json_file:
            json_file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        # create a dummy instance with mandatory attributes
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(3, 5)  # create dummy with two mand. attr
        elif cls.__name__ == "Square":
            dummy_instance = cls(3)  # create dummy with one mand. attr
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        the filename must be <Class name>.json e.g. Rectangle.json
        if the file doesn't exist, and empty list is returned
        otherwise, a list of instances - based on the current cls
        we are using the from_json_string and create methods previously
        """
        filename = f"{cls.__name__}.json"

        # try to open and read from the file
        try:
            with open(filename, "r") as json_file:
                json_str = json_file.read()
        except (Exception, FileNotFoundError):
            return []

        # convert the string back to a list of dict using the from_json..
        list_dict = cls.from_json_string(json_str)

        # convert each dictionary back into an instance of the cls
        # using the create classmethod above (unpack method **d)
        instance_list = [cls.create(**d) for d in list_dict]
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes a python obj, to a csv file"""
        # open the file
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            if list_objs is None or len(list_objs) == 0:
                csv_file.write("[]")
            else:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        csv_writer.writerow([obj.id, obj.width,
                                            obj.height, obj.x, obj.y])
                    elif cls.__name__ == 'Square':
                        csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserialiazes a csv file"""
        list_objs = []
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r') as csv_file:
                read_csv = csv.reader(csv_file)
                for row in read_csv:
                    if cls.__name__ == 'Rectangle':
                        list_objs.append(cls.create(
                            id=int(row[0]), width=int(row[1]),
                            height=int(row[2]), x=int(row[3]), y=int(row[4])
                            ))
                    elif cls.__name__ == 'Square':
                        list_objs.append(cls.create(
                            id=int(row[0]), size=int(row[1]),
                            x=int(row[2]), y=int(row[3])
                            ))
        except (FileNotFoundError, Exception):
            pass

        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        # create a turtle screen
        screen = turtle.Screen()
        # add bg color to screen
        screen.bgcolor("white")

        # create a turtle for drawing rectangles
        rect_turtle = turtle.Turtle()
        # specifiy turtle shape as square (repre a rectangle)
        rect_turtle.shape("square")
        # specify the color
        rect_turtle.color("blue")

        # Draw the rectangles
        for rectangle in list_rectangles:
            rect_turtle.penup()
            rect_turtle.goto(rectangle.x, rectangle.y)
            rect_turtle.pendown()
            for _ in range(2):
                rect_turtle.forward(rectangle.width)
                rect_turtle.left(90)
            rect_turtle.pendup()

        # create turtle for drawing squares
        square_turtle = turtle.Turtle()
        # specify the shape 'square'
        square_turtle.shape('square')
        # specify color
        square_turtle.color('orange')

        # Draw the squares
        for square in list_squares:
            square_turtle.penup()
            square_turtle.goto(square.x, square.y)
            square_turtle.pendown()
            for _ in range(4):
                square_turtle.forward(square.size)
                square_turtle.left(90)
        square_turtle.penup()

        # close the window on click
        screen.exitonclick()
