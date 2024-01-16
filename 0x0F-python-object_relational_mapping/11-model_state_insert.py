#!/usr/bin/python3
"""module defines a script that lists all objects
from an inputted database"""


from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def add_state_to_table(username, password, db_name):
    """
    add states to the State object: "Louisiana"
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

    # create an instance
    new_state = State(name='Louisiana')

    # create session
    session = Session()

    # add new state to the instance
    session.add(new_state)

    # commit the addition (insert the record)
    session.commit()

    print(new_state.id)

    # close the session
    session.close()


if __name__ == "__main__":
    add_state_to_table(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
