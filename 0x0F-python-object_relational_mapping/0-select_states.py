#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd="", db=argv[2], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cur.fetchall()
    for row in states:
        print(row)
    cur.close()
    conn.close()
