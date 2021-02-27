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

#now we need to figure out logic for handling incoming IDs
incomingID = "0"   #temp variable
pastID = "0"

#TODO: make these stmts modular
#cur.execute("USE quicketsystem")
print("Now using database quicketsystem")

incomingID = str(input("Simlulated ticket is: "))

try:
    #cur.execute("SELECT * FROM guests WHERE ticketID=%s AND used=0 FOR UPDATE", (incomingID,))
    #cur.execute("UPDATE guest SET used=1 WHERE ticketID=%s", (incomingID))
    cur.execute("UPDATE guests SET used=1 WHERE ticketID=? AND used=0", (incomingID,))
    #cur.commit()
    print("DEBUG: select thingy done")
except mariadb.Error as e:
    print(f"Error checking ticket: {e}")
    sys.exit(1)

conn.close()
