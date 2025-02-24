import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
p = GPIO.PWM(21, 1000)
p.start(0)
try:
    while True:
        duty_cycle = input()
        p.ChangeDutyCycle(int(duty_cycle))
        GPIO.output(22, GPIO.input(24))

finally:
    GPIO.output(22, 0)
    p.stop()
    GPIO.cleanup()