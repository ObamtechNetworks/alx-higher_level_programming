#!/usr/bin/python3
"""
This module defines a script that runs sql queries using MySQLdb
It lists all states
"""


# import the MySQLdb module
import MySQLdb
import sys

# create a func for this


def list_states(username, password, dbname):
    """
    lists states using MySQLdb module
    Args:
        (username):(str) -> the sql database username
        (password):(str) -> password of the sql database
        (dbname):(str) -> the database to use
    """
    # FOLLOW THE STEPS IN USING MySQLdb

    # STEP 1: create a connection running on localhost with port 3306
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=dbname,
            charset="utf8")

    # STEP 2: create a cursor
    cur = db.cursor()  # create a cursor in MySQL python

    # STEP 3: BEGIN TO EXECUTE QUERIES
    # lists all state from db, first create the basic SQL query
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    # STEP 4: FETCH RESULT, USING fetchall since
    query_rows = cur.fetchall()
    for rows in query_rows:
        print(rows)

    # close cursor and db connection
    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        list_states(args[1], args[2], args[3])
