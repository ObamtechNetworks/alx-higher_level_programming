#!/usr/bin/python3
"""module defines a script that lists objects
from a given database"""

# Import the model to use for the DB
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def list_state_like_a_sql_alchemy_style(username, password, db_name):
    """
    lists all states in a database contains 'a'
    using sqlalchemy method

    username (str): username of the given database
    password (str): password of the given database
    db_name (str): the database to use
    """
    # CREATE A CONNECTION
    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            db_name)

    # CREATE AN ENGINE
    engine = create_engine(DB_URL, pool_pre_ping=True)
    # MIGRATE ORM to TABLE
    Base.metadata.create_all(engine)

    # CREATE SESSION FOR CRUD OPERATIONS
    Session = sessionmaker(bind=engine)
    session = Session()  # session instance

    # Query to list ALL states that contains a (from both sides)
    query = session.query(State).filter(State.name.like('%a%')).order_by(
            State.id).all()

    # PRINT results, state id and state name
    for state in query:
        print("{}: {}".format(state.id, state.name))

    # close the session
    session.close()


if __name__ == "__main__":
    list_state_like_a_sql_alchemy_style(sys.argv[1], sys.argv[2], sys.argv[3])
