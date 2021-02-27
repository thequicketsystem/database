import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="quicket",
        host="localhost",
        database="quicketsystem")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

print("We have connected to the database.")

cur = conn.cursor()
#print("DEBUG: cursor made")
