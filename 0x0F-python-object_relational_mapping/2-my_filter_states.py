#!/usr/bin/python3
"""Takes in an argument from hbtn_0e_0_usa database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY {}".format(argv[4]))
    r = cursor.fetchall()
    for row in r:
        print(row)
