#!/usr/bin/python3
"""A class that defines all common attributes for other classes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Instantiates new model"""

        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], tform)
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], tform)
            self.__dict__.update(kwargs)

        else:
            self.id =str(uuid.uuid4())
            self.created_at = self.update_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """str representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """save definition"""
        from models import storage
        self.update_at = datetime.new()
        storage.save()

    def t0_dict(self):
        """returns dictionary of the Basemodel class"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] =self.__class.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
