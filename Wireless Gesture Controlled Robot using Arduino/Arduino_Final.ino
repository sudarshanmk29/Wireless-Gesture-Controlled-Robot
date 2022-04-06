//////////////////////////////////////////////// Wireless Gesture Controlled Robotic Arm using Image processing /////////////////////////////////////////////////////////////
#include <Servo.h>
int Motor_B = 2;
int Motor_S = 3;
int Motor_E = 4;
int Motor_Wp= 5;
int Motor_Wr= 6;
int Motor_G = 7;

int Delay = 10;

Servo servo_B;
Servo servo_S;
Servo servo_E;
Servo servo_Wp;
Servo servo_Wr;
Servo servo_G;

int servo_B_Pos,servo_S_Pos, servo_E_Pos, servo_Wp_Pos, servo_Wr_Pos, servo_G_Pos;

char mydata; 

void setup() 
{
  Serial.begin(9600);         
  servo_B.attach(Motor_B);
  servo_S.attach(Motor_S);
  servo_E.attach(Motor_E);
  servo_Wp.attach(Motor_Wp);
  servo_Wr.attach(Motor_Wr);
  servo_G.attach(Motor_G);

  // Robot arm initial position
  /*servo_B_Pos = 90;
  servo_B.write(servo_B_Pos);
  servo_S_Pos = 150;
  servo_S.write(servo_S_Pos);
  servo_E_Pos = 35;
  servo_E.write(servo_E_Pos);
  servo_Wp_Pos = 140;
  servo_Wp.write(servo_Wp_Pos);
  servo_Wr_Pos = 85;
  servo_Wr.write(servo_Wr_Pos);
  servo_G_Pos = 80;
  servo_G.write(servo_G_Pos);*/
  Serial.println("Connection established...");

}

void loop() 
{
   if(Serial.available()){
      mydata = Serial.read();
   if (mydata == '0')
   {
      
        servo_B.write(180);
        delay(Delay);
      
   }
   if (mydata == '1')
   {
       
        servo_B.write(0);
        delay(Delay);
      
   }
   if (mydata == '2')
   {
      
        servo_S.write(180);
        delay(Delay);
      
   }
   if (mydata == '3')
   {
      
        servo_S.write(0);
        delay(Delay);
      
   }
   if(mydata == '4')
   {
      
        servo_E.write(180);
        delay(Delay);
      
   }
   if (mydata == '5')
   {
      
        servo_E.write(0);
        delay(Delay);
      
   }
   if(mydata == '6')
   {
      
        servo_Wp.write(180);
        delay(Delay);
      
   }
   if (mydata == '7')
   {   
      
        servo_Wp.write(0);
        delay(Delay);
      
   }
   if (mydata == '8')
   {
      
        servo_Wr.write(180);
        delay(Delay);
      
   }
   if(mydata == '9')
   {
      
        servo_Wr.write(0);
        delay(Delay);
      
   }
   if (mydata == 'A')
   {
      
        servo_G.write(180);
        delay(Delay);
  
   }
   if (mydata == 'B')
   {
      
        servo_G.write(0);
        delay(Delay);
   }
  }
   /*else
   {
      servo_B.write(servo_B_Pos);
      servo_S.write(servo_S_Pos);
      servo_E.write(servo_E_Pos);
      servo_Wp.write(servo_Wp_Pos);
      servo_Wr.write(servo_Wr_Pos);
      servo_G.write(servo_G_Pos);
   }*/
} 


  

  
