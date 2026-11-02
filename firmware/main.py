import machine
import utime
from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd

i2c = I2C(0, scl=Pin(16), sda=Pin(18), freq=400000)

devices = i2c.scan()
if len(devices) == 0:
    print("No I2C devices found")
else:
    print("I2C devices found:", [hex(device) for device in devices])

lcd = I2cLcd(i2c, devices[0], 2, 16)
lcd.clear()

lcd.putstr("READY!!!")
wait_time = 1
lcd.clear()
lcd.putstr("Half-Life")
lcd.set_cursor(0, 1)
lcd.putstr("Week 4 and 9")
wait_time = 1
lcd.clear()
