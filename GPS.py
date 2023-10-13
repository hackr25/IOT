"""
sudo nano /boot/config.txt






#############
sudo systemctl stop serial-getty@ttyS0.service

sudo systemctl enable serial-getty@ttyAMA0.service
sudo apt-get install minicom

sudo cat /dev/ttyAMA0
"""
import time
import serial
import string
import pynmea2
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
port = "/dev/ttyAMA0" # the serial port to which the pi is connected.
#create a serial object
ser = serial.Serial(port, baudrate = 9600, timeout = 0.5)
while 1:
    try:
        data = ser.readline()
# print data
    except:
        print("loading")
#wait for the serial port to churn out data
    if data[0:6] == '$GPGGA':
        
        print msg
        