import RPi.GPIO as Io
import time

sense_pin = 11
servo1 = 13
dspl_pin = 15
Io.setmode(Io.BOARD)
Io.setwarnings(False)
Io.setup(sense_pin, Io.IN)
Io.setup(dspl_pin, Io.OUT)
Io.setup(servo1, Io.OUT)
servo1 = Io.PWM(13, 50)
last_time = time.time()
this_time = time.time()
rpm = 0.0
Io.setmode(Io.BOARD)
servo1.start(0)
duty = 0
def rpmsense(channel):
    global rpm, this_time, last_time
    this_time = time.time()
    rpm = (1.0 / (this_time - last_time)) * 60.0
    if (1.0 / (this_time - last_time)) * 60.0 >= 400.0:
        servo1.ChangeDutyCycle(12)
    print('RPM = {:7.1f}'.format(rpm))
    last_time = this_time
    return ()
Io.add_event_detect(sense_pin, Io.RISING, callback=rpmsense, bouncetime=1)
