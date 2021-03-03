import mariadb
import sys

#function to read out incoming tickets
def readTicket(cur, incomingID):
    try:
        cur.execute("UPDATE guests SET used=1 WHERE ticketID=? AND used=0", (incomingID,))
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

    return

#function to set all used fields to 0 for testing purposes (not working)
def clearUsed(cur):
    values = [123,234,345,456,567]
    try:
        for item in values:
            cur.execute("UPDATE guests SET used=0 WHERE ticketID=?",(item,))
            print(f"ID reset: {item}")
    except mariadb.Error as e:
        print(f"Error resetting database: {e}")
        sys.exit(1)

    return

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
    print("We have connected to the database.")
    cur = conn.cursor()

    #loop to continuously check tickets against the db
    while True:
        #get an incoming ticket. later this will be real
        incomingID = str(input("Simlulated ticket is: "))
        
        if (incomingID == "exit") or (incomingID == "Exit"):
            #LET ME OOOOOOOOOOUT AAAAAAHHHHHHHH
            break
        elif (incomingID == "wipe") or (incomingID == "reset") or (incomingID == "clear"):
            clearUsed(cur)
        #otherwise, read the ticket
        else:
            readTicket(cur, incomingID)

    #close out our connection now that we're all done
    conn.close()

    return

main()
        
