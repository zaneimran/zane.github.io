#!/usr/bin python
import serial, time
port = serial.Serial("/dev/ttyAMA0", baudrate=2400)

while True:
	rvc = port.readline()
	if(rvc):
		print ("Serial # = " + repr(rvc))


