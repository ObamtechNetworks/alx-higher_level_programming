#!/usr/bin/python3
"""
This module defines a script that runs sql queries using MySQLdb
"""


# import the MySQLdb module
import MySQLdb
import sys

# create a func for this


def show_states_based_on_user_input(username, password, dbname, user_input):
    """
    Lists states based on user input  using MySQLdb module.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        dbname (str): Database name to use
        user_input (str): User input, string to search for

    Returns:
        None
    """

    # STEP 1: create a connection running on localhost port 3306
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=dbname,
            charset="utf8")

    # STEP 2: create a cursor
    cur = db.cursor()  # create a cursor in MySQL python

    # QUERY that lists all state from db where name matches user's input
    query = """
    SELECT * FROM states WHERE name LIKE '{:s}'
    ORDER BY states.id ASC
    """.format(user_input)

    # STEP 3: execute the SQL query
    cur.execute(query)

    # STEP 4: fetch results
    query_rows = cur.fetchall()
    for rows in query_rows:
        if rows[1] == user_input:
            print(rows)

    # STEP 4(cleanup): close cursor and db connection
    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 5:
        states_based_on_user_input(args[1], args[2], args[3], args[4])
