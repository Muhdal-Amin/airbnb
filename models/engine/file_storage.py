#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os


class FileStorage:

    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets the key-value pair in __objects (class.id as key, obj as val)"""
        keyFormat = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[keyFormat] = obj

    def save(self):
        """serializes __objects to the JSON __file_path"""
        dictObj = {}
        for key, val in FileStorage.__object.items():
            dictObj[key] = val.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as jsonF:
                json.dump(dictObj, jsonF)

    def reload(self):
        """deserializes the JSON string to objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        definedClasses = {"BaseModel": BaseModel,
                          "User": User,
                          "State": State,
                          "City": City,
                          "Amenity": Amenity,
                          "Place": Place,
                          "Review": Review}

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as jsonF:
                deserialised_obj = load(jsonF)
                for obj_values in deserialized_obj.values():
                    className = obj_values["__class__"]
                    class_obj = definedClasses[className]
                    self.new(class_obj(**obj_values))

        except FileNotFoundError:
            pass


    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
            {"id": str,
             "created_at": datetime.datetime,
             "updated_at": datetime.datetime},
            "User":
            {"email": str,
             "password": str,
             "first_name": str,
             "last_name": str},
            "State":
            {"name": str},
            "City":
            {"state_id": str,
             "name": str},
            "Amenity":
            {"name": str},
            "Place":
            {"city_id": str,
             "user_id": str,
             "name": str,
             "description": str,
             "number_rooms": int,
             "number_bathrooms": int,
             "max_guest": int,
             "price_by_night": int,
             "latitude": float,
             "longitude": float,
             "amenity_ids": list},
            "Review":
            {"place_id": str,
             "user_id": str,
             "text": str}
        }
        return attributes
