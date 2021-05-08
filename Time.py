# FOR SQLITE DATABASE

import time
import datetime
import sqlite3

conn = sqlite3.connect('clients.db')
curr = conn.cursor()
curr.execute('''CREATE TABLE IF NOT EXISTS reservedClients (
    ID INT PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Age INT NOT NULL,
    `Contact Number` CHAR(11),
    Address TEXT NOT NULL);''')

class Time:
    def __init__(self):
        pass
    
