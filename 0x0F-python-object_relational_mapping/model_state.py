#!usr/bin/python3
"""This module defines a class definition of a `State and an instance
`Base = declarative_base()` of the SQLAlchemy library
This is used to for the ORM mapping and configuration
"""


# import modules
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

# create a Base instance
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)  # cannot be null


'''
def main(username, password, db_name):
    """ to execute the MYSQL connection and session"""

    # Define the MYSQL CONNECTION
    DB_URL = "mysql://{}:{}@localhost:3306/db_name".format(
            username,
            password,
            db_name)

    # define the connection engine
    engine = create_engine(DB_URL)

    # bind the engine to the metadata of the Base Class
    Base.metadata.create_all(engine)

    # create a session to intereact withthe database
    Session = sessionmaker(bind=engine)
    session = Session()  # create  a session instance


if __name__ == '__main__':
    args = sys.argv

    if len(args) == 4:
        main(args[1], args[2], args[3])
'''
