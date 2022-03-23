import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(val):
        return [int(element) for element in bin(val) [2:].zfill(8)]

try: 
    print("Вверите период в секундах")
    T = float(input()) 

    while True:
        x = 0
        while x < 255:
            GPIO.output(dac, decimal2binary(x))
            time.sleep(T / 510)
            x += 1
        while x > 0:
            GPIO.output(dac, decimal2binary(x))
            time.sleep(T / 510)
            x -= 1

except KeyboardInterrupt:
    print("\nUser stop programm")

finally: 

    GPIO.output(dac, 0)

    GPIO.cleanup()