#include <DS1302.h>
#include <Herkulex.h>
char* Read_Time;
int N0, N1, N3, N4, N6, N7;

DS1302 rtc(4, 5, 6);

void setup()
{
  rtc.halt(false);
  rtc.writeProtect(false);
  Serial.begin(115200);
  rtc.setDOW(THURSDAY);        // Set Day-of-Week to FRIDAY
  rtc.setTime(16, 00, 0);     // Set the time to 12:00:00 (24hr format)
  rtc.setDate(8, 17, 2019);   // Set the date to August 6th, 2010
  Herkulex.beginSerial1(115200);
  Herkulex.reboot(1);
  Herkulex.reboot(2);
  delay(500); 
  Herkulex.initialize();
  delay(200);
  pinMode(48, OUTPUT);
  pinMode(49, OUTPUT);
  pinMode(50, OUTPUT);
  pinMode(51, OUTPUT);
  pinMode(52, OUTPUT);
  pinMode(53, OUTPUT);
}

void loop()
{
  Read_Time = rtc.getTimeStr();
  N0 = (Read_Time[0]-48);
  N1 = (Read_Time[1]-48);
  N3 = (Read_Time[3]-48);
  N4 = (Read_Time[4]-48);
  N6 = (Read_Time[6]-48);
  N7 = (Read_Time[7]-48);
  Serial.print("and the time is: ");
  Serial.println(rtc.getTimeStr());
  if (N0 == 1 && N1 == 6) {
    Herkulex.moveOneAngle(1, -144, 1000, LED_GREEN);
    digitalWrite(48, HIGH);
    if (N6 == 0 && N7 == 0) {
      Herkulex.moveOneAngle(2, 150, 1000, LED_GREEN);
      digitalWrite(53, LOW);
    }
    else if (N6 == 1 && N7 == 0) {
      Herkulex.moveOneAngle(2, 90, 1000, LED_GREEN);
      digitalWrite(49, HIGH);
    }
    else if (N6 == 2 && N7 == 0) {
      Herkulex.moveOneAngle(2, 30, 1000, LED_BLUE);
      digitalWrite(49, LOW);
      digitalWrite(50, HIGH);
    }
    else if (N6 == 3 && N7 == 0) {
      Herkulex.moveOneAngle(2, -30, 1000, LED_GREEN);
      digitalWrite(50, LOW);
      digitalWrite(51, HIGH);
    }
    else if (N6 == 4 && N7 == 0) {
      Herkulex.moveOneAngle(2, -90, 1000, LED_BLUE);
      digitalWrite(51, LOW);
      digitalWrite(52, HIGH);
    }
    else if (N6 == 5 && N7 == 0) {
      Herkulex.moveOneAngle(2, -150, 1000, LED_GREEN);
      digitalWrite(52, LOW);
      digitalWrite(53, HIGH);
    }
    delay (10000);
  }
}
