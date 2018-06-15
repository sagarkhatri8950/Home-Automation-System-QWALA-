import time
import os
import RPi.GPIO as GPIO
import _thread
import threading
def start(timer):
    swData=timer.split()
    if swData[2]!='cancel':
        if swData[1]=='1':
           # thread=threading.Thread(target= switch1(int(swData[2])*60))
            #thread.start()
            switch1(int(swData[2])*60)
        elif swData[1]=='2':
            switch2(int(swData[2])*60)
        elif swData[1]=='3':
            switch3(int(swData[2])*60)
    else:
        if swData[1]=='1':
           # thread=threading.Thread(target= switch1(int(swData[2])*60))
            #thread.start()
            switch1close()
        elif swData[1]=='2':
            switch2close()
        elif swData[1]=='3':
            switch3close()
            
def switch1(timer):
 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.HIGH)
    start=1
    while start<=timer:
        #print(start)
        if start==timer:
            GPIO.output(16, GPIO.LOW)
            #GPIO.cleanup()
        time.sleep(1)
        start +=1

        
def switch2(timer):

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(20, GPIO.HIGH)
    start=1
    while start<=timer:
        #print(start)
        if start==timer:
            GPIO.output(20, GPIO.LOW)
            #GPIO.cleanup()
        time.sleep(1)
        start +=1



def switch3(timer):
 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.HIGH)
    start=1
    while start<=timer:
        #print(start)
        if start==timer:
            GPIO.output(21, GPIO.LOW)
            #GPIO.cleanup()
        time.sleep(1)
        start +=1

def switch1close():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.LOW)

def switch2close():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    GPIO.output(20, GPIO.LOW)

def switch3close():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.LOW)
    
#start("switch 1 close")
