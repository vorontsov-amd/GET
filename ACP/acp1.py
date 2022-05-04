import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

levels = 2**len(dac)
maxVoltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(val):
    return [int(element) for element in bin(val) [2:].zfill(8)]

def adc():

    for value in range(256):
        signal = decimal2binary(value)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        cmpValue = GPIO.input(comp)
        if cmpValue == 0:
            voltage = value / levels * maxVoltage
            return voltage


try:
    while True:
        voltage = adc()
        print("Expected ADC: ", "{:.3f}".format(voltage), "V")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()