from machine import Pin 
from time import sleep

button1 = Pin(22,Pin.IN, Pin.PULL_UP)
button2 = Pin(23,Pin.IN, Pin.PULL_UP)
led = Pin(2,Pin.OUT)

while True:
    #button1_value = not button2.value() and not button1.value()
    #print(button1_value)
    #Xor
    led.value( not button2.value() != not button1.value())
    sleep(0.5)