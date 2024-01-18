#!/usr/bin/python3
"""module defines a script that lists all objects
from an inputted database"""


from model_state import Base, State
from sqlalchemy import (create_engine, update, delete)
from sqlalchemy.orm import sessionmaker
import sys


def delete_states_a(username, password, db_name):
    """
    A script that deletes states where name contains letter a
    username (str): username of the given database
    password (str): password of the given database
    db_name (str): the database to use
    """

    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            db_name)

    # establish connection
    engine = create_engine(DB_URL, pool_pre_ping=True)
    Base.metadata.create_all(engine)  # create table

    # create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # delete matching records2
    delete_statement = delete(State).where(
            State.name.like('%a%'))

    # execute the delete statement
    session.execute(delete_statement)

    # commit changes to database
    session.commit()

    states = session.query(State).order_by(State.id).all()

    # close the session
    session.close()


if __name__ == "__main__":
    delete_states_a(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
