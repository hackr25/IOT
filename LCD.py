"""
Steps
wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/lcd_i2c.py
sudo python lcd_i2c.py

code
"""
import smbus
import time
# Define some device parameters
I2C_ADDR = 0x27 # I2C device address

# Define some device constants
LCD_CHR = 1 # Mode - Sending data

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line


LCD_BACKLIGHT = 0x08 # On
#LCD_BACKLIGHT = 0x00 # Off
ENABLE = 0b00000100 # Enable bit
# Timing constants

E_DELAY = 0.0005
#Open I2C interface
#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1) # Rev 2 Pi uses 1
def lcd_init():
    # Initialise display
    lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    
    
    lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
def lcd_byte(bits, mode):
    # Send byte to data pins
    # bits = the data
    # mode = 1 for data
    # 0 for command
bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHT

# High bits

lcd_toggle_enable(bits_high)
# Low bits
bus.write_byte(I2C_ADDR, bits_low)

def lcd_toggle_enable(bits):
    # Toggle enable
    
    bus.write_byte(I2C_ADDR, (bits | ENABLE))
    
    
    
def lcd_string(message,line):
    # Send string to display
    message = message.ljust(LCD_WIDTH," ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        
def main():
    # Main program block
    # Initialise display
    while True:
        # Send some test
        lcd_string("RPiSpy <",LCD_LINE_1)
        lcd_string("I2C LCD <",LCD_LINE_2)
        time.sleep(3)
        # Send some more text
        lcd_string("> RPiSpy",LCD_LINE_1)
        lcd_string("> I2C LCD",LCD_LINE_2)
        time.sleep(3)
if __name__ == '__main__':
    try:
        main()
        except KeyboardInterrupt:
            pass
        finally:
        lcd_byte(0x01, LCD_CMD)