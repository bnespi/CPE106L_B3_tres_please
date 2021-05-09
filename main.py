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
        
        print("\nWhen do you want to set appointment?")
        userDate = input("Preferred Date: ") # to get user's preferred date
        userTime = input("Preferred Time: ") # to get user's preferred time
        client.sched = Schedule(userDate, userTime)
        print(client.sched)
        print(client.sched.wholeDateTime)
        
        clientTuple = (ticket, name, age, contactNum, address, client.sched.wholeDateTime)
        newClientSlot = timee.Time()
        conn = newClientSlot.initializeDB('clients.db')
        newClientSlot.addData(conn, clientTuple)
        
        
        

        print("\nWhat do you want to do next?")
        print("1: Appoint a checkup appointment for another patient.")
        print("2: Exit.")
        userInput = int(input("Choice: "))

if __name__ == "__main__":
    main()