#!/usr/bin/python3
"""
    Module for class Student.
"""


class Student:
    """
        A class students that defines a student by:
        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that returns directory description with filter """
        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                res = {}
                for i in attrs:
                    if i in self.__dict__:
                        res[i] = self.__dict__[i]
                return res
        return self.__dict__ 
