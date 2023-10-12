#!/usr/bin/python3
"""This module creates an Amenity class that inherits from the BaseModel"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """This class inherits from the BaseModel to  manage amenity objects"""

    name = ""
