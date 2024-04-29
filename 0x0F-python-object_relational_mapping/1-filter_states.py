#!/usr/bin/python3
"""Create states table in hbtn_0e_0_usa with some data"""

import sys
import MySQLdb

def list_names_n(username, password, name):
    db = MySQLdb.connect(host="127.0.0.1", port=3306, user=username, passwd=password, db=name)
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id ASC')
    stateNames = cur.fetchall()
    for name in stateNames:
        print(name)

    cur.close()
    db.close()

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]
    list_names_n(username, password, name)