#!/usr/bin/python3
"""City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """Class to link SQL"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=False, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
