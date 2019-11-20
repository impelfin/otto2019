import serial
from time import sleep

ser = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.1)
while True:
	if ser.inWaiting() > 1:
		response = ser.readline()
		print("arduino transmit data : " + str(response))
		ser.write("response")
