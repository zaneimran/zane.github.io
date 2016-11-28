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

index = 0

port = serial.Serial("/dev/ttyAMA0", baudrate=2400)

def logTofile():
    print("Logging to File...")
    rvc = port.readline()
    if(rvc):
        print ("Serial # = " + repr(rvc))
        now = datetime.datetime.now()
        timenow = now.strftime("%Y-%m-%d %H:%M")
        logfile = open("templog.txt", "a")
        logfile.write(timenow)
        logfile.write(" ")
        logfile.write(rvc)
        logfile.close

def uploadTowebiopi():
    print("Uploading data to Webiopi")
    serial = webiopi.deviceInstance("serial")
    serial = Serial("ttyAMA0", 2400)
    if (serial.available() > 0):
        data = serial.readString()
        webiopi.sleep(1)
    
def uploadToplotly():
    print("Uploading")
    rvc = port.readline()
    if(rvc):
        print ("Serial # = " + repr(rvc))
        stream.write({'x': datetime.datetime.now(), 'y': rvc})
        time.sleep(0.1) # delay between stream posts
        
    

        
root = Tk()
root.minsize(700, 400)
root.maxsize(700, 400)
root.title("Data Logger Control Panel")

logButton = Button(text="Log to File", command=logTofile)
webiopiButton = Button(text="Upload to Webiopi", command=uploadTowebiopi)
plotlyButton = Button(text="Upload to Plotly", command=uploadToplotly)

logButton.pack()
webiopiButton.pack()
plotlyButton.pack()

root.mainloop()

