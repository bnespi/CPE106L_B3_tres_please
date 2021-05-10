# FOR SQLITE DATABASE

import time
import datetime
import sqlite3

class Time:
    def __init__(self):
        pass
    
    def initializeDB(self, fileName):
        return sqlite3.connect(fileName)

    def addData(self, conn, tupleData):
        curr = conn.cursor()
        curr.execute('''
            INSERT OR REPLACE INTO 
            reservedClients ('Name', 'Age', 'Contact Number', 'Address', 'DateandTime') 
            VALUES (?, ?, ?, ?, ?)
                    ''', tupleData)
        conn.commit()
        return curr.lastrowid
    