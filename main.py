from Person import Person
from pyzbar.pyzbar import decode #for decoding qrcode
import qrcode as qr
import cv2 as cv
import numpy as np
import Time as timee
from Schedule import Schedule
import os


def prompt():
    print("1: Schedule a checkup appointment for a new patient.")
    print('2: Scan your schedule qr')
    print("3: Exit.")
    uInput = int(input("Choice: "))
    return uInput


def prompt_details():
    print("\nPlease enter your details below: \n")
    name = input("Name: ")
    age = int(input("Age: "))
    contactNum = input("Contact Number: ")
    address = input("Address: ")
    return (name, age, contactNum, address)



def convert_to_str(t):
    return (t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"), t.strftime("%H:%M:%S"))


def main():
    ''' While the app operator does not input "quit" criteria, continue asking for 
    every patient's information. This would mean that for every patient, 
    a new Person object will be instantiated. '''

    print("\tWelcome to Consultation Scheduler\n")
    userInput = prompt()

    print("What do you want to do today?")

    while userInput != 3:
        if userInput == 1: # creates new appointment schedule
            name, age, contactNum, address = prompt_details()

            client = Person(name, age, contactNum, address) # new instance of Person object

            print("\nWhen do you want to set appointment?\nOffice Hours: 9AM-5PM, Monday to Friday")
            # in a while loop because the appointment date must be in HH:00 format
            while True:
                userDate = input("Preferred Date (Month Name/Day): ") # to get user's preferred date
                userTime = input("Preferred Time (HH:00 AM/PM): ") # to get user's preferred time
                # comparison code block should come in here

                if 'AM' in userTime:#if scheduled in the morning
                    # only 9-11AM is allowed
                    if 11 >= userTime[0:userTime.find(':')] >= 9:
                        print('Clinic opens at 9AM')
                        #prompt again
                elif 'PM' in userTime: #if scheduled in the afternoon
                    if userTime[0:userTime.find(':')] >= 5:
                        print('Clinic closes at 5PM')
                elif userTime[userTime.find(':')+1: userTime.find(' ')] != '00':
                    print("Sorry but we only accept hourly reservations, i.e. 8:00 am")
                else:
                    break

            # process of inserting time slot into database (once confirmed to be available)
            client.sched = Schedule(userDate, userTime)

            clientSchedule = (client.sched.wholeDateTime)
            clientTuple = (name, age, contactNum, address, clientSchedule)
            newClientSlot = timee.Time() # new instance of Time class to be inserted into database
            conn = newClientSlot.initializeDB('clients.db') # create connection to sqlite3 database

            # Getting the Date and Time data from the SQLite Database
            curr = conn.cursor()
            curr.execute("SELECT DateandTime FROM reservedClients")
            results = curr.fetchall()

            # Converting the SQLite database into a list since it was in a tuple from SQLite
            convertData = [(i[0]) for i in results]

            # Converting the user input which was a date.time object into a str type variable
            time = clientSchedule
            year, month, day, time = convert_to_str(time)

            date_time = year + "-" + month + "-" + day + " " + time

            found = date_time in convertData
            curr.close()

            # if the chosen schedule is not in the data base
            if found == False:
                x = newClientSlot.addData(conn, clientTuple)

                # confirmation of time slot reservation
                print("Success! The summary of your appointment is found below.")
                print(client.sched)
                # print(client.name+'\n'+str(client.sched.wholeDateTime))
                client_qr = qr.make(client.name + '\n' + str(client.sched.wholeDateTime))
                client_qr.save(os.getcwd() + '\\client_qr\\' + client.name + str(x) + '.jpg')

                qrjpg = cv.imread('client_qr\\' + client.name + str(x) + '.jpg')
                cv.imshow('Your QR Code', qrjpg)
                cv.waitKey(1)
                input()
                cv.destroyAllWindows()
                # generation of the qr code block should come in here

            # if the chosen schedule is in the database
            else:
                print("The timeslot you have selected is already taken.")
            

        # variable scanned_data is essential in this part
        # scanned_data holds the name and the wholeDateTime
        elif userInput == 2:

            #setup for vision
            cap = cv.VideoCapture(0)  # VideoCapture(arg) where arg states which camera to use
            cap.set(3, 1080)  # 3 - width
            cap.set(3, 720)  # 4 - height

            #setup for database checking
            checkClientSlot = timee.Time()  # new instance of Time class to be inserted into database
            conn = checkClientSlot.initializeDB('clients.db')  # create connection to sqlite3 database
            curr = conn.cursor()

            while True:
                success, image = cap.read()
                decoded = None
                # success is a boolean variable
                # image is the video feed

                for barcode in decode(image):
                    if barcode != []:
                        scanned_data = barcode.data.decode('utf-8')
                        name = scanned_data[0:scanned_data.find('\n')]
                        date_and_time = scanned_data[scanned_data.find('\n')+1:]

                        command = "SELECT Name,DateandTime FROM reservedClients WHERE Name = ? AND DateandTime = ?"
                        curr.execute(command, (name, date_and_time))
                        from_db = curr.fetchall()

                        if (name, date_and_time) in from_db:
                            pts = np.array([barcode.polygon], np.int32)
                            pts = pts.reshape((-1, 1, 2))
                            cv.polylines(image, [pts], True, (0, 255, 0), 5)
                            enclosure = barcode.rect
                            cv.putText(image, name,
                                       (enclosure[2], enclosure[1]),
                                        cv.FONT_ITALIC, 0.3,
                                        (255, 0, 0), 1)
                        else:
                            pts = np.array([barcode.polygon], np.int32)
                            pts = pts.reshape((-1, 1, 2))
                            cv.polylines(image, [pts], True, (0, 0, 255), 5)
                            enclosure = barcode.rect

                cv.imshow('QR Scanner', image)
                cv.waitKey(1)
                if decoded != None:
                    cv.destroyWindow('QR Scanner')
                    break




        # prompt for next action to do, exit program if "quit" criterias was satisfied
        print("\nWhat do you want to do next?")
        userInput = prompt()
    
    print("Thank you for using Consultation Scheduler. Have a great day!")

if __name__ == "__main__":
    main()