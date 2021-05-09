# Consultation Scheduler
Group tres please code source for Software Design Laboratory Project.

## Project Description

  The project "Consultation Scheduler" is viewed to be implemented for clinics. It aims to create a no-contact transaction on patient scheduling. The patient only needs to show their qr code so that he/she won't need to write on any forms anymore. This reduces the contact needed to relay information. 


## Features:
  - will use the PyQt GUI toolkit to implement the GUI of our software project
  - most establishments nowadays require people to write on a piece of paper their information. 
    With this scheduler, a person only needs to hold on their qr code to have those information on the fly.
  - a specific qr code will be created when the patient has chosen a specific time for his/her appointment
     the info on this qr code will be:
     1. Name
     2. Age
     3. Contact Number
     4. Address
     5. Date and Time of Consultation


## Installation
This program used external dependencies. Install them first before running. 
1. Open command prompt. 
2. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install "pyzbar" module and its scripts. 
```bash
pip install pyzbar
pip install pyzbar[scripts]
```
3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install "qrcode" module.
```bash
pip install qrcode[pil]
```
4. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install "OpenCV-Python" module.
```bash
pip install opencv-python
```
5. Run the program.

## Developers
1. Carcellar, Mon Timothy Isaac M.
2. Espiritu, Joseph Benedict B.
3. Ugale, Rionne Angelo