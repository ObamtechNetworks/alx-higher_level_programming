#!/usr/bin/python3
"""This module defines a script that runs sql queries using MySQLdb"""


# import the module
import MySQLdb
import sys

# create a func for this


def cities_lists(username, password, dbname):
    """lists all cities using MySQLdb module"""
    # create a connection running on localhost port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname,
            charset="utf8")

    cur = db.cursor()  # create a cursor in MySQL python

    # lists all state from db
    query = """
    SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cur.execute(query)
    query_rows = cur.fetchall()
    for rows in query_rows:
        print(rows)

    # close cursor and db connection
    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        cities_lists(args[1], args[2], args[3])
