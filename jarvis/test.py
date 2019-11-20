import serial, time
SERIALPORT = "/dev/ttyAMA0"
BAUDRATE = 115200

ser = serial.Serial(SERIALPORT, BAUDRATE)

ser.timeout = 0.1

print("starting up serial monitor")

try:
	ser.open()
except Exception as e:
	print("Exception:opening serial port:"+str(e))
if ser.isOpen():
	try:
		ser.flushInput()
		ser.flushOutput()
		time.sleep(0.1)
		while True:
			ser.write(b'1')
			print("write 1")
			response = ser.readline().decode()
			print("pi3 recv data: " + str(response))
		ser.close()
	except Exception as e:
		print("error : " + str(e))
		ser.close()
	finally:
		ser.close()
		pass
else :
	print("cannot open serial port")

