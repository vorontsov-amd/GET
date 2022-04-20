import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
MaxVoltage = 3.3
MaxVoltageRC = 0.3
levels = 2**len(dac)




GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(val):
    return [int(element) for element in bin(val) [2:].zfill(8)]

def adc():
    value = 0
    for i in range(8):
        value += 2**(7-i)
        signal = decimal2binary(value)
        GPIO.output(dac, signal)
        time.sleep(0.001)
        cmpValue = GPIO.input(comp)
        if cmpValue == 0:
            value -= 2**(7-i)
        voltage = (value * MaxVoltage) / levels
    return voltage


try:
    data = []
    start = time.time()

    GPIO.output(troyka, 1)
    voltage = adc()
    print("Зарядка началась")
    while(voltage < 3.12):
        print("vol = {:.2f}".format(voltage))
        data.append(voltage)
        voltage = adc()

    GPIO.output(troyka, 0)
    print("Зарядка закончилась")
    while(voltage > 0.02 * 3.3):
        print("vol = {:.2f}".format(voltage))
        data.append(voltage)
        voltage = adc()

    finish = time.time()
    print("общее время = {:.2f}".format(finish - start))

    plt.plot(data)
    plt.show()

    data_str = [str(item) for item in data]
    with open("data.txt", "w") as out:
        out.write("\n".join(data_str))


finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()