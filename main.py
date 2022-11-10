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
rpm = 0
Io.setmode(Io.BOARD)
servo1.start(0)
duty = 0
def rpmsense(channel):
    global rpm, this_time, last_time
    this_time = time.time()
    rpm = (1 / (this_time - last_time)) * 60
    print('RPM = {:7.1f}'.format(rpm))
    last_time = this_time
    return ()


Io.add_event_detect(sense_pin, Io.RISING, callback= rpmsense, bouncetime=1)

if rpm >= 1000:
    servo1.ChangeDutyCycle(12)
else:
    pass

try:
    for x in range(0, 10000000):
        time.sleep(0.5)
except:
    time.sleep(2)
    Io.remove_event_detect(sense_pin)
    Io.output(servo1, False)
    Io.cleanup()
    servo1.stop()
