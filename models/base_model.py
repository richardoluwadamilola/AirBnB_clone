#!/usr/bin/python3
# Defines the Base class for the project

import models
from uuid import uuid4
from datetime import datetime

Class BaseModel:
    # Represents the BaseModel of the AirBnB project.

    def __init__(self, *args, **kwargs):
        """
        Initialize a BaseModel.
        Args:
        *args(any): Unused.
        **kwargs(dict): key/value pairs of attributes.
        """

        dtime = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())  #id(str): handles unique user identity
            self.created_at = datetime.utcnow()  #created_at: assigns current datetime
            self.updated_at = datetime.utcnow() #updated_at: updates current datetime
            models.storage.new(self)
        else: 
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                            value, dtime)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else: 
                    self.__dict__[key] = value

def save(self):
    """
    Updates the public instance attribute:
    'updated_at' with the current datetime
    """
    self.updated_at = datetime.utcnow()
    models.storage.save()

def to_dict(self):
    """
    Returns a dictionary containing all keys/values of
    __dict__ of an instance
    """
    redict = {}
    for key, value in self.__dict__.items():
        if key == "created_at" of key == "updated_at":
            redict[key] = value.isoformat()
        else:
            redict[key] = value
    redict["__class__"] = self.__class__.__name__
    return redict

def __str__(self):
    """
    Returns string representation of the class
    """
    clame = self.__class__.__name__
    return "[{}] ({}) {}". format(clame, self.id, self.__dict__)




