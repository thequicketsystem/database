import mariadb
import sys

#function to read out incoming tickets
def readTicket(cur, incomingID, conn):
    try:
        cur.execute("UPDATE guests SET used=1 WHERE ticketID=? AND used=0", (incomingID,))
        conn.commit()
        cur.execute("SELECT ROW_COUNT()")
        #currently only says there's no result set
        result = cur.fetchall()
        if result != 0:
            print(incomingID, "has been set to USED.")
        else:
            print(f"ERROR: DUPLICATE TICKET ENTRY")
            return
    except mariadb.Error as e:
        print(f"Error updating ticket: {e}")
        sys.exit(1)


#function to set all used fields to 0 for testing purposes
def clearUsed(cur, conn):
    values = [123,234,345,456,567]
    try:
        for item in values:
            cur.execute("UPDATE guests SET used=0 WHERE ticketID=?",(item,))
            conn.commit()
            print(f"ID reset: {item}")
    except mariadb.Error as e:
        print(f"Error resetting database: {e}")
        sys.exit(1)


#lists the current state of thetable. not working.
def listGuests(cur, conn):
    #values = [123,234,345,456,567]
    print(f"The state of this table is: ")
    try:
        #cur.execute("SELECT * FROM guests")
        #rows = cur.fetchall()
        #for line in rows:
        #    print(line)
        cur.execute("SELECT * FROM guests")
        while True:
            row = cur.fetchone()
            if not row:
                return
            print(row)
    except mariadb.Error as e:
        print(f"Error displaying table: {e}")
        sys.exit(1)


def main():
    #set up our db connection
    try:
        conn = mariadb.connect(
        user="root",
        password="quicket",
        host="localhost",
        database="quicketsystem")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    #establish our cursor
    print("We have connected to the", conn.database, "database.")
    print("Server is", conn.server_name)
    cur = conn.cursor()

    #loop to continuously check tickets against the db
    while True:
        #get an incoming ticket. later this will be real
        incomingID = str(input("Simlulated ticket is: "))
        
        if (incomingID == "exit") or (incomingID == "end"):
            #LET ME OOOOOOOOOOUT AAAAAAHHHHHHHH
            break
        elif (incomingID == "wipe") or (incomingID == "reset") or (incomingID == "clear"):
            clearUsed(cur,conn)
        elif (incomingID == "show") or (incomingID == "display") or (incomingID == "state"):
            listGuests(cur,conn)
        #otherwise, read the ticket
        else:
            readTicket(cur, incomingID, conn)

    #close out our connection now that we're all done
    conn.close()

    return

main()
        
