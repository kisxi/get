import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]

def volume(value):
    res = [0,0,0,0,0,0,0,0]
    v = value//(255/8)
    print(v)
    for i in range(7, -1,-1):
        if v > 0:
            res[i] = 1
            v -= 1
    return res


def adc():
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        GPIO.output(dac, dec2bin(value))
        time.sleep(0.01)
        if GPIO.input(comp) == 1:
            value -= 2**i
    return value


try:
    while True:
        value = adc()
        print(volume(value), value/255*3.3)
        GPIO.output(leds, volume(value))
finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup() 

