#!/usr/bin/python3
"""Base model of Upsell"""
import uuid
import models
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """Class which defines all common attributes for the other classes"""
    id = Column(String(60), primary_key=True)
    created = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated = Column(DateTime, default=datetime.utcnow(), nullable=False)
    def __init__(self, *args, **kwargs):
        """
        __init__ method for the BaseModel class
        Args:
            args (tuple): arguments
            kwargs (dict): key word arguments
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created' or key == 'updated':
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created = datetime.now()
            self.updated = datetime.now()
            models.storage.new(self)

    # def __eq__(self, num: int, num2: int) -> bool:
    #     if num != num2:
    #         print(f"Unequal attributes")
    #         return False
    #     else:
            # return True
        
    def __str__(self) -> str:
        """Returns the string representation of the class data"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        """Saves new data to storage"""
        models.storage.new(self)
        models.storage.save()
    
    def to_dict(self):
        data = self.__dict__.copy()
        if "created" in data:
            data["created"] = data["created"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        data['updated'] = data['updated'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        data["__class__"] = self.__class__.__name__
        return data
