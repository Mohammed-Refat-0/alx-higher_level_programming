#!/usr/bin/python3
"""   lists all states with a name starting with "N"
database hbtn_0e_0_usa using sqldb"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    curs.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
