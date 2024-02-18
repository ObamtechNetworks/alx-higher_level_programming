#!/usr/bin/python3
"""module defines a script that list objects
from a given database"""

# import the model to map to DB
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def state_obj_with_user_input(username, password, db_name, state_to_search):
    """
    lists states based on user input in a DB  using sqlalchemy method

    username (str): username of the given database
    password (str): password of the given database
    db_name (str): the database to use
    """

    # CREATE A CONNECTION
    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            db_name)

    # CREATE ENGINE
    engine = create_engine(DB_URL, pool_pre_ping=True)

    # MIGRATE OBJECTS TO TABLE
    Base.metadata.create_all(engine)

    # CREATE SESSION FOR CRUD OPERATIONS
    Session = sessionmaker(bind=engine)
    session = Session()

    # QUERY to find state that macthes user_input
    find_match = session.query(State).filter(
            State.name == state_to_search).order_by(State.id).all()

    # if there's a match
    if find_match:  # print all the state id from the match
        for state in find_match:
            print("{}".format(state.id))
    else:
        print("Not found")

    # close the session
    session.close()


if __name__ == "__main__":
    state_obj_with_user_input(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4])
