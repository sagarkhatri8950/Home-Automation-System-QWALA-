import cv2
import numpy as np
import os
import time
import face_ids
def detect_me():
    #os.system("fswebcam ~/Desktop/Qwala/cap.jpg")
    cam = cv2.VideoCapture(0)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer/trainner.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    while True:
        ret, im = cam.read()
        #im = cv2.imread('cap.jpg')
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            #cv2.imshow('im', im)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])            
            if(conf<50):
                usr = face_ids.get_id()
                for i in usr.keys():
                    if(Id==i):
                        print(usr[i])
                        #return Id
                    else:
                        print("unknown")
