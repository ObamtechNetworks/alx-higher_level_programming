#!/usr/bin/python3
"""module defines a script that lists all objects
from an inputted database"""


from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def state_obj_with_user_input(username, password, db_name, state_name):
    """
    lists states with inputted name
    in a database using sqlalchemy method

    username (str): username of the given database
    password (str): password of the given database
    db_name (str): the database to use
    """

    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            db_name)

    engine = create_engine(DB_URL, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    find_match = session.query(State).filter(State.name == state_name).order_by(State.id).all()

    if find_match:
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
