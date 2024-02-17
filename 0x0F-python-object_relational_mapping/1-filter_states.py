#!/usr/bin/python3
"""
This module defines a script that runs sql queries using MySQLdb
"""


# import the MySQLdb module
import MySQLdb
import sys

# create a func for this


def states_starting_with_N(username, password, dbname):
    """
    Lists states starting with 'N' using MySQLdb module.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        dbname (str): Database name.

    Returns:
        None
    """

    # STEP 1: create a connection running on localhost port 3306
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=dbname,
            charset="utf8")

    # STEP 2: create cursor
    cur = db.cursor()  # create a cursor in MySQL python

    # QUERY to list all state from db
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"

    # STEP 3, execute the SQL query
    cur.execute(query)
    
    # STEP 4, fetch all the results
    query_rows = cur.fetchall()
    for rows in query_rows:
        if rows[1][0] == 'N':
            print(rows)

    # close cursor and db connection
    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        states_starting_with_N(args[1], args[2], args[3])
