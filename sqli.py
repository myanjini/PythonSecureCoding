import sys
import sqlite3

title = sys.argv[1]
query = "select * from albums where title like '%%%s%%'" % title
try:
    conn = sqlite3.connect('chinook.db')
    curs = conn.cursor()

    for row in curs.execute(query):
        print(row)
except sqlite3.Error as e:
    print(e)
finally:
    curs.close()
    conn.close()
