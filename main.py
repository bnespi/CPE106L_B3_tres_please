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

        client = Person(name, age, contactNum, address) # new instance of Person object
        
        
        print("\nWhen do you want to set appointment?")
        userDate = input("Preferred Date: ") # to get user's preferred date
        userTime = input("Preferred Time: ") # to get user's preferred time
        # comparison code block should come in here
        
        
        # process of inserting time slot into database (once confirmed to be available)
        clientTuple = (name, age, contactNum, address, client.sched.wholeDateTime)
        newClientSlot = timee.Time() # new instance of Time class to be inserted into database
        conn = newClientSlot.initializeDB('clients.db')
        newClientSlot.addData(conn, clientTuple)

        # confirmation of time slot reservation
        client.sched = Schedule(userDate, userTime)
        print(client.sched)

        # generation of the qr code block should come in here
        # https://betterprogramming.pub/how-to-generate-and-decode-qr-codes-in-python-a933bce56fd0
        # link above might help us for this
        
        
        # prompt for next action to do, exit program if "quit" criterias was satisfied
        print("\nWhat do you want to do next?")
        print("1: Appoint a checkup appointment for another patient.")
        print("2: Exit.")
        userInput = int(input("Choice: "))

if __name__ == "__main__":
    main()