def loop():
    serial = webiopi.devicesInstance("serial")

    if (serial.available() > 0):
        data = serial.readString()
        print(" Serial = " (data))

    webiopi.sleep(1)
