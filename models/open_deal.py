#!/usr/bin/python3
from models.base import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Opendeal(BaseModel, Base):
    """Class of a Opendeal"""
    __tablename__ = 'Open_deal'

    name = Column(String(255), nullable=False)
    number = Column(Integer, nullable=False)
    user_id = Column(String(50), ForeignKey('users.id'), nullable=False)
    closeddeal = Column(String(50), ForeignKey('Closed_deal.id'), nullable=False)
