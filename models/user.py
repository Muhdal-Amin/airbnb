#!usr/bin/python3
"""This module creates a User class that inherits from the BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel to manage user objects"""

    email=""
    password=""
    first_name=""
    last_name=""
