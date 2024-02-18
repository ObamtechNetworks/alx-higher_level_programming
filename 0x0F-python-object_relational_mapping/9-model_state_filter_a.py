#!/usr/bin/python3
"""module defines a script that lists objects
from a given database"""


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

    query = session.query(State).filter(State.name.like('%a%')).order_by(
            State.id).all()

    for state in query:
        print("{}: {}".format(state.id, state.name))

    # close the session
    session.close()


if __name__ == "__main__":
    list_state_sql_alchemy_style(sys.argv[1], sys.argv[2], sys.argv[3])
