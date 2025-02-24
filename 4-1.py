import RPi.GPIO as GPIO


def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    try:
        while True:
            value = input()
            if value == 'q':
                break
            elif int(value) < 0 or int(value) > 255:
                print('Введено число, выходящее за границы допустимых значений')
            else:
                GPIO.output(dac, decimal2binary(int(value)))
                voltage = (int(value)/255)*3.3
                print('Напряжение:', voltage, 'B')
    except ValueError:
        print('Введено не число/нецелое число')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

