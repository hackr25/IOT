#wget https://raspberrytips.nl/files/tm1637.py
"""
Copy the above URL and Paste it in terminal
"""
import sys
import RPi.GPIO as GPIO
#CLK -> GPIO23 (Pin 16)
#Di0 -> GPIO24 (Pin 18)
Display = tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
Display.Clear()
while(True):
now = datetime.datetime.now()
hour = now.hour
minute = now.minute
second = now.second
currenttime = [ int(hour / 10), hour % 10, int(minute / 10), minute % 10 ]
Display.Show(currenttime)
Display.ShowDoublepoint(second % 2)
time.sleep(1)
"""
GND : 14
VCC : 4
DI0 : 18
CLK : 16
"""