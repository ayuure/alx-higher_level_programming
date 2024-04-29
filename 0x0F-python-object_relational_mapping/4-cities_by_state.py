#!/usr/bin/python3
"""Create states table in hbtn_0e_0_usa with some data"""

import MySQLdb
import sys


def list_cities(username, password, database):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM cities")
    states = cur.fetchall()


    for state_name in states:
        print(state_name)

    cur.close()
    db.close()

if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    list_cities(username, password, database)