#!/usr/bin/python3
"""module defines a script that maps objects to DB using ORM"""

# import models to map and interface with
from model_state import Base, State
from sqlalchemy import (create_engine, update)
from sqlalchemy.orm import sessionmaker
import sys


def change_state_name_sqlalchemy_style(username, password, db_name):
    """
    A script that changes the name of a state based on a given id
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

    # CREATE ENGINE
    engine = create_engine(DB_URL, pool_pre_ping=True)

    # MIGRATE OBJECTS TO TABLE
    Base.metadata.create_all(engine)  # create table

    # CREATE SESSION FOR CRUD OPERATIONS
    Session = sessionmaker(bind=engine)
    session = Session()  # SESSION INSTANCE

    # QUERY to update the record where id = 2
    update_statement = update(State).where(
            State.id == 2).values(name="New Mexico")

    # EXECUTE the  update statement
    session.execute(update_statement)

    # commit changes to database
    session.commit()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # close the session
    session.close()


if __name__ == "__main__":
    change_state_name_sqlalchemy_style(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
