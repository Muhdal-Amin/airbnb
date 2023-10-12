#!/usr/bin/python3
"""This module creates a Review class that inherits from the BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
        """This class inherits from the BaseModel to manage review objects"""

        place_id = ""
        user_id = ""
        text = ""
