#!/usr/bin/python3
"""This module defines a class definition of a `City`
and an instance `declarative_base()` of the SQLAlchemy library
This is used to for the ORM mapping and configuration
"""


# import modules
from relationship_state import Base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


# define the city model
class City(Base):
    """a city class to be used as ORM mapper for sqlalchemy"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)  # cannot be null
    # a foreign key to states.id in the states table
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
