#!/usr/bin/python3
"""User FIle"""
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    firstName = Column(String(255), nullable=False)
    lastName = Column(String(255), nullable=False)
    closedDeal = relationship("Closed_deal", backref="users")
    openDeal = relationship("Open_deal", backref="users")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)