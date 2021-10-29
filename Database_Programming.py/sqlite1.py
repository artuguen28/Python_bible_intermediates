#        Inserting values

import sqlite3

conn = sqlite3.connect('mydata.db')
c = conn.cursor()

# These are the 3 values that are being inserting on our table:
c.execute("""INSERT INTO persons VALUES
    ('John', 'Smith', 25),
    ('Anna', 'Smith', 30),
    ('Mike', 'Johnson', 40)""")

conn.commit()

conn.close()
