#!/usr/bin/python3
"""This module defines a script that runs sql queries using MySQLdb"""


# import the module
import MySQLdb
import sys

# create a func for this


def cities_lists_by_user_input(username, password, dbname, user_input):
    """lists all cities by user_input using MySQLdb module"""
    # create a connection running on localhost port 3306
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname,
            charset="utf8")

    cur = db.cursor()  # create a cursor in MySQL python

    # lists all cities in state given by user_input from db
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cur.execute(query, (user_input,))
    query_rows = cur.fetchall()

    city_names = []

    for rows in query_rows:
        for col in rows:
            city_names.append(str(col))

    print(', '.join(city_names))
    # close cursor and db connection
    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 5:
        cities_lists_by_user_input(args[1], args[2], args[3], args[4])
