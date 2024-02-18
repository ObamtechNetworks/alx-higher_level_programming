#!/usr/bin/python3
"""
module defines a script that lists all objects
from a given database
Using the SQLAlchemy style
"""


from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def list_state_sql_alchemy_style(username, password, db_name):
    """
    lists all states in a database using sqlalchemy method

    username (str): username of the given database
    password (str): password of the given database
    db_name (str): the database to use
    """

    # STEP 1: Create a connection engine
    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            db_name)

    engine = create_engine(DB_URL, pool_pre_ping=True)
    # STEP 2: Migrate objects to  Database via ORM mapping
    Base.metadata.create_all(engine)

    # STEP 3: create a session to manipulate DB
    Session = sessionmaker(bind=engine)
    session = Session()

    # STEP 4: write query to list all State objects from the DB
    query_result = session.query(State).order_by(State.id).all()

    # OUTPUT RESULT
    for state in query_result:
        print("{}: {}".format(state.id, state.name))

    # CLOSE SESSION
    session.close()


if __name__ == "__main__":
    list_state_sql_alchemy_style(sys.argv[1], sys.argv[2], sys.argv[3])
