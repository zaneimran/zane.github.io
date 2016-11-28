import serial, time
import datetime
port = serial.Serial("/dev/ttyAMA0", baudrate=2400)

def filewrite(rvc, timenow):
    logfile = open("templog.txt", "a")
    logfile.write(timenow)
    logfile.write(" ")
    logfile.write(rvc)
    logfile.close

while True:
    rvc = port.readline()
    if(rvc):
        port.flushInput()
        print ("Serial # = " + repr(rvc))
        now = datetime.datetime.now()
        timenow = now.strftime("%Y-%m-%d %H:%M")
        filewrite(rvc, timenow)
