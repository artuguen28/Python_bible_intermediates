import sqlite3

#       Classes and tables

class Person():
    def __init__(self, first=None,
        last=None, age=None):
        self.first = first
        self.last = last
        self.age = age

    def clone_person(self, result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]


#       From table to object

conn = sqlite3.connect('mydata.db')
c = conn.cursor()

c.execute("""SELECT * FROM persons
    WHERE last_name = 'Smith'""")

person1 = Person()
person1.clone_person(c.fetchone())

print(person1.first)
print(person1.last)
print(person1.age)

#       From object to table

person2 = Person("Bob", "Davis", 23)
c.execute(f"""INSERT INTO persons VALUES
    ('{person2.first}', '{person2.last}', '{person2.age}')""")
    
conn.commit()
conn.close()

