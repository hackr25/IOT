"""
steps:
Step 1: Open Telegram app in your system or mobile
Open Telegram app in your system or mobile\
1.2 Start "BotFather
1.3 Open "BotFather"
1.4 Start "BotFather"
/start
1.5 Create a new Bot
1.6 Obtain access token
3.3 Install "Python Package Index"
sudo apt-get install python-pip
3.4 Install "telepot"
sudo pip install telepot
Step 4: Run the Python Code
4.1 Clone the git
git clone https://github.com/salmanfarisvp/TelegramBot.git
4.2 Paste your Bot Token here
bot = telepot.Bot('Bot Token')
Note: 1.6 for more details
4.3 Run the Code
python telegrambot.py
All set, now time to connect the Pi and LED.
Step 5: Connect LED to Pi
Step 6: Send Command
6.1 Start our Bot
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
    GPIO.output(pin,GPIO.HIGH)
    return
def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command
    if command == 'on':
        bot.sendMessage(chat_id, on(11))
    elif command =='off':
        bot.sendMessage(chat_id, off(11))
bot = telepot.Bot('Bot Token')#BotToken means that you have Generated from telegram
bot.message_loop(handle)
print 'I am listening...'
while 1:
    time.sleep(10)

    
