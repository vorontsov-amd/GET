import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

def decimal2binary(val):
        return [int(element) for element in bin(val) [2:].zfill(8)]

try: 
    while True:
        print("print number 0 to 255")
        value = input()
        if value == 'q' :
            break 
        try:
            if float(value) % 1 != 0:
                print("not int")
                continue
            elif int(value) > 255:
                print(" more 255 ")
                continue
            elif int(value) < 0:
                print(" less 0 ")
                continue
            value = int(value)

            GPIO.output(dac, decimal2binary(value))
            print("Expected CAP: ", "{:.3f}".format(3.3 * value / 255), "V") 
        except ValueError:
            print("Not a num")

finally: 

    GPIO.output(dac, 0)

    GPIO.cleanup()