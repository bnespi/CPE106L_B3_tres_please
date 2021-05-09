# FOR SQLITE DATABASE

import time
import datetime
import sqlite3
import os


class Time:
    def __init__(self):
        pass
    
    def initializeDB(self, fileName):
        return sqlite3.connect(os.getcwd()+'\\CPE106L_B3_tres_please\\'+fileName)

    def addData(self, conn, tupleData):
        curr = conn.cursor()
        curr.execute('''
            INSERT OR REPLACE INTO 
            reservedClients ('Name', 'Age', 'Contact Number', 'Address', 'Date and Time') 
            VALUES (?, ?, ?, ?, ?)
                    ''', tupleData)
        conn.commit()
        return curr.lastrowid
    