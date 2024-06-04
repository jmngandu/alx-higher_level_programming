#!/usr/bin/pyton3
"""Defiantion for a student class
"""


class Student:
   """a class for a student
   """

   def __init__(self, first_name, last_name, age):
       """Initalizes a student object
       """

       self.first_name = first_name
       self.last_name = last_name
       self.age = age

   def to_json(self, attrs=None):
       """returns a json representatiion of
       the object
       """

       if attrs != None and not isinstance(attrs, list):
           raise TypeError("attrs must me a list of strings")

       if attrs != None and any(not isinstance(attr, str) for attr in attrs):
           raise TypeError("attrs must me a list of strings")

       if attrs == None:
           return self.__dict__

       json_dic = {}
       for key in attrs:
           if key in self.__dict__.keys():
               json_dic[key] = self.__dict__[key]

       return json_dic

    def relod_from_json(self, json):
    """replaces object's attributes
    """

        for k, v in json.items():
            setattr(self, k, v)
