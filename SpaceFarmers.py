from sense_hat import SenseHat
import sys
from time import sleep

import logging
import logging.config

#from picamera import PiCamera
#from PIL import Image

import socket
import fcntl
import struct

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
    

host_name = socket.gethostname()
host_ip = get_ip_address()
hostName = host_name  + ' ' + host_ip

# Logging configuration under ./myconf.conf
logging.config.fileConfig('myconf.conf')
logger = logging.getLogger('SpaceFarmersLogger')

sense = SenseHat()
sense.clear()

r = 0
g = 128
b = 0
y = 0

green = (r,g,b)
black = (r,b,y)

#camera = PiCamera()
#camera.resolution = (1024, 768)

r = (255,0,0)
b = (0,0,255)
bl = (0,0,0)

morning1 = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r
    ]
morning2 = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    b,b,b,b,b,b,b,b
    ]
morning3 = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
    ]
night = [
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl
    ]
morning4 = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
    ]
morning5 = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
    ]
noon1 = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
    ]
noon2 = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
    ]
noon3 = [
    r,r,r,r,r,r,r,r,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
    ]
noon4 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b
    ]
noon5 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    bl,bl,bl,bl,bl,bl,bl,bl
    ]
noon6 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl
    ]
noon7 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl
    ]
night1 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl
    ]
night2 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl
    ]
night3 = [
    b,b,b,b,b,b,b,b,
    b,b,b,b,b,b,b,b,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl
    ]
night4 = [
    b,b,b,b,b,b,b,b,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl
    ]
night5 = [
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl
    ]
night6 = [
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    r,r,r,r,r,r,r,r
    ]
night7 = [
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r
    ]
night8 = [
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r
    ]
night9 = [
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r
    ]
night10 = [
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r
    ]
night11 = [
    bl,bl,bl,bl,bl,bl,bl,bl,
    bl,bl,bl,bl,bl,bl,bl,bl,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r
    ]
night11 = [
    bl,bl,bl,bl,bl,bl,bl,bl,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r
    ]

def temperature_reading():
    celcius = int(round(sense.get_temperature(), 2))
    fahrenheit = int(round(1.8 * celcius + 32, 2))
    return fahrenheit

def temperature_reading_from_pressure():
    celcius = int(round(sense.get_temperature_from_pressure(), 2))
    fahrenheit = int(round(1.8 * celcius + 32, 2))
    return fahrenheit

def humidity_reading():
    humidity = int(round(sense.get_humidity(), 2))
    return humidity

def entire(time):
    temp = temperature_reading()
    temp_pressure = temperature_reading_from_pressure()
    humi = humidity_reading()
    sense.set_pixels(time)
#    camera.capture("plant_image.jpg")
    logger.info(hostName, extra={'Temperature F':temp, 'Temperature from Pressure sensor F':temp_pressure, 'Humidity %':humi, 'Host':host_name, 'IP':host_ip})
    print(hostName + ' Temp: ', temp, ' Temp Pressure: ', temp_pressure, ' Humi: ', humi)
    sleep(1)
    
