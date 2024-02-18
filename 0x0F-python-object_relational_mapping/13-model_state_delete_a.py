#!/usr/bin/python3
"""module defines a script that manipluates objects via ORM"""

# import the models to interface with
from model_state import Base, State
from sqlalchemy import (create_engine, update, delete)
from sqlalchemy.orm import sessionmaker
import sys


def delete_states_like_a(username, password, db_name):
    """
    A script that deletes states where name contains letter a
    username (str): username of the given database
    password (str): password of the given database
    db_name (str): the database to use
    """
    # CREATE A CONNECTION
    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            db_name)

    # CREATE ENGINEn
    engine = create_engine(DB_URL, pool_pre_ping=True)
    # MIGRATE OBJECTS TO TABLE
    Base.metadata.create_all(engine)  # create table

    # create the session FOR CRUD OPERATIONS
    Session = sessionmaker(bind=engine)
    session = Session()

    # filter out all states that contains 'a'
    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()

    # check if they exist
    if states_to_delete:
        for state in states_to_delete:  # delete the states
            session.delete(state)

        # commit changes to the database
        session.commit()

    # ALTERNATIVE METHOD
    # QUERY TO delete matching records2
    # delete_statement = delete(State).where(
    #        State.name.like('%a%'))

    # execute the delete statement
    # session.execute(delete_statement)

    # commit changes to database
    # session.commit()

    # states = session.query(State).order_by(State.id).all()

    # close the session
    session.close()


if __name__ == "__main__":
    delete_states_like_a(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
