import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT, initial=0)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(0)

try:
    while True:
        print("Duty cycle: ")
        Duty_cucle = float(input())
        p.start(Duty_cucle)
        print(str(3.3 * Duty_cucle / 100) + "V")

finally: 
    GPIO.cleanup()

