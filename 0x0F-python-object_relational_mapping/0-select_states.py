#!/usr/bin/python3
"""This module defines a script that runs sql queries using MySQLdb"""


# import the module
import MySQLdb


# create a connection running on localhost port 3306
db = MySQLdb.connect(
        host="localhost", port=3306, user="root",
        passwd="Obamidele2023!!!", db="hbtn_0e_0_usa",
        charset="utf8")

cur = db.cursor()  # create a cursor in MySQL python
# lists all state from db
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
query_rows = cur.fetchall()
for rows in query_rows:
    print(rows)
cur.close()
db.close()
