#!/usr/bin/python3
"""This module creates a City class that inherits from the BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """This class inherits from the BaseModel to manage city objects"""

    state_id = ""
    name = ""
