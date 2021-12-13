# Name   : Christian Meier
# Klasse : ETS 2021
# Datum  : 16.11.2021

from bmp180 import BMP180                                           # Bibliothek Sensor (BMP180) Temperatur,Luftdruck
from machine import Pin                                             # Bibliothek Pin (Ein/Ausgang)                                             
from machine import I2C                                             # Bibliothek Busssystem
import time                                                         # Bibliothek Zeiten

bus = I2C(scl = Pin(22), sda = Pin(21), freq = 100000)              # Bussystem Parameter eingestellt

bmp180 = BMP180(bus)                                                # Busssystem mit Sensor verbunden
bmp180.oversample_sett = 2
bmp180.baseline = 101325
Temperatur = int(bmp180.temperature)                                # Wert der Temperatur in Ganzenwerte ausgegeben
Luftdruck  = int(bmp180.pressure / 100)                             # Wert des Luftdruck in Ganzenwerte ausgegeben
errechneteHoehe = int(bmp180.altitude)                              # Wert der Höhe über Null in Ganzen Werten

while True:                                                         # Wiederholende Schleife
    print(Temperatur, "\u00b0C")                                    # Wert Temperatur ausgegeben, Unicode für ° 
    print(Luftdruck, "hPa")                                         # Wert Luftdruck ausgegeben
    print(errechneteHoehe, "Meter ueber dem Wasser")                # Wert Höhe ausgegeben
    print("\n")                                                     # Leerzeichen ausgeben 
    time.sleep(10)                                                  # Wartezeit von 10 Sekunden
