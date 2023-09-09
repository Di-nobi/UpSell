#!/usr/bin/python3

import models
from models.base import BaseModel, Base
from models.user import User
from models.open_deal import Opendeal
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {
    'User': User,
    'Opendeal': Opendeal,

}

class database():
    """Interacts with MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        user = 'first_usr'
        pssword = getenv('Upselldb122#@!')
        host = getenv('DINOBI_SERVE_HOST')
        db = 'Upsell_db'

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pssword, host, db))

    def all(self, cls):
        """Gets all data available"""
        new_dict = {}
        for cls in classes:
            if not cls:
                objt = self.__session.query(cls).all()
                for obj in objt:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        """Adds new data to the database"""
        self.__session.add(obj)

    def get(self, cls, id):
        """Gets a class key"""
        all_key = models.storage.all(cls).values()
        for count in all_key:
            if count.id == id:
                return count
        return None
    
    def count(self, cls):
        """Counts the number of class"""
        return len(models.storage.all(cls).values())
    
    def save(self):
        """Saves new added data"""
        self.__session.commit()

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session