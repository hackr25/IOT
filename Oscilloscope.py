"""
steps:
1.sudo raspi-config
2.udo apt-get update
sudo apt-get upgrade
3.cd ~
4.sudo apt-get install build-essential python-dev python-smbus git
5.git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
6.cd Adafruit_Python_ADS1x15
sudo python setup.py install
7.cd examples
8.python simpletest.py
9.sudo apt-get install python-matplotlib
10.sudo apt-get install python-pip12
11.sudo pip install drawnow
12.sudo nano scope.py
13.import time
import matplotlib.pyplot as plt
from drawnow import *
import Adafruit_ADS1x15
14.adc = Adafruit_ADS1x15.ADS1115()
15.GAIN = 1
16.Val = [ ]
cnt = 0
17.plt.ion()
18.adc.start_adc(0, gain=GAIN)
19.plt.ylim(-5000,5000)
plt.title('Osciloscope')
plt.grid(True)
plt.ylabel('ADC outputs')
lt.plot(val, 'ro-', label='lux')
plt.legend(loc='lower right')
20.value = adc.get_last_result()
21.print('Channel 0: {0}'.format(value))
time.sleep(0.5)
val.append(int(value))
22.drawnow(makeFig)
23.cnt = cnt+1
if(cnt>50):
val.pop(0)
24.sudo python scope.py
25.Import warnings
import matplotlib.cbook
warnings.filterwarnings(“ignore”, category=matplotlib.cbook.mplDeprecation)
"""

import time
import matplotlib.pyplot as plt
#import numpy
from drawnow import *
#import Adafruit_ADS1x15 module
import Adafruit_ADS1x15
# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
val = []
cnt = 0
plt.ion()
# Start continuous ADC conversions on channel 0 using the previous gain value.
adc.start_adc(0, gain=GAIN)
print('Reading ADS1x15 channel 0')
#create the figure function
def makeFig():
    plt.ylim(-5000,5000)
    plt.title('Osciloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')
while (True):
    # Read the last ADC conversion value and print it out.
    value = adc.get_last_result()
    print('Channel 0: {0}'.format(value))
    # Sleep for half a second.
    time.sleep(0.5)
    val.append(int(value))
    drawnow(makeFig)
    plt.pause(.000001)
    cnt = cnt+1
    if(cnt>50):
        val.pop(0)
