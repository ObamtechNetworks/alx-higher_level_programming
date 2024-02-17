#!/usr/bin/python3
"""
This module defines a script that runs sql queries using MySQLdb
"""


# import the module
import MySQLdb
import sys

# create a func for this


def list_cities(username, password, dbname):
    """
    lists all cities using MySQLdb module
    Args:
        (username: str): the username of the database
        (password: str): the database access password
        (dbname: str): the database name
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

    # STEP 2: create cursor
    cur = db.cursor()  # create a cursor in MySQL python

    # STEP 3: QUERY TO EXECUTE
    # lists all state from db
    query = """
    SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    # STEP 4: EXECUTE QUERY
    cur.execute(query)

    # STEP 5: fetch results
    query_rows = cur.fetchall()
    for rows in query_rows:
        print(rows)

    # STEP 6: close connection
    # close cursor and db connection
    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        list_cities(args[1], args[2], args[3])
