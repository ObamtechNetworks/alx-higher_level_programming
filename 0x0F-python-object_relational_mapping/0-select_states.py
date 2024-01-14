#!/usr/bin/python3
"""Thismodule defines a script that runs sql queries using MySQLdb"""


# import the module
import MySQLdb
import sys

# create a func for this


def states_lists(username, password, dbname):
    """lists states using MySQLdb module"""
    # create a connection running on localhost port 3306
    db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=dbname,
            charset="utf8")

    cur = db.cursor()  # create a cursor in MySQL python

    # lists all state from db
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for rows in query_rows:
        print(rows)

    # close cursor and db connection
    cur.close()
    db.close()


if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        states_lists(args[1], args[2], args[3])
