
import RPi.GPIO as GPIO # RPi.GPIO can be reffered to as GPIO from now
from time import sleep

GPIO.setwarnings(False)                     #  Ignore warnings for now
GPIO.setmode(GPIO.BOARD)                    #  GPIO Numbering of Pins
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   #  Set ledPin as output

while True:
    print 'LED on'
    GPIO.output(8, GPIO.HIGH)       # LED on
    sleep(1)                 # wait 1 second
    print 'LED off'
    GPIO.output(8, GPIO.LOW)        # LED off
    sleep(1)                 # wait 1 second

