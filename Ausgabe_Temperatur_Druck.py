# Name   : Christian Meier
# Klasse : ETS 2021
# Datum  : 16.11.2021

from bmp180 import BMP180
from machine import Pin
from machine import I2C
import time 

bus = I2C(scl = Pin(22), sda = Pin(21), freq = 100000)

bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

Temperatur = int(bmp180.temperature) 
Luftdruck  = int(bmp180.pressure / 100) 
errechneteHoehe = int(bmp180.altitude) 

while True:
    print(Temperatur, "\u00b0C")
    print(Luftdruck, "hPa")
    print(errechneteHoehe, "Meter ueber dem Wasser")
    print("\n")
    time.sleep(10)
