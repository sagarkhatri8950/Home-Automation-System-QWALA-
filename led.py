import RPi.GPIO as GPIO
import time
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

def on():
    setup()
    #while True :
    GPIO.output(18, GPIO.HIGH)
       
def off():
    setup()
    GPIO.output(18, GPIO.LOW)
    GPIO.cleanup()
