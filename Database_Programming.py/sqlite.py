#       Connecting to SQLite

import sqlite3

# This command creates a new database on your disk.
conn = sqlite3.connect('mydata.db')

# To execute statements:
c = conn.cursor()

# Now we can create our first table:
c.execute("""CREATE TABLE persons (
    first_name TEXT,
    last_name TEXT,
    age INTEGER
    )""")

#  Committing to our connection:
conn.commit()

# Closing the connection:
conn.close()

