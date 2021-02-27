#!/usr/bin/python
import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="Shockwave42",
        host="localhost")
        #database="employees"
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

print("DEBUG: connected")

cur = conn.cursor()
print("DEBUG: cursor made")

#create the DB
cur.execute("CREATE DATABASE IF NOT EXISTS quicketsystem")
cur.execute("USE quicketsystem")
print("DEBUG: database made and selected")
#create the table and populate it
cur.execute("CREATE TABLE IF NOT EXISTS guests (userID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, lastName VARCHAR(100) NOT NULL, firstName VARCHAR(100) NOT NULL, ticketID INT NOT NULL, used INT NOT NULL)")
print("DEBUG: table made")
cur.execute("INSERT INTO guests (lastName, firstName, ticketID, used) VALUES('Mohundro', 'Drew', 123, 0), ('Pollard', 'Carol', 234, 0), ('Bigej', 'Alex', 345, 0), ('Smith', 'Gunther', 456, 0), ('Preston','May',567, 0);")
print("DEBUG: data inserted")

## DEBUG:
some_name = "Carol"
cur.execute("SELECT firstName,lastName FROM guests WHERE firstName=?", (some_name,))
# Print Result-set
for (firstName, lastName) in cur:
    print(f"First Name: {firstName}, Last Name: {lastName}")
print("DEBUG: SELECT done")

#cur.execute("SHOW DATABASES")

#retrieving information
#some_name = "Georgi"
#cur.execute("SELECT first_name,last_name FROM employees WHERE first_name=?", (some_name,))

#for first_name, last_name in cur:
#    print(f"First name: {first_name}, Last name: {last_name}")

#insert information
#try:
#    cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria","DB"))
#except mariadb.Error as e:
#    print(f"Error: {e}")

#conn.commit()
#print(f"Last Inserted ID: {cur.lastrowid}")

conn.close()
