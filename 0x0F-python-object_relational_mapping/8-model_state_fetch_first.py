#!/usr/bin/python3
"""module defines a script that lists objects
from an given database"""

# import models State and Base (declarive_base)
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def list_first_state_obj_sql_alchemy_style(username, password, db_name):
    """
    lists first state object in database using sqlalchemy method

    username (str): username of the given database
    password (str): password of the given database
    db_name (str): the database to use
    """

    # CREATE  CONNECTION
    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            db_name)

    # CREATE ENGINE
    engine = create_engine(DB_URL, pool_pre_ping=True)
    # MIGRATE TO DATABASE
    Base.metadata.create_all(engine)

    # CREATE A SESSION SO AS TO PERFORM CRUD OPERATIONS
    Session = sessionmaker(bind=engine)
    session = Session()  # session instance

    # WRITE QUERIES
    # so instead of using .all(), to list or select all, we use .first()
    state_query = session.query(State).order_by(State.id).first()

    # check if result is valid, like doesn't return null
    if state_query:  # print the state id and name
        print("{}: {}".format(state_query.id, state_query.name))
    else:  # if nothing found, print nothing
        print("Nothing")

    # close the session
    session.close()


if __name__ == "__main__":
    list_first_state_obj_sql_alchemy_style(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
