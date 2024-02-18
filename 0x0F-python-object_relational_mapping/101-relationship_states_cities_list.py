#!/usr/bin/python3
"""
A module that lists all states and cities objects in the db
from the database `hbtn_0e_100_usa`
"""


# import necessary sqlalchemy modules
from sqlalchemy.orm import sessionmaker, joinedload
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City
import sys


def list_states_n_cities(username, password, db_name):
    """
    lists all states objects with correspoinding cities
    Args:
        username: (str): A username of the database
        password: (str): The database password
        db_name: (str): The name of the database to use
    """

    # STEP 1: CREATE CONNECTION
    DB_URL = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username,
            password,
            db_name)

    # CREATE ENGINE
    engine = create_engine(DB_URL, pool_pre_ping=True)

    # MIGRATE OBJECTS TO TABLE
    Base.metadata.create_all(engine)  # create table

    # create the session FOR CRUD OPERATIONS
    Session = sessionmaker(bind=engine)
    session = Session()  # create session instance

    # list states with corresponding cities
    states = session.query(State).options(joinedload(State.cities)).all()
    # print the results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
    # close the session
    session.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        list_states_n_cities(sys.argv[1], sys.argv[2], sys.argv[3])
