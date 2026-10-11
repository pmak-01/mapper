#include <Servo.h>

Servo servo1;
int servo_pin = 10;
int angle, max_angle = 150, min_angle = 30, del_angle = 10;
int servo_del = 100;

int trig_pin = 12, echo_pin = 11;
int ping_time, ping_del = 10;
double dist;

int measure_button_pin = 8, measure_button_val;
int end_button_pin = 7, end_button_val;

double data[13]; // length = max_angle - min_angle + 1

void setup() {
  servo1.attach(servo_pin);

  pinMode(trig_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  pinMode(measure_button_pin, INPUT_PULLUP);
  pinMode(end_button_pin, INPUT_PULLUP);

  Serial.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(measure_button_pin) == LOW)
    measure();
  if (digitalRead(end_button_pin) == LOW)
    Serial.println("END");
  delay(servo_del);
}

double get_distance() {
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(ping_del);
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(ping_del);
  digitalWrite(trig_pin, LOW);

  ping_time = pulseIn(echo_pin, HIGH);

  dist = 0.343 * ping_time / 2.0; // in mm
  return dist;
}

void measure() {
  int i = 0;
  for (angle = min_angle; angle <= max_angle; angle += del_angle, ++i) {
    servo1.write(angle);
    delay(servo_del);
    data[i] = get_distance();
    delay(servo_del);
  }
  servo1.write(min_angle);

  for (double d : data) {
    Serial.print(d);
    Serial.print(", ");
  }

  Serial.println();
}