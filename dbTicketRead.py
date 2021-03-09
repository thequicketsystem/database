import mariadb
import sys

global idList
idList = []

def helloDB():
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
        
    return conn

#function to read out incoming tickets
def readTicket(incomingID):
    conn = helloDB()
    cur = conn.cursor()

    idList.append(incomingID)
    print(idList)
    
    try:
        for each in idList:
            cur.execute("SELECT used FROM guests WHERE ticketID=%d;", (int(each),))
            result = cur.fetchall()[0][0]
            print(result)
            print(type(result))
            if result == 0:
                #working - sets used bit to 1
                cur.execute("UPDATE guests SET used=1 WHERE ticketID=%d AND used=0;", (int(each),))
                conn.commit()
                print(incomingID, "has been set to USED.")
                idList.pop(0)

            else:
                print(f"ERROR: DUPLICATE TICKET ENTRY")
                idList.pop(0)
    except mariadb.Error as e:
        print(f"Error updating ticket: {e}")
        sys.exit(1)

    print(idList)
    conn.close()


#function to set all used fields to 0 for testing purposes
def clearUsed():
    conn = helloDB()
    cur = conn.cursor()
    
    values = [123,234,345,456,567]
    
    try:
        for item in values:
            cur.execute("UPDATE guests SET used=0 WHERE ticketID=?",(item,))
            conn.commit()
            print(f"ID reset: {item}")
    except mariadb.Error as e:
        print(f"Error resetting database: {e}")
        sys.exit(1)
        
    conn.close()


#lists the current state of thetable. not working.
def listGuests():
    conn = helloDB()
    cur = conn.cursor()
    print(f"The state of this table is: ")
    query = "SELECT * FROM guests;"
    rows = []
    try:
        cur.execute(query)
        rows = cur.fetchall()
    except mariadb.Error as e:
        print(f"Error displaying table: {e}")
        sys.exit(1)

    print(f"Returning to main.")
    conn.close()
    return rows


def main():
    #loop to continuously check tickets against the db
    while True:
        #get an incoming ticket. later this will be real
        incomingID = input("Simlulated ticket is: ")
        
        if (incomingID == "exit") or (incomingID == "end"):
            #LET ME OOOOOOOOOOUT AAAAAAHHHHHHHH
            break
        elif (incomingID == "wipe") or (incomingID == "reset") or (incomingID == "clear"):
            clearUsed()
        elif (incomingID == "show") or (incomingID == "display") or (incomingID == "state"):
            rows = listGuests()
            print(rows)
        #otherwise, read the ticket
        else:
            readTicket(incomingID)

    return

main()
        
