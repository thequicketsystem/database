import mariadb
import sys

def readTicket(cur, incomingID):
    try:
        cur.execute("UPDATE guests SET used=1 WHERE ticketID=? AND used=0", (incomingID,))
        print(incomingID, "has been set to USED.")
    except mariadb.Error as e:
        print(f"Error updating ticket: {e}")
        sys.exit(1)

    return

def main():
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
    
    while True:
        incomingID = str(input("Simlulated ticket is: "))
        
        if (incomingID == "exit") or (incomingID == "Exit"):
            break
        else:
            readTicket(cur, incomingID)
            
    conn.close()

    return

main()
        
