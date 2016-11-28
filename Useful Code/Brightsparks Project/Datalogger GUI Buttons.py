from Tkinter import *
import serial, time
import datetime
import webiopi
import datetime
import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects
from webiopi.devices.serial import Serial

username = 'zaneshaq'
api_key = 'k53c99f7d1'
stream_token = 'doxcsw1igt'

py.sign_in('zaneshaq', 'k53c99f7d1')

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = Layout(
    title='Zane Imran Sun Tracker Project - Brightsparks'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Sun-Tracker')

stream = py.Stream('doxcsw1igt')
stream.open()

port = serial.Serial("/dev/ttyAMA0", baudrate=2400)

rvc = port.readline()
root = Tk()
root.title("Data Logger Control Panel")
label_1 = Label(text="Hello")
label_1.pack()
root.mainloop()

while True:
    if(rvc):
        print ("Serial # = " + repr(rvc))
        print("Uploading to Plotly")
        stream.write({'x': datetime.datetime.now(), 'y': rvc})
        time.sleep(0.1) # delay between stream posts
        
        print("Logging to File...")
        now = datetime.datetime.now()
        timenow = now.strftime("%Y-%m-%d %H:%M")
        logfile = open("templog.txt", "a")
        logfile.write(timenow)
        logfile.write(" ")
        logfile.write(rvc)
        logfile.close
        
        print("Uploading data to Webiopi")
        serial = webiopi.deviceInstance("serial")
        serial = Serial("ttyAMA0", 2400)
        if (serial.available() > 0):
            data = serial.readString()
            webiopi.sleep(1)




        
    



