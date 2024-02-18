#!/usr/bin/python3
"""This module defines a class definition of a `State and an instance
`Base = declarative_base()` of the SQLAlchemy library
This is used to for the ORM mapping and configuration
"""


# import modules
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    # Also, the reference from a City object to his State
    # should be named state, this is the work of the backref
    # If the State object is deleted,
    # all linked City objects must be automatically deleted.
    # this is handled by the cascade="all, delete-orphan"
    from relationship_city import City
    cities = relationship(
            "City",
            cascade="all, delete-orphan",
            backref='state')
