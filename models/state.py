#!/usr/bin/python3
"""This module creates a State class that inherits from the BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
        """This class inherits from the BaseModel to manage state objects"""

        name = ""
