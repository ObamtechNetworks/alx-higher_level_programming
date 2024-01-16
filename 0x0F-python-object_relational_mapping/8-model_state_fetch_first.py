#!/usr/bin/python3
"""module defines a script that lists all objects
from an inputted database"""


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

    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            db_name)

    engine = create_engine(DB_URL, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    state_query = session.query(State).order_by(State.id).first()

    if state_query:
        print("{}: {}".format(state_query.id, state_query.name))
    else:
        print("Nothing")

    # close the session
    session.close()


if __name__ == "__main__":
    list_state_sql_alchemy_style(sys.argv[1], sys.argv[2], sys.argv[3])
