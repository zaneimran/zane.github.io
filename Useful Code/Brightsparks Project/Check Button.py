from Tkinter import * # Imports Tkinter
from time import sleep # Time/Sleep
import serial, time # Serial and Time
import datetime # Current Date and Time
from webiopi.devices.serial import Serial # Webiopi Serial
import webiopi # Webiopi Library
import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects

port = serial.Serial("/dev/ttyAMA0", baudrate=2400) # Sets up serial port

#Sets Up Plotly
username = 'zaneshaq'
api_key = 'k53c99f7d1'   #Plotly Account Details
stream_token = 'doxcsw1igt'

py.sign_in('zaneshaq', 'k53c99f7d1')

trace1 = Scatter(   #Settings for graph layout
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = Layout(
    title='Zane Imran Sun Tracker Project - Brightsparks' #Graph Title
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Sun-Tracker') #Graph File Name

stream = py.Stream('doxcsw1igt')
stream.open() # Starts Graph Stream

class Main: # Creates Class named Main

    def __init__(self, master):  #Always performs this function 

        self.master = master 
        self.logging = False
        self.uploading = False #Sets button toggle
        self.graphing = False 
        frame = Frame(master)
        frame.pack() # Creates Window 

#Creates Log to File Button 
        self.logFilebutton = Button(frame, text="Log To File", fg="blue",
            command=lambda: self.logTofile(True))
        self.logFilebutton.grid(row=0, column=0)

        self.stopLogbutton = Button(frame, text="Toggle Off",
            command=lambda: self.logTofile(False))
        self.stopLogbutton.grid(row=0, column=1)

#Creates Log to Webiopi Button
        self.logWebiopibutton = Button(frame, text="Log To Webiopi", fg="red",
            command=lambda: self.logTowebiopi(True))
        self.logWebiopibutton.grid(row=1, column=0)

        self.stopWebiopibutton = Button(frame, text="Toggle Off",
            command=lambda: self.logTowebiopi(False))
        self.stopWebiopibutton.grid(row=1,column=1)

#Creates Log to Plotly Button
        self.logPlotlybutton = Button(frame, text="Log To Graph", fg="Green",
            command=lambda: self.logToplotly(True))
        self.logPlotlybutton.grid(row=2,column=0)

        self.stopPlotlybutton = Button(frame, text="Toggle Off",
            command=lambda: self.logToplotly(False))
        self.stopPlotlybutton.grid(row=2,column=1)



# Log to text File Function
    def logTofile(self, logging=None):
        if logging is not None:
            self.logging = logging
        if self.logging:
            print "Logging to Text File"
            rvc = port.readline()
            if(rvc):
                port.flushInput()
                dataArray = rvc.split(",")
                light_string =dataArray[0]
                light =dataArray[1]
                volt_string =dataArray[2]
                volt =dataArray[3]
                temp_string =dataArray[4]
                temp =dataArray[5]
                print light_string, light
                print volt_string, volt
                print temp_string, temp 
                now = datetime.datetime.now()
                timenow = now.strftime("%Y-%m-%d %H:%M")
                logfile = open("templog.txt", "a")
                logfile.write(timenow)
                logfile.write("   ")
                logfile.write("Light Level = ")
                logfile.write(light)
                logfile.write("   ")
                logfile.write("Voltage = ")
                logfile.write(volt)
                logfile.write("   ")
                logfile.write("Temperature = ")
                logfile.write(temp)
                logfile.write("\n")
                logfile.close
            self.master.after(1, self.logTofile)

# Log to Webiopi Function

    def logTowebiopi(self, uploading=None):
        if uploading is not None:
            self.uploading = uploading
        if self.uploading:
            port.flushInput()
            print "Logging to Webiopi"
            serial = webiopi.deviceInstance("serial")
            serial = Serial("ttyAMA0", 2400)
            if (serial.available() > 0):
                data = serial.readString()
                webiopi.sleep(1)
            self.master.after(1, self.logTowebiopi)

# Log to Plotly Graph Function

    def logToplotly(self, graphing=None):
        if graphing is not None:
            self.graphing = graphing
        if self.graphing:
            print "Logging to Webiopi"
            rvc = port.readline()
            if(rvc):
                port.flushInput()
                dataArray = rvc.split(",")
                light_string =dataArray[0]
                light =dataArray[1]
                volt_string =dataArray[2]
                volt =dataArray[3]
                temp_string =dataArray[4]
                temp =dataArray[5]
                print light_string, light
                print volt_string, volt
                print temp_string, temp
                stream.write({'x': datetime.datetime.now(), 'y': light})
                time.sleep(0.1) # delay between stream posts
            self.master.after(1, self.logToplotly)


root = Tk() #Main window
root.title("Data Logging GUI")
main = Main(root) #Object for Main class
root.mainloop() #Window Loop 
