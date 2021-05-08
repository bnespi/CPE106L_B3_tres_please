from Person import Person
import ClinicTime
import Time
from Schedule import Schedule

def main():
    ''' While the app operator does not input "quit" criteria, continue asking for 
    every patient's information. This would mean that for every patient, 
    a new Person object will be instantiated. '''
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
        # other processes
        print("\nWhen do you want to set appointment?")
        userDate = input("Preferred Date: ") # to get individual month and day
        userTime = input("Preferred Time: ") # to get individual hour and minute
        '''month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        hour = int(input("Enter hour: "))
        minute = int(input("Enter minute: "))
        client.sched = Schedule.Schedule(month, day, hour, minute)
        print(client.sched)'''
        client.sched = Schedule(userDate, userTime)
        print(client.sched)
        

        print("\nWhat do you want to do next?")
        print("1: Appoint a checkup appoint for another patient.")
        print("2: Exit.")
        userInput = int(input("Choice: "))

if __name__ == "__main__":
    main()