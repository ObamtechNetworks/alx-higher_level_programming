#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
# Imports the model to work with, so step one creating model
from model_state import Base, State
# imports create engine for creating the DB engine to interface with
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True)
    # create table based on input
    Base.metadata.create_all(engine)
