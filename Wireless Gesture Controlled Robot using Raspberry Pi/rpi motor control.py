################################### Raspberry Pi Program for Robot Control ############################################

import socket               # For Socket Programming
import RPi.GPIO as GPIO     # For Controlling the motor in Raspberry Pi
from time import sleep      # For turning the motor off for some amt. of time



## This Program acts like the Server to receive incoming Data

Server = socket.socket()    # Creates an instance of socket for the Server
Port = 12345                # Port to host server on
maxConnections = 5
IP = "localhost"            # IP address of the Client Machine

Server.bind(('', Port))     # To bind the client and Host on the same network

# Starts server
Server.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

# Accepts the incoming connection
(Inc_data, address) = Server.accept()
print("New connection made!")

# Setting up the hardware connections for raspberry pi

Basepin = 3                 # GPIO2
Shoulderpin = 5             # GPIO3
Elbowpin = 7                # GPIO4
WristRollpin = 11           # GPIO17
WristPitchpin = 13          # GPIO27
Gripperpin = 15             # GPIO22

# Setup for Base Motor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Basepin,GPIO.OUT)
base = GPIO.PWM(Basepin,50)
base.start(2)

#Setup for Shoulder Motor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Shoulderpin,GPIO.OUT)
shoulder = GPIO.PWM(Shoulderpin,50)
shoulder.start(7)

#Setup for Elbow Motor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Elbowpin,GPIO.OUT)
Elbow = GPIO.PWM(Elbowpin,50)
Elbow.start(7)

#Setup for Wrist Roll Motor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(WristRollpin,GPIO.OUT)
wr = GPIO.PWM(WristRollpin,50)
wr.start(2)

#Setup for Wrist Pitch Motor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(WristPitchpin,GPIO.OUT)
wp = GPIO.PWM(WristPitchpin,50)
wp.start(0)

while True:
    message = Inc_data.recv(1024)   # Gets the incoming message
    message = message.decode()      # decode

    # String Manipulation to run the motors
    msg = message.split(',')
    for i in msg:
        if i == 'Bf':
            # print(i)
            base.ChangeDutyCycle(12)
        elif i == 'Br':
            # print(i)
            base.ChangeDutyCycle(2)
        elif i == 'Sf':
            # print(i)
            shoulder.ChangeDutyCycle(10)
        elif i == 'Sr':
            # print(i)
            shoulder.ChangeDutyCycle(7)
        elif i == 'Ef':
            # print(i)
            Elbow.ChangeDutyCycle(10.5)
        elif i == 'Er':
            # print(i)
            Elbow.ChangeDutyCycle(7)
        elif i == 'Wrp':
            # print(i)
            wr.ChangeDutyCycle(12.5)
        elif i == 'Wrn':
            # print(i)
            wr.ChangeDutyCycle(2)
        elif i == 'Wpf':
            # print(i)
            wp.ChangeDutyCycle(3)
        elif i == 'Wpr':
            # print(i)
            wp.ChangeDutyCycle(0)
        elif i == 'Go':
            # print(i)
        elif i == 'Gc':
            print(i)

