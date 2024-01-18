#!/usr/bin/python3
"""A script that prints all City objects
from the database hbtn_0e_14_usa
"""

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

    # construct URL
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

    cities_states = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()

    for city, state in cities_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # close the session
    session.close()


if __name__ == "__main__":
    fetch_city_objs(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3])
