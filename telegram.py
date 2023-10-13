"""
steps:
Step 1: Open Telegram app in your system or mobile

1.2 Start "BotFather
1.3 Open "BotFather"
1.4 Start "BotFather"
/start
1.5 Create a new Bot
1.6 Obtain access token
3.3 Install "Python Package Index"
sudo apt-get install python-pip
3.4 Install "telepot"

Step 4: Run the Python Code
4.1 Clone the git
git clone https://github.com/salmanfarisvp/TelegramBot.git
4.2 Paste your Bot Token here
bot = telepot.Bot('Bot Token')
Note: 1.6 for more details

python telegrambot.py
All set, now time to connect the Pi and LED.
Step 5: Connect LED to Pi
Step 6: Send Command

6.2 Send "on" & "off"

"""

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO
#LED
def on(pin):
    
    return
def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return
# to use Raspberry Pi board pin numbers

# set up GPIO output channel

def handle(msg):
    chat_id = msg['chat']['id']
    
    print 'Got command: %s' % command
    if command == 'on':
        
    elif command =='off':
        
bot = telepot.Bot('Bot Token')#BotToken means that you have Generated from telegram

print 'I am listening...'
while 1:
    

    