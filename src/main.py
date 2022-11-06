from time import sleep
from machine import Pin

led = Pin(0, Pin.OUT)

while True:
    led.value(not led.value())
    sleep(2)