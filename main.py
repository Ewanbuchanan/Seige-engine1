import RPi.GPIO as Io
import time

sense_pin = 11
servo_pin = 13
dspl_pin = 15
servo1 = Io.PWM(13, 50)
Io.setmode(Io.BOARD)
Io.setup(sense_pin, Io.IN)
Io.setup(servo_pin, Io.OUT)
Io.setup(dspl_pin, Io.OUT)
last_time = time.time()
this_time = time.time()
rpm = 0

servo1.start(0)
duty = 0


def rpmsense(channel):
    global rpm, this_time, last_time
    this_time = time.time()
    rpm = (1 / (this_time - last_time)) * 60
    print('RPM = {:7.1f}'.format(rpm))
    last_time = this_time
    return ()


Io.add_event_detect(sense_pin, Io.RISING, callback=rpmsense, bouncetime=1)

if rpm >= 1000:
    servo1.ChangeDutyCycle(12)
else:
    pass

try:
    for x in range(0, 100000):
        time.sleep(0.5)
except:
    Io.remove_event_detect(sense_pin)
    Io.output(servo1, False)
    Io.cleanup()
    servo1.stop()
