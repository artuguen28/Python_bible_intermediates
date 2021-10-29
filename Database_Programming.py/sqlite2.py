#       Selecting values
import sqlite3

conn = sqlite3.connect('mydata.db')
c = conn.cursor()

c.execute("""SELECT * FROM persons;""")

# We use fetchall() method in order to get our results:
persons = c.fetchall()
for d in range(0, len(persons)):
    print(persons[d])

conn.commit()
conn.close()


