from machine import Pin
from time import sleep
ledVerde = Pin(23,Pin.OUT) 
ledAmarelo = Pin(22,Pin.OUT)
ledVermelho = Pin(4,Pin.OUT)
ledPedestreVerde = Pin(18,Pin.OUT)
ledPedestreVermelho = Pin(19,Pin.OUT)
button = Pin(5,Pin.IN,Pin.PULL_UP)

while True:
    ledAmarelo.off()
    ledVermelho.off()
    ledPedestreVerde.off()
    ledPedestreVermelho.on()
    ledVerde.on()
    if not button.value():
        ledVerde.off()
        ledAmarelo.on()
        sleep(2)
        ledPedestreVermelho.off()
        ledAmarelo.off()
        ledVermelho.on()
        ledPedestreVerde.on()
        sleep(2)


#    ledPedestreVerde.off()
#    ledPedestreVermelho.on()
#    sleep(2)
#    ledVerde.off()
#    ledAmarelo.on()
#    sleep(1)
#    ledPedestreVerde.on()
#    ledPedestreVermelho.off()
#    ledAmarelo.off()
#    ledVermelho.on()
#    sleep(2)