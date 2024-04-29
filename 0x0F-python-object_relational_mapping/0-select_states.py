#!/usr/bin/python3
"""Create states table in hbtn_0e_0_usa with some data"""

import sys
import MySQLdb


def list_all_states(username, password, name):
    db = MySQLdb.connect(host="localhost",
                        port=3306, user=username, 
                        passwd=password, db=name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    list_all_states(username, password, name)
