#!/usr/bin/python3
"""User FIle"""
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String


class User(BaseModel, Base):
    __tablename__ = 'users'
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    firstName = Column(String(255), nullable=True)
    lastName = Column(String(255), nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)