import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 16
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(val):
    return [int(bit) for bit in bin(val)[2:].zfill(8)]

def adc():
    for i in range(256):
        sig = dec2bin(i)
        GPIO.output(dac, sig)
        time.sleep(0.1)
        if GPIO.input(comp) == 1:
            return i
    return 255


try:
    while True:
        value = adc()
        print(dec2bin(value), value/255*3.3)
        time.sleep(0.05)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()        