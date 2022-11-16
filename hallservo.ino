volatile int count = 0; //volatile so it can be adjusted by interrupt (hall val)
const byte interruptPin = 2;
int interrupt;
int state = 0;
int pos = 0;


#include <Servo.h>

Servo myservo;
const int hallSensorPin = 2;
const int servoPin = 13;

void setup() {
  Serial.begin(9600);
  myservo.write(0);
  pinMode(hallSensorPin, INPUT);
  digitalWrite(2, HIGH);
  attachInterrupt(2, interrupt, LOW);
  myservo.attach(servoPin);
}

void loop()
{
  if (hallSensorPin == HIGH) {
    count++;
  } else {
    count;
  }

  state = digitalRead(hallSensorPin);
  if (count >= 7) {
    for (pos = 0; pos <= 180; pos += 180) {
      myservo.write(pos);
      delay(25);
    }
    delay(1000);
  }
  for (pos = 180; pos >= 0; pos -= 180) {
    myservo.write(pos);
    delay(25);
  }
  Serial.println(count); {
    delay(100);
  }
}


//this should trigger servo once hall sensor detects a count of 7, no rpm calculations, 
//but since it will only spin for so long before it looses energy to continue, it's unnecessary. 
//Adjust line 32 count for trigger value
//!hall sensor is on pin 2 as an interrupt, so the arduino will automatically detect changes in the sensor, so if count +1, it will update and check if it is at 7 or higher for trigger.
//i havent tested it, so i have no clue if it works but i figured i would upload it anyways haha. 
