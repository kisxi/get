import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]



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
        print(dec2bin(value), value/255*3.3)
        time.sleep(0.5)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()        