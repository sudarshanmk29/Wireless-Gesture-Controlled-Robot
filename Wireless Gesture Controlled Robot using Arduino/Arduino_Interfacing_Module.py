import serial               # add Serial library for Serial communication


class Interfacing:
    def __init__(self, pno, br):
        self.portno = pno
        self.baudrate = br

    def connect(self):
        try:
            self.ser = serial.Serial(self.portno, self.baudrate, timeout=1)
            # print("Robot Connected")
        except:
            pass

    def send_Data(self, baseF, baseR, shoulderF, shoulderR, elbowF, elbowR, wrist_pitchF, wrist_pitchR, wrist_rollP, wrist_rollN, gripperO, gripperC):
        try:
            if baseF == 'Bf':
                self.ser.write(b'0')
            elif baseR == 'Br':
                self.ser.write(b'1')
            elif shoulderF == "Sf":
                self.ser.write(b'2')
            elif shoulderR == 'Sr':
                self.ser.write(b'3')
            elif elbowF == "Ef":
                self.ser.write(b'4')
            elif elbowR == 'Er':
                self.ser.write(b'5')
            elif wrist_pitchF == "Wpf":
                self.ser.write(b'6')
            elif wrist_pitchR == 'Wpr':
                self.ser.write(b'7')
            elif wrist_rollP == 'Wrp':
                self.ser.write(b'8')
            elif wrist_rollN == 'Wrn':
                self.ser.write(b'9')
            elif gripperO == "Go":
                self.ser.write(b'A')
            elif gripperC == 'Gc':
                self.ser.write(b'B')
            elif baseF == '0':
                self.ser.write(b'C')
            elif baseR == '1':
                self.ser.write(b'D')
            elif shoulderF == '2':
                self.ser.write(b'E')
            elif shoulderR == '3':
                self.ser.write(b'F')
            elif elbowF == '4':
                self.ser.write(b'G')
            elif elbowR == '5':
                self.ser.write(b'H')
            elif wrist_pitchF == '6':
                self.ser.write(b'I')
            elif wrist_pitchR == '7':
                self.ser.write(b'J')
            elif wrist_rollP == '8':
                self.ser.write(b'K')
            elif wrist_rollN == '9':
                self.ser.write(b'L')
            elif gripperO == '10':
                self.ser.write(b'M')
            elif gripperC == '11':
                self.ser.write(b'N')

            print("DataSent")
        except:
            print("Data not sent")
            pass

