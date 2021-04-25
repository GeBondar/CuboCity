#include <Stepper.h>
#define STEPS_PER_MOTOR_REVOLUTION 32   
#define STEPS_PER_OUTPUT_REVOLUTION 32 * 64

Stepper small_stepper(STEPS_PER_MOTOR_REVOLUTION, 2, 4, 3, 5);
int  Steps2Take;

int LedPin = 7;
int LedPin2 = 8;
int SwitchPin = 6;
boolean LastButton = LOW;
boolean CurrentButton = LOW;
boolean LedOn = false;

void setup()
{
  pinMode(LedPin2, OUTPUT);
  pinMode(LedPin, OUTPUT);
  pinMode(SwitchPin, INPUT);
  Serial.begin(9600);
}
void loop(){
  Serial.println(digitalRead(SwitchPin));
  if (digitalRead(SwitchPin)==HIGH)
  {
    Serial.println(digitalRead(SwitchPin));
    delay(50);
    if (digitalRead(SwitchPin)==HIGH)
    {
       if (LedOn==1)
       { 
          digitalWrite(LedPin2, LOW);
          Serial.println(digitalRead(SwitchPin));    
          digitalWrite(LedPin, HIGH);
          Steps2Take  =  STEPS_PER_OUTPUT_REVOLUTION / 4;  
          small_stepper.setSpeed(500);   
          small_stepper.step(Steps2Take);
          delay(7000);
          Serial.println("start_1");
          LedOn = 0;
      }
      else
      {   
          digitalWrite(LedPin, LOW);
          Serial.println(digitalRead(SwitchPin)); 
          digitalWrite(LedPin2, HIGH);
          Steps2Take  =  - STEPS_PER_OUTPUT_REVOLUTION / 4;  
          small_stepper.setSpeed(500);  
          small_stepper.step(Steps2Take);
          delay(7000);
          Serial.println("start_2");
          LedOn = 1; 
      }
    }
  }
 }
 
