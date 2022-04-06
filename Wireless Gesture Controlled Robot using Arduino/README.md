1) This directory contains code for controlling the Robotic Arm using your Laptop and Arduino via Bluetooth.

2) Connect your Laptop's Bluetooth to HC-05 Bluetooth attached to Arduino.

3) Clone this repository in your system and dump the Arduino_Final.ino file onto Arduino.

4) Make sure that your Bluetooth isn't connected to the Arduino while dumping the code.

**For the *Final_Gesture_control.py* program to work follow the following steps:**

**Install OpenCV Library:**

For Python3:
pip3 install opencv-python

For Python2:
pip install opencv-python

Ensure that your are using a built in Camera with your Laptop.

Incase your laptop doesn't have a built in Camera. Just change the following code:
cap = cv2.VideoCapture(0)

to:
cap = cv2.VideoCapture(1)

and change the below code:
cv2.waitKey(1)

to:
k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

**NOTE: Make sure you are using a USB Camera**


**INSTALL MEDIAPIPE LIBRARY:**

For Python3:
pip3 install mediapipe

**NOTE: Mediapipe Library supports only Python 3.7 and above. Please ensure that you install the Latest Version of Python in your System**

**INSTALLING SOCKET LIBRARY:**

For Python:
pip3 install sockets

**INSTALLING SERIAL LIBRARY:**

for Python:
pip3 install pyserial

**NOTE: Ensure that the Baud Rate is 9600 and port number will be displayed in the Arduino IDE.
Refer the below website for more details on finding the port number:
https://support.arduino.cc/hc/en-us/articles/4406856349970-Select-board-and-port-in-Arduino-IDE**
