'''I wrote this code from scratch over a long period of time as 
I learnt more about Python and Tkinter. The code is split up into seperate sections,
the first imports all the libraries required. Next it sets up plotly with the 
stream tokens and account details. I then had to start the stream and set-up the 
raspberry pi uart serial port to recieve data from the picaxe. Next I have the main 
class which contains all the functions for the data logger. First each buttons is set-up
and then I define the functions for each button. I only just learnt about how classes work 
recently so my code structure might not be the best, however I plan to continue to keep working
on the code and making it more efficient. For example being able to perform more than one function at once.
Each function first reads data from the serial port, I had to spend a lot of time getting the serial data to be split up into
individual variables however in the end it worked. The principle is the same for each function
however each does something different with the data. Lastly after creating the class and functions
I then had to make the Tkinter GUI and create the object for class main.'''
  
################## Imports Python Libraries ##################
##############################################################

from Tkinter import * # Imports Tkinter
from time import sleep # Time/Sleep
import serial, time # Serial and Time
import datetime # Current Date and Time
from webiopi.devices.serial import Serial # Webiopi Serial
import webiopi # Webiopi Library
import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis

###############################################################
##################### Sets up plotly details ##################

username                 = 'zaneshaq'
api_key                  = 'k53c99f7d1'
stream_token_temperature = 'iuqh3xt5ph'
stream_token_lightlevel    = 'vlx5vddak3'

py.sign_in('zaneshaq', 'k53c99f7d1')

# JSON code for plotly graph
trace_temperature = Scatter(
    x=[],
    y=[],
    name='Temp',
   stream=Stream(
        token=stream_token_temperature # Sets up temperature stream
    ),
    yaxis='y'
)

trace_lightlevel = Scatter(
    x=[],
    y=[],
    name='Light %',
    stream=Stream(
        token=stream_token_lightlevel # Sets up Lightlevel stream
    ),
    yaxis='y2'
)

layout = Layout(
    title='Sun Tracker - Temperature and Lightlevel Readings', #Labels graph
    yaxis=YAxis(
        title='Celcius'
    ),
    yaxis2=YAxis(
        title='Light %',
        side='right',
        overlaying="y"
    )
)

#Streams the data to plotly
data = Data([trace_temperature, trace_lightlevel])
fig = Figure(data=data, layout=layout)

print py.plot(fig, filename='Sun Tracker - Temperature and Lightlevel Readings')

stream_temperature = py.Stream(stream_token_temperature)
stream_temperature.open()

stream_lightlevel = py.Stream(stream_token_lightlevel)
stream_lightlevel.open()


####################################################
############# Sets up serial port  #################

port = serial.Serial("/dev/ttyAMA0", baudrate=2400)

########### Class Containing Functions#################

class Main: # Creates Class named Main - Contains all the functions

    def __init__(self, master):  #Always performs this function first

        self.master = master 
        self.logging = False
        self.uploading = False #Sets button toggle
        self.graphing = False 
        frame = Frame(master)
        frame.pack() # Creates Window 

############ Creates Log to File Button  ###############
        self.logFilebutton = Button(frame, text="Log To File   ", fg="blue",
            command=lambda: self.logTofile(True))
        self.logFilebutton.grid(row=0, column=0)

        self.stopLogbutton = Button(frame, text="Toggle Off",
            command=lambda: self.logTofile(False))
        self.stopLogbutton.grid(row=0, column=1)

############# Creates Log to Webiopi Button #############
        self.logWebiopibutton = Button(frame, text="Log To Webiopi", fg="red",
            command=lambda: self.logTowebiopi(True))
        self.logWebiopibutton.grid(row=1, column=0)

        self.stopWebiopibutton = Button(frame, text="Toggle Off",
            command=lambda: self.logTowebiopi(False))
        self.stopWebiopibutton.grid(row=1,column=1)

############# Creates Log to Plotly Button #############

        self.logPlotlybutton = Button(frame, text="Log To Plotly", fg="green",
            command=lambda: self.logToplotly(True))
        self.logPlotlybutton.grid(row=2, column=0)

        self.stopPlotlybutton = Button(frame, text="Toggle Off",
            command=lambda: self.logToplotly(False))
        self.stopPlotlybutton.grid(row=2,column=1)

        

################## Creates Quit Button ###################
        self.quitButton = Button(frame, text="QUIT",
            command=master.destroy)
        self.quitButton.grid(row=3, column=0, columnspan=2)


############### Log to text File Function ################
    def logTofile(self, logging=None):
        if logging is not None:
            self.logging = logging
            print "Please choose an option to log data to... "
        if self.logging:
            print "Logging to Text File"
            rvc = port.readline() #Reads data from picaxe
            if(rvc):
                port.flushInput()
                dataArray = rvc.split(",") #Splits serial data up
                light_string =dataArray[0]
                light =dataArray[1]
                volt_string =dataArray[2]
                volt =dataArray[3]
                temp_string =dataArray[4]
                temp =dataArray[5]
                print light_string, light
                print volt_string, volt
                print temp_string, temp 
                now = datetime.datetime.now() #Gets date and time
                timenow = now.strftime("%Y-%m-%d %H:%M")
                logfile = open("templog.txt", "a") #Writes data to text file
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

############## Log to Webiopi Function #################

    def logTowebiopi(self, uploading=None):
        if uploading is not None:
            self.uploading = uploading
            print "Please choose an option to log data to... "
        if self.uploading:
            port.flushInput() #Empty serial buffer
            print "Logging to Webiopi"
            serial = webiopi.deviceInstance("serial")
            serial = Serial("ttyAMA0", 2400)
            if (serial.available() > 0):  #Uploads to Webiopi
                data = serial.readString()
                webiopi.sleep(1)
            self.master.after(1, self.logTowebiopi)

############ Log to Plotly Graph Function ################

    def logToplotly(self, graphing=None):
        if graphing is not None:
            self.graphing = graphing
            print "Please choose an option to log data to... "
        if self.graphing:
            print "Logging to Plotly"
            rvc = port.readline() #Reads serial port
            if(rvc):
                port.flushInput() #Clears serial port
                dataArray = rvc.split(",") #Splits data up
                light_string =dataArray[0]
                light =dataArray[1]
                volt_string =dataArray[2]
                volt =dataArray[3]
                temp_string =dataArray[4]
                temp =dataArray[5]
                print light_string, light
                print volt_string, volt
                print temp_string, temp
                now = datetime.datetime.now()  #Streams light and temperature values
                stream_temperature.write({'x': now, 'y': temp })
                stream_lightlevel.write({'x': now, 'y': light })
            
            time.sleep(0.1) # delay between stream posts
            self.master.after(1, self.logToplotly)

stream_temperature.close() #Closes the plotly stream
stream_lightlevel.close()

############## Creates GUI Interface  ###########
root = Tk() #Main window
root.title("Data Logging GUI")
main = Main(root) #Object for Main class
root.mainloop() #Window Loop 
