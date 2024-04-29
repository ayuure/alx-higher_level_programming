#!/usr/bin/python3
"""Create states table in hbtn_0e_0_usa with some data"""

import MySQLdb
import sys


def take_argu(username, password, database, state_name):
    db = MySQLdb.connect(
        host="127.0.0.1", port=3306,
        user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (state_name + '%',))
    states = cur.fetchall()


    for state_name in states:
        print(state_name)

    cur.close()
    db.close()

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:]
    take_argu(username, password, database, state_name)