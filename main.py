import Person as patient
import ClinicTime
import Time

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

        client = patient.Person(name, age, contactNum, address)
        # other processes

        

        print("\nWhat do you want to do next?")
        print("1: Appoint a checkup appoint for another patient.")
        print("2: Exit.")
        userInput = int(input("Choice: "))

if __name__ == "__main__":
    main()