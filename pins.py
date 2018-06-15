import RPi.GPIO as GPIO
import time
def lightSetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

def fanSetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)

def doorSetup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)

    

def lightOn():
    lightSetup()
    GPIO.output(18, GPIO.HIGH)
       
                   
def lightOff():
    lightSetup()
    GPIO.output(18, GPIO.LOW)
    #GPIO.cleanup() It will set all pins off so use it only when you wnat to turn off every thing.
        


def fanOn():
    fanSetup()
    GPIO.output(23, GPIO.HIGH)
    

def fanOff():
    fanSetup()
    GPIO.output(23, GPIO.LOW)
    


def doorOpen():
    doorSetup()
    GPIO.output(24, GPIO.HIGH)
    

def doorClose():
    doorSetup()
    GPIO.output(24, GPIO.LOW)
    

