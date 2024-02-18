#!/usr/bin/python3
"""module defines a script that lists or inserts/ manipulates obj
from a given database"""

# import the models to interface with the DB
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def add_state_to_table(username, password, db_name):
    """
    insert a state  to the State object: "Louisiana"
    in a database using sqlalchemy method

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
    # create session instance
    session = Session()

    # create a state instance with the field to add
    new_state = State(name='Louisiana')

    # add the new state instance to the session
    session.add(new_state)

    # commit the changes to DB addition (insert the record)
    session.commit()

    # print the id of the newly added object
    print(new_state.id)

    # close the session
    session.close()


if __name__ == "__main__":
    add_state_to_table(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
