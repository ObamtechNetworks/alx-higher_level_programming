#!/usr/bin/python3
"""
A module that creates the State `California` with the City: `San Fransisco`
from the database `hbtn_0e_100_usa`
"""


# import necessary sqlalchemy modules
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from relationship_state import State, Base
from relationship_city import City


def create_state_and_city_frm_DB(username, password, db_name):
    """
    creates the state `California` and city `San Fransisco`
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

    # create the state object instance
    state1 = State(name="California")

    # create the City object instance and reference it's state
    city1 = City(name="San Fransisco", state=state1)

    state1.cities.append(city1)

    # add the State and City object to the database session
    session.add(state1)

    # commit changes to the database session
    session.commit()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        create_state_and_city_frm_DB(sys.argv[1], sys.argv[2], sys.argv[3])
