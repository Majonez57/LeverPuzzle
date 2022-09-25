import RPi.GPIO as GPIO
from time import sleep as zzz

LED_PINS = [21, 20, 16, 12, 1]
LEV_PINS = [14,15,18,23,24,25]

DEFAULT = 21
LEV_VALS = [21,5,20,12,29,22]

def puzzle():
    out = DEFAULT
    for i in LEV_PINS:
        if GPIO.input(i):
            out == out ^ out
    return out
    

def outToLights(out):
    temp_out = out
    for i in LED_PINS:
        GPIO.output(i, GPIO.HIGH if temp_out & 1 else GPIO.LOW)
        temp_out = temp_out >> 1

while True:
    zzz(0.5)
    outToLights(puzzle())
    