while True:
    sense.show_message("Space Farmers!", text_colour=green, back_colour=black)
    sense.set_pixel(3, 0, (255, 255, 255))
    sense.set_pixel(2, 1, (255, 255, 255))
    sense.set_pixel(3, 1, (255, 255, 255))
    sense.set_pixel(4, 1, (255, 255, 255))
    sense.set_pixel(2, 2, (255, 255, 255))
    sense.set_pixel(3, 2, (0, 0, 255))
    sense.set_pixel(4, 2, (255, 255, 255))
    sense.set_pixel(2, 3, (255, 255, 255))
    sense.set_pixel(3, 3, (255, 255, 255))
    sense.set_pixel(4, 3, (255, 255, 255))
    sense.set_pixel(2, 4, (255, 255, 255))
    sense.set_pixel(3, 4, (255, 255, 255))
    sense.set_pixel(4, 4, (255, 255, 255))
    sense.set_pixel(2, 5, (255, 0, 0))
    sense.set_pixel(3, 5, (255, 0, 0))
    sense.set_pixel(4, 5, (255, 0, 0))
    sense.set_pixel(2, 6, (255, 0, 0))
    sense.set_pixel(3, 6, (255, 0, 0))
    sense.set_pixel(4, 6, (255, 0, 0))
    sense.set_pixel(1, 6, (255, 0, 0))
    sense.set_pixel(5, 6, (255, 0, 0))

    sense.set_pixel(1, 7, (255, 0, 0))
    sense.set_pixel(2, 7, (255, 0, 0))
    sense.set_pixel(4, 7, (255, 0, 0))
    sense.set_pixel(5, 7, (255, 0, 0))
    sleep(0.1)

    sense.set_pixel(2, 0, (255, 255, 255))
    sense.set_pixel(3, 0, (255, 255, 255))
    sense.set_pixel(4, 0, (255, 255, 255))
    sense.set_pixel(2, 1, (255, 255, 255))
    sense.set_pixel(3, 1, (0, 0, 255))
    sense.set_pixel(4, 1, (255, 255, 255))
    sense.set_pixel(2, 2, (255, 255, 255))
    sense.set_pixel(3, 2, (255, 255, 255))
    sense.set_pixel(4, 2, (255, 255, 255))
    sense.set_pixel(2, 3, (255, 255, 255))
    sense.set_pixel(3, 3, (255, 255, 255))
    sense.set_pixel(4, 3, (255, 255, 255))
    sense.set_pixel(2, 4, (255, 0, 0))
    sense.set_pixel(3, 4, (255, 0, 0))
    sense.set_pixel(4, 4, (255, 0, 0))
    sense.set_pixel(2, 5, (255, 0, 0))
    sense.set_pixel(3, 5, (255, 0, 0))
    sense.set_pixel(4, 5, (255, 0, 0))
    sense.set_pixel(1, 5, (255, 0, 0))
    sense.set_pixel(5, 5, (255, 0, 0))
    sense.set_pixel(1, 6, (255, 0, 0))
    sense.set_pixel(2, 6, (255, 0, 0))
    sense.set_pixel(4, 6, (255, 0, 0))
    sense.set_pixel(5, 6, (255, 0, 0))
    sleep(0.1)

    sense.set_pixel(2, 0, (255, 255, 255))
    sense.set_pixel(3, 0, (0, 0, 255))
    sense.set_pixel(4, 0, (255, 255, 255))
    sense.set_pixel(2, 1, (255, 255, 255))
    sense.set_pixel(3, 1, (255, 255, 255))
    sense.set_pixel(4, 1, (255, 255, 255))
    sense.set_pixel(2, 2, (255, 255, 255))
    sense.set_pixel(3, 2, (255, 255, 255))
    sense.set_pixel(4, 2, (255, 255, 255))
    sense.set_pixel(2, 3, (255, 0, 0))
    sense.set_pixel(3, 3, (255, 0, 0))
    sense.set_pixel(4, 3, (255, 0, 0))
    sense.set_pixel(2, 4, (255, 0, 0))
    sense.set_pixel(3, 4, (255, 0, 0))
    sense.set_pixel(4, 4, (255, 0, 0))
    sense.set_pixel(1, 4, (255, 0, 0))
    sense.set_pixel(5, 4, (255, 0, 0))
    sense.set_pixel(1, 5, (255, 0, 0))
    sense.set_pixel(2, 5, (255, 0, 0))
    sense.set_pixel(4, 5, (255, 0, 0))
    sense.set_pixel(5, 5, (255, 0, 0))
    sleep(0.1)

    sense.set_pixel(2, 0, (255, 255, 255))
    sense.set_pixel(3, 0, (255, 255, 255))
    sense.set_pixel(4, 0, (255, 255, 255))
    sense.set_pixel(2, 1, (255, 255, 255))
    sense.set_pixel(3, 1, (255, 255, 255))
    sense.set_pixel(4, 1, (255, 255, 255))
    sense.set_pixel(2, 2, (255, 0, 0))
    sense.set_pixel(3, 2, (255, 0, 0))
    sense.set_pixel(4, 2, (255, 0, 0))
    sense.set_pixel(2, 3, (255, 0, 0))
    sense.set_pixel(3, 3, (255, 0, 0))
    sense.set_pixel(4, 3, (255, 0, 0))
    sense.set_pixel(1, 3, (255, 0, 0))
    sense.set_pixel(5, 3, (255, 0, 0))
    sense.set_pixel(1, 4, (255, 0, 0))
    sense.set_pixel(2, 4, (255, 0, 0))
    sense.set_pixel(4, 4, (255, 0, 0))
    sense.set_pixel(5, 4, (255, 0, 0))
    sense.set_pixel(1, 7, (0, 0, 0))
    sense.set_pixel(2, 7, (0, 0, 0))
    sense.set_pixel(4, 7, (0, 0, 0))
    sense.set_pixel(5, 7, (0, 0, 0))
    sense.set_pixel(3, 6, (0, 0, 0))
    sleep(0.1)

    sense.set_pixel(2, 0, (255, 255, 255))
    sense.set_pixel(3, 0, (255, 255, 255))
    sense.set_pixel(4, 0, (255, 255, 255))
    sense.set_pixel(2, 1, (255, 0, 0))
    sense.set_pixel(3, 1, (255, 0, 0))
    sense.set_pixel(4, 1, (255, 0, 0))
    sense.set_pixel(2, 2, (255, 0, 0))
    sense.set_pixel(3, 2, (255, 0, 0))
    sense.set_pixel(4, 2, (255, 0, 0))
    sense.set_pixel(1, 2, (255, 0, 0))
    sense.set_pixel(5, 2, (255, 0, 0))
    sense.set_pixel(1, 3, (255, 0, 0))
    sense.set_pixel(2, 3, (255, 0, 0))
    sense.set_pixel(4, 3, (255, 0, 0))
    sense.set_pixel(5, 3, (255, 0, 0))
    sense.set_pixel(1, 6, (0, 0, 0))
    sense.set_pixel(2, 6, (0, 0, 0))
    sense.set_pixel(4, 6, (0, 0, 0))
    sense.set_pixel(5, 6, (0, 0, 0))
    sense.set_pixel(3, 5, (0, 0, 0))
    sleep(0.1)

    sense.set_pixel(2, 0, (255, 0, 0))
    sense.set_pixel(3, 0, (255, 0, 0))
    sense.set_pixel(4, 0, (255, 0, 0))
    sense.set_pixel(2, 1, (255, 0, 0))
    sense.set_pixel(3, 1, (255, 0, 0))
    sense.set_pixel(4, 1, (255, 0, 0))
    sense.set_pixel(1, 1, (255, 0, 0))
    sense.set_pixel(5, 1, (255, 0, 0))
    sense.set_pixel(1, 2, (255, 0, 0))
    sense.set_pixel(2, 2, (255, 0, 0))
    sense.set_pixel(4, 2, (255, 0, 0))
    sense.set_pixel(5, 2, (255, 0, 0))
    sense.set_pixel(1, 5, (0, 0, 0))
    sense.set_pixel(2, 5, (0, 0, 0))
    sense.set_pixel(4, 5, (0, 0, 0))
    sense.set_pixel(5, 5, (0, 0, 0))
    sense.set_pixel(3, 4, (0, 0, 0))
    sleep(0.1)

    sense.set_pixel(2, 0, (255, 0, 0))
    sense.set_pixel(3, 0, (255, 0, 0))
    sense.set_pixel(4, 0, (255, 0, 0))
    sense.set_pixel(1, 0, (255, 0, 0))
    sense.set_pixel(5, 0, (255, 0, 0))
    sense.set_pixel(1, 1, (255, 0, 0))
    sense.set_pixel(2, 1, (255, 0, 0))
    sense.set_pixel(4, 1, (255, 0, 0))
    sense.set_pixel(5, 1, (255, 0, 0))
    sense.set_pixel(1, 4, (0, 0, 0))
    sense.set_pixel(2, 4, (0, 0, 0))
    sense.set_pixel(4, 4, (0, 0, 0))
    sense.set_pixel(5, 4, (0, 0, 0))
    sense.set_pixel(3, 3, (0, 0, 0))
    sleep(0.1)

    sense.set_pixel(1, 0, (255, 0, 0))
    sense.set_pixel(2, 0, (255, 0, 0))
    sense.set_pixel(4, 0, (255, 0, 0))
    sense.set_pixel(5, 0, (255, 0, 0))
    sense.set_pixel(1, 3, (0, 0, 0))
    sense.set_pixel(2, 3, (0, 0, 0))
    sense.set_pixel(4, 3, (0, 0, 0))
    sense.set_pixel(5, 3, (0, 0, 0))
    sense.set_pixel(3, 2, (0, 0, 0))
    sleep(0.1)

    sense.set_pixel(1, 2, (0, 0, 0))
    sense.set_pixel(2, 2, (0, 0, 0))
    sense.set_pixel(4, 2, (0, 0, 0))
    sense.set_pixel(5, 2, (0, 0, 0))
    sense.set_pixel(3, 1, (0, 0, 0))
    sleep(0.1)

    sense.set_pixel(1, 1, (0, 0, 0))
    sense.set_pixel(2, 1, (0, 0, 0))
    sense.set_pixel(4, 1, (0, 0, 0))
    sense.set_pixel(5, 1, (0, 0, 0))
    sense.set_pixel(3, 0, (0, 0, 0))
    sleep(0.1)

    sense.set_pixel(1, 0, (0, 0, 0))
    sense.set_pixel(2, 0, (0, 0, 0))
    sense.set_pixel(4, 0, (0, 0, 0))
    sense.set_pixel(5, 0, (0, 0, 0))
        
    sleep(2)
    entire(morning1)
    entire(morning2)
    entire(morning3)
    entire(morning4)
    entire(morning5)
    entire(noon1)
    entire(noon2)
    entire(noon3)
    entire(noon4)
    entire(noon5)
    entire(noon6)
    entire(noon7)
    entire(night1)
    entire(night2)
    entire(night3)
    entire(night4)
    entire(night5)
    entire(night6)
    entire(night7)
    entire(night8)
    entire(night9)
    entire(night10)
    entire(night11)

