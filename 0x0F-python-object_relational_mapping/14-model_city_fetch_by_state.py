#!/usr/bin/python3
"""A script that prints all City objects
from the database hbtn_0e_14_usa
"""

# import the models
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


def fetch_city_objs(username, password, db_name):
    """
    fetches all `City` objects from the given database
    username (str): the given database username
    password (str): the given database password
    db_name (str): the given database name
    """

    # CREATE CONNECTION
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

    # query to list all cities & states, where city.state_id matches State.id
    cities_states = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()
    # print the state name, city id and city name in the format below
    for city, state in cities_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # close the session
    session.close()


if __name__ == "__main__":
    fetch_city_objs(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
