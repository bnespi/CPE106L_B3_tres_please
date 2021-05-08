from Person import Person
import ClinicTime
import Time as timee
from Schedule import Schedule
import sqlite3
import datetime

def main():
    ''' While the app operator does not input "quit" criteria, continue asking for 
    every patient's information. This would mean that for every patient, 
    a new Person object will be instantiated. '''
    
    # variables
    ticket = 0
    # conn = sqlite3.connect('clients.db')

    print("Good Day!\n")
    
    print("What do you want to do today?")
    print("1: Appoint a checkup appointment for a new patient.")
    print("2: Exit.")
    userInput = int(input("Choice: "))

    while (userInput != 2):
        print("\nPlease enter your details below: \n")
        name = input("Name: ")
        age = int(input("Age: "))
        contactNum = input("Contact Number: ")
        address = input("Address: ")

        client = Person(name, age, contactNum, address)
        ticket += 1
        # other processes
        print("\nWhen do you want to set appointment?")
        userDate = input("Preferred Date: ") # to get user's preferred date
        userTime = input("Preferred Time: ") # to get user's preferred time
        client.sched = Schedule(userDate, userTime)
        print(client.sched)
        print(client.sched.wholeDateTime)
        
        clientTuple = (ticket, name, age, contactNum, address, datetime.datetime.strptime(userDate + " 2021 " + userTime, "%B %d %Y %I:%M %p"))
        newClientSlot = timee.Time()
        conn = newClientSlot.initializeDB('clients.db')
        newClientSlot.addData(conn, clientTuple)
        # newClientSlot.curr.execute('''INSERT INTO 'reservedClients' ('ID', 'Name', 'Age', 'Contact Number', 'Address', 'Reserved Date and Time') VALUES (?, ?, ?, ?, ?, ?);, clientTuple''')
        # newClientSlot.conn.commit()
        
        

        print("\nWhat do you want to do next?")
        print("1: Appoint a checkup appoint for another patient.")
        print("2: Exit.")
        userInput = int(input("Choice: "))

if __name__ == "__main__":
    main()