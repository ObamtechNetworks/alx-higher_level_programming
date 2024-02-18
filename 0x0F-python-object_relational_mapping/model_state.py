#!/usr/bin/python3
"""This module defines a class definition of a `State and an instance
`Base = declarative_base()` of the SQLAlchemy library
This is used to for the ORM mapping and configuration
"""


# import modules
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# create a Base instance
Base = declarative_base()


class State(Base):
    """
    a state class model to be used as ORM mapper for sqlalchemy
    Args:
        `Base` (the Base class for ORM mapping and configuration)
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)  # cannot be null
