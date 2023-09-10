#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Closeddeal(BaseModel, Base):
    """Class of a Opendeal"""
    __tablename__ = 'Closed_deal'

    name = Column(String(255), nullable=False)
    number = Column(Integer, nullable=False)
    user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
    opendeal = Column(String(50), ForeignKey('Open_deal.id'), nullable=False)