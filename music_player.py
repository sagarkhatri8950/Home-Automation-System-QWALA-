import os
 
import pygame
from mutagen.id3 import ID3

listofsongs = []
 

 
index = 0
 
def directorychooser():
    directory="/home/pi/Music/"
    os.chdir(directory)
 
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
 
             listofsongs.append(files)
             print(files)
 
 
    pygame.mixer.init(frequency=44100, size=16,channels=2, buffer=4096)#using this distorted sound fix increased sound quality.
    #pygame.mixer.init() #but using this we get distorted sound
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
 
#directorychooser()
 
def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])
    #return songname
 
 
def startsong(event):
    pygame.mixer.music.play()

 
def nextsong():
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    #updatelabel()
 
def prevsong():
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    #updatelabel()
 
 
def stopsong():
    pygame.mixer.music.stop()
    #v.set("")
    #return songname
 

listofsongs.reverse()

 



