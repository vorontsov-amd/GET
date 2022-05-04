import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [24, 25, 8, 7, 12, 16, 20, 21 ]
comp = 4
troyka = 17

levels = 2**len(dac)
maxVoltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(val):
    return [int(element) for element in bin(val) [2:].zfill(8)]

def adc():
    value = 0
    for i in range(8):
        value += 2**(7-i)
        signal = decimal2binary(value)
        GPIO.output(dac, signal)
        time.sleep(0.0001)
        cmpValue = GPIO.input(comp)
        if cmpValue == 0:
            value -= 2**(7-i)
            signal = decimal2binary(value)
        voltage = value / levels * maxVoltage
        #print(signal)
    print(value, signal, "Expected ADC: ", "{:.3f}".format(voltage), "V")
    return voltage


def LegsFunc():
    voltage = adc()
    for i in range(8):
        if (voltage > maxVoltage * i / 8):
            GPIO.output(leds[i], 1)
        else:
            GPIO.output(leds[i], 0)


try:
    while True:
        LegsFunc()

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()