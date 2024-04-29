#!/usr/bin/python3
"""Create states table in hbtn_0e_0_usa with some data"""

import MySQLdb
import sys


def take_argu(username, password, database, state_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        db=database
    )
    query = """
            SELECT * FROM states
            WHERE name LIKE %s
            ORDER BY states.id ASC
            """
    cur = db.cursor()
    cur.execute(query,
                (state_name + '%',))
    states = cur.fetchall()

    for state_name in states:
        print(state_name)

    cur.close()
    db.close()


if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:]
    take_argu(username, password, database, state_name)
