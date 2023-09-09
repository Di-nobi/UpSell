#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String

class Opendeal(BaseModel, Base):
    """Class of a Opendeal"""
    __tablename__ = 'opendeal'

    name = Column(String(255), nullable=False)
    number = Column(Integer, nullable=False)

