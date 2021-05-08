# FOR SQLITE DATABASE

import time
import datetime
import sqlite3



"""curr.execute('''CREATE TABLE IF NOT EXISTS reservedClients (
    ID INT PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Age INT NOT NULL,
    `Contact Number` CHAR(11),
    Address TEXT NOT NULL);''')"""

class Time:
    def __init__(self):
        pass
    
    def initializeDB(self, fileName):
        return sqlite3.connect(fileName)

    def addData(self, conn, tupleData):
        curr = conn.cursor()
        curr.execute('''INSERT OR REPLACE INTO reservedClients ('ID', 'Name', 'Age', 'Contact Number', 'Address', 'Date and Time') VALUES (?, ?, ?, ?, ?, ?)''', tupleData)
        conn.commit()
        return curr.lastrowid
    

# conn = sqlite3.connect('clients.db') # to establish connection to the database
# curr = conn.cursor()