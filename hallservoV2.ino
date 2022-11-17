volatile int count = 0; //volatile so it can be adjusted by interrupt (hall val)
const byte interruptPin = 2;
int interrupt;
int state;
int pos = 0;

#include <Servo.h>

Servo myservo;
const int hallpin = 2;
const int servoPin = 13;
float hallthresh = 7.0; //CHANGE FOR ACTIVATION

void setup() {
  Serial.begin(9600);
  myservo.write(0);
  pinMode(hallpin, INPUT);
  digitalWrite(2, HIGH);
  attachInterrupt(2, interrupt, LOW);
  myservo.attach(servoPin);
}

void loop() {
  //pre allocate ?
  float hall_count = 1.0;
  float start = micros();
  bool on_state = false;

  while (true) {
    if (digitalRead(hallpin) == 0) {
      if (on_state == false) {
        on_state = true;
        hall_count += 1.0;
      }
    } else {
      on_state = false;
    }
    //SERVO FUNCTION!
    state = digitalRead(hallpin);
    if (hall_count >= hallthresh) {
      for (pos = 0; pos <= 180; pos += 180) {
        myservo.write(pos);
        delay(1000);
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
  //print info
  float end_time = micros();
  float time_passed = ((end_time - start) / 1000000.0);
  Serial.print("Time Passed: ");
  Serial.print(time_passed);
  Serial.println("s");
  float rpm_val = (hall_count / time_passed) * 60.0;
  Serial.print(rpm_val);
  Serial.println(" RPM");
  delay(1);
}
