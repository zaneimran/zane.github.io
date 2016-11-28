import plotly.plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure, Data, Stream, YAxis # plotly graph objects
import time # timer functions
import serial
import datetime

username = 'zaneshaq'
api_key = 'k53c99f7d1'
stream_token_lightlevel = 'doxcsw1igt'
stream_token_voltage = 'vlx5vddak3'
stream_token_temperature = 'iuqh3xt5ph'

py.sign_in('zaneshaq', 'k53c99f7d1')

trace_lightlevel = Scatter(
    x=[],
    y=[],
    stream=Stream(
        token=stream_token_lightlevel,
        maxpoints=200
    ),
    yaxis='y'
)

trace_voltage = Scatter(
    x=[],
    y=[],
    stream=Stream(
        token=stream_token_voltage,
        maxpoints=200
    ),
    yaxis='y2'
)

trace_temperature = Scatter(
    x=[],
    y=[],
    stream=Stream(
        token=stream_token_temperature,
        maxpoints=200
    ),
    yaxis='y3'
)

layout = Layout(
    title='Zane Imran Sun Tracker Project - Brightsparks',
    yaxis=YAxis(
        title='Light'
        ),
    yaxis2=YAxis(
        title='Volt',
        ),
    yaxis3=YAxis(
        title='Temp',
        )
)

data = Data([trace_lightlevel, trace_voltage, trace_temperature])
fig = Figure(data=data, layout=layout)
print py.plot(fig, filename='Raspberry Pi Streaming Sun-Tracker')

#fig = Figure(data=[trace_lightlevel, trace_voltage, trace_temperature], layout=layout)

#print py.plot(fig, filename='Raspberry Pi Streaming Sun-Tracker')

stream_lightlevel = py.Stream(stream_token_lightlevel)
stream_lightlevel.open()

stream_voltage = py.Stream(stream_token_voltage)
stream_voltage.open()

stream_temperature = py.Stream(stream_token_temperature)
stream_temperature.open()

port = serial.Serial("/dev/ttyAMA0", baudrate=2400)

while True:
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
    
    stream_lightlevel.write({'x': datetime.datetime.now(), 'y': light})
    stream_voltage.write({'x': datetime.datetime.now(), 'y': volt})
    stream_temperature.write({'x': datetime.datetime.now(), 'y': temp})
    time.sleep(0.1) # delay between stream posts
