#!/usr/bin/python3
"""This module defines a class definition of a `City`
and an instance `Base = declarative_base()` of the SQLAlchemy library
This is used to for the ORM mapping and configuration
"""


# import modules
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
# from sqlalchemy.orm import sessionmaker
# import sys

class City(Base):
    """a city class to be used as ORM mapper for sqlalchemy"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)  # cannot be null
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
