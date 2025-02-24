import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

t = 10 #период функции

try:
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(t/512)
    for i in range(255, -1, -1):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(t/512)


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

