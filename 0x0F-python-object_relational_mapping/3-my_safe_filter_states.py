#!/usr/bin/python3
"""
This module defines a script that runs sql queries using MySQLdb
"""


# import the module
import MySQLdb
import sys

# create a func for this


def states_based_on_safe_user_input(username, password, dbname, user_input):
    """
    Lists states based on user input  using MySQLdb module.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        dbname (str): Database name.
        user_input (str): User input.

    Returns:
        None
    """

    # STEP 1: create connection
    # create a connection running on localhost port 3306
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=dbname,
            charset="utf8")

    # STEP 2: create a cursor
    cur = db.cursor()  # create a cursor in MySQL python

    # QUERY to execute
    # lists all state from db
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"

    # SANITIZE USER INPUT
    u_input = '%' + user_input + '%'

    # using parametization
    cur.execute(query, (u_input,))

    # STEP 3: fetch results
    # fetch all match columns
    query_rows = cur.fetchall()
    for rows in query_rows:
        if rows[1] == user_input:
            print(rows)

    # STEP 4: close connection
    # close cursor and db connection
    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 5:
        states_based_on_safe_user_input(args[1], args[2], args[3], args[4])
