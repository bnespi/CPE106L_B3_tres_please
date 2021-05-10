from Person import Person
from pyzbar.pyzbar import decode #for decoding qrcode
from datetime import datetime
import qrcode as qr
import cv2 as cv
import numpy as np
import ClinicTime
import Time as timee
from Schedule import Schedule
import sqlite3
import os


def main():
    ''' While the app operator does not input "quit" criteria, continue asking for 
    every patient's information. This would mean that for every patient, 
    a new Person object will be instantiated. '''
    
    # variables

    print("Good Day!\n")
    
    print("What do you want to do today?")
    print("1: Schedule a checkup appointment for a new patient.")
    print('2: Scan your schedule qr')
    print("3: Exit.")
    userInput = int(input("Choice: "))

    while userInput != 3:
        if userInput == 1:
           
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
            
        
            # processt of inserting time slot into database (once confirmed o be available)
            client.sched = Schedule(userDate, userTime)

           

            clientTuple = (name, age, contactNum, address, client.sched.wholeDateTime)
            
            clientSchedule = (client.sched.wholeDateTime)
            newClientSlot = timee.Time() # new instance of Time class to be inserted into database
            
            conn = newClientSlot.initializeDB('clients.db')
            

            # Getting the Date and Time data from the SQLite Database
            cur = conn.cursor()
            cur.execute("SELECT DateandTime FROM reservedClients")
            results = cur.fetchall()
            #Converting the SQLite database into a list since it was in a tuple from SQLite
            convertData=[(i[0]) for i in results]
           
            # Converting the user input which was a date.time object into a str type variable 
            time = clientSchedule
            year = time.strftime("%Y")
            month = time.strftime("%m")
            day = time.strftime("%d")
            time = time.strftime("%H:%M:%S")

            date_time = year + "-" + month + "-" + day + " " + time
           
            # Checking if the chosen timeslot of the user is already taken 
            x = 0
            found = False
            for each_value in convertData:
                
                if convertData[x] == date_time:
                    found = True
                    break
                x = x + 1
           


            cur.close()


            #if the chosen schedule is not in the data base
            if found == False:
                x = newClientSlot.addData(conn, clientTuple)
            #confirm schedule here


            # confirmation of time slot reservation
            #print(client.name+'\n'+str(client.sched.wholeDateTime))

            # generation of the qr code block should come in here
            # https://betterprogramming.pub/how-to-generate-and-decode-qr-codes-in-python-a933bce56fd0
            # link above might help us for this
                client_qr = qr.make(client.name+'\n'+str(client.sched.wholeDateTime))
                client_qr.save(os.getcwd()+'\\client_qr\\'+client.name+str(x)+'.jpg')

            #if the chosen schedule is in the database
            else:
                print("The timeslot you have selected is already taken")
            

        #variable scanned_data is essential in this part
        #scanned_data holds the name and the wholeDateTime

        elif userInput == 2:
            cap = cv.VideoCapture(0)  # VideoCapture(arg) where arg states which camera to use
            cap.set(3, 1080)  # 3 - width
            cap.set(3, 720)  # 4 - height

            while True:
                success, image = cap.read()
                decoded = None
                # success is a boolean variable
                # image is the video feed

                for barcode in decode(image):
                    if barcode != []:
                        scanned_data = barcode.data.decode('utf-8')
                        print(scanned_data)
                        pts = np.array([barcode.polygon], np.int32)
                        pts = pts.reshape((-1, 1, 2))
                        cv.polylines(image, [pts], True, (0, 255, 0), 5)
                        enclosure = barcode.rect
                        cv.putText(image, scanned_data[6:scanned_data.find('\n')],
                                   (enclosure[2], enclosure[1]),
                                    cv.FONT_ITALIC, 0.3,
                                    (255, 0, 0), 1)
                    decoded = barcode


                cv.imshow('QR Scanner', image)
                cv.waitKey(1)
                if decoded != None:
                    cv.destroyWindow('QR Scanner')
                    break
                # if arg is 0 or -1 then the program runs eternally
                # if arg is 1 then it waits for a click
        # prompt for next action to do, exit program if "quit" criterias was satisfied
        print("\nWhat do you want to do next?")
        print("1: Schedule a checkup appointment for a new patient.")
        print('2: Scan your schedule qr')
        print("3: Exit.")
        userInput = int(input("Choice: "))

if __name__ == "__main__":
    main()








    """
    Program sequence:
	Asks the user what to do
		if (make schedule)
			ask for name, age, contact, and address
			ask for preferred date and time
			check whether date and time is available (wala pa)
			if (available)
				confirm schedule
				generate qr code
			else
				input date and time again (wala pa)
			ask the user what to do next
		else if (decode qr code) -> wala pa
			input image file
			decode
		else
			exit
            
    """