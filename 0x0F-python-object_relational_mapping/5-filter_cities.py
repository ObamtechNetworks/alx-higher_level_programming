#!/usr/bin/python3
"""This module defines a script that runs sql queries using MySQLdb"""


# import the module
import MySQLdb
import sys

# create a func for this


def list_cities_by_user_input(username, password, dbname, user_input):
    """
    lists all cities by user_input using MySQLdb module
    Args:
        (username: str): The DB username
        (password: str): The DB password
        (dbname: str): The DB to use
        (user_input: str): The cities to list
    """
    # STEP 1: create connection
    # create a connection running on localhost port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname,
            charset="utf8")

    # STEP 2: Creae a cursor
    cur = db.cursor()  # create a cursor in MySQL python

    # STEP 3: QUERY to execute
    # lists all cities in state based on match by user_input from db
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # STEP 4: EXECUTE Query
    cur.execute(query, (user_input,))

    # STEP 5: fetch results
    query_rows = cur.fetchall()

    # create a list to store city_names
    city_names = []

    # loop through the 2D tuple  results
    # append only the city_names that match to the city_names list

    for rows in query_rows:
        for col in rows:
            city_names.append(str(col))

    # convert list to string separated by comma
    print(', '.join(city_names))

    # STEP 6: close connection
    # close cursor and db connection
    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 5:
        list_cities_by_user_input(args[1], args[2], args[3], args[4])
