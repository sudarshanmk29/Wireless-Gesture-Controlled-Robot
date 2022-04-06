import cv2
import Hand_Tracking_Module as htm  # Importing custom made module
import Arduino_Interfacing_Module as aim
import time

# Opening the WebCam
cap = cv2.VideoCapture(0)
cap.set(10, 500)

# Setting the Webcam video Window size
cap.set(3, 700)
cap.set(4, 700)

portNumber = 'COM9'
BaudRate = 9600
previous_time = 0  # for FPS
current_time = 0  # for FPS

# defining a list of the tip id's as per the mediapipe package specification
tipnum = [4, 8, 12, 16, 20]


Interface = aim.Interfacing(portNumber, BaudRate)


def Base_Motor_Forward(finger):
    if finger[0] == finger[1] == finger[2] == finger[3] == finger[4] == 0:
        cv2.putText(frame, "Base forward", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Bf'

def Base_Motor_Reverse(finger):
    if finger[0] == 1 and finger[1] == finger[2] == finger[3] == finger[4] == 0:
        cv2.putText(frame, "Base Reverse", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Br'

def Shoulder_Motor_Forward(finger):
    if finger[1] == 1 and finger[0] == finger[2] == finger[3] == finger[4] == 0:
        cv2.putText(frame, "Shoulder forward", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Sf'

def Shoulder_Motor_Reverse(finger):
    if finger[1] == finger[0] == 1 and finger[2] == finger[3] == finger[4] == 0:
        cv2.putText(frame, "Shoulder reverse", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Sr'

def Elbow_Motor_forward(finger):
    if finger[2] == 1 and finger[0] == finger[1] == finger[3] == finger[4] == 0:
        cv2.putText(frame, "Elbow forward", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Ef'

def Elbow_Motor_Reverse(finger):
    if finger[2] == finger[1] == 1 and finger[0] == finger[3] == finger[4] == 0:
        cv2.putText(frame, "Elbow reverse", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Er'

def Wrist_Motor_Pitch_forward(finger):
    if finger[0] == finger[1] == finger[2] == 1 and finger[3] == finger[4] == 0:
        cv2.putText(frame, "Wrist Pitch Forward", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Wpf'

def Wrist_Motor_Pitch_reverse(finger):
    if finger[1] == finger[2] == finger[4] == 1 and finger[0] == finger[3] == 0:
        cv2.putText(frame, "Wrist Pitch Reverse", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Wpr'

def Wrist_Motor_Roll_positive(finger):
    if finger[1] == finger[4] == 1 and finger[0] == finger[2] == finger[3] == 0:
        cv2.putText(frame, "wrist roll positive", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Wrp'

def Wrist_Motor_Roll_negative(finger):
    if finger[0] == finger[4] == 1 and finger[1] == finger[2] == finger[3] == 0:
        cv2.putText(frame, "wrist roll negative", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Wrn'

def Gripper_Open(finger):
    if finger[4] == 1 and finger[0] == finger[1] == finger[2] == finger[3] == 0:
        cv2.putText(frame, "Gripper Open", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Go'

def Gripper_Close(finger):
    if finger[2] == finger[3] == finger[4] == 1 and finger[0] == finger[1] == 0:
        cv2.putText(frame, "Gripper close", (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        return 'Gc'


# Defining an object for the Hand_Detector class in the Hand_Tracking_Module
detector = htm.Hand_Detector(detectionCon=0.7)

while True:
    # To capture the video feed as images
    check, frame = cap.read()
    # to find the landmarks on the hand
    frame = detector.findHands(frame, draw=False)
    # Save the Landmarks on the hand as a list
    lmlist = detector.find_Position(frame, draw=False)

    Interface.connect()  # To connect with Arduino

    # If there are elements in the list then only we can proceed
    if len(lmlist) != 0:
        fingers = []  # List to get the fingers.We use this list for our Robot project

        # Thumb
        if lmlist[tipnum[0]][1] > lmlist[tipnum[0] - 1][1]:  # Here on the x axis if the tip of the Thumb is
            fingers.append(1)  # to the right of landmark 3; then 1 is added to
            # the fingers list else 0 is added
        else:
            fingers.append(0)

        # 4 fingers
        for ID in range(1, 5):
            if lmlist[tipnum[ID]][2] < lmlist[tipnum[ID] - 2][2]:  # Here on the y axis if the tip of the
                fingers.append(1)  # remaining 4 fingers is above the first
                # point from the bottom of the finger then
                # 1 is appended to the fingers list else
                # 0 is appended
            else:
                fingers.append(0)

        Bf = Base_Motor_Forward(fingers)
        Br = Base_Motor_Reverse(fingers)
        Sf = Shoulder_Motor_Forward(fingers)
        Sr = Shoulder_Motor_Reverse(fingers)
        Ef = Elbow_Motor_forward(fingers)
        Er = Elbow_Motor_Reverse(fingers)
        Wpf = Wrist_Motor_Pitch_forward(fingers)
        Wpr = Wrist_Motor_Pitch_reverse(fingers)
        Wrp = Wrist_Motor_Roll_positive(fingers)
        Wrn = Wrist_Motor_Roll_negative(fingers)
        Go = Gripper_Open(fingers)
        Gc = Gripper_Close(fingers)


        Interface.send_Data(Bf, Br, Sf, Sr, Ef, Er, Wpf, Wpr, Wrp, Wrn, Go, Gc)

    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time
    cv2.putText(frame, f"FPS:{str(int(fps))}", (10, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

    # To show WebCam feed on the screen
    cv2.imshow("Finger Counting", frame)
    cv2.waitKey(1)
