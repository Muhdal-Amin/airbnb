#!/usr/bin/python3
"""
This script contains the BaseModel that defines all

common attributes/methods for other classes

"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:

    """Parent class from which other child classes will inherit from"""

    def __init__(self, *args, **kwargs):

        """
        BaseModel class contructor that initializes all instance attributes

        Args:
            - *args: list of arguments (not to be used)
            - **kwargs: dictionary of key-value arguments
        """

        if kwargs:
              for key in kwargs:
                  if key == "created_at":
                      self.__dict__["created_at"] = datetime.strptime(
                          kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                  elif key == "updated_at":
                      self.__dict__["updated_at"] = datetime.strptime(
                          kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                  else:
                      self.__dict__[key] = kwargs[key]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """updates the public instance attribute (updated_at)"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = my_dict["created_at"].isoformat()
        new_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return new_dict

    def __str__(self):
        """string representation of all class instance and it's attributes"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
