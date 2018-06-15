from gtts import gTTS
import os

def speak(speakData,mediaName):
    #tts=gTTS(text='Sonipat Temperature is 34.0. Humidity is 28 and Pressure is 1008 Speed is 3.6 and cloud is haze',lang='en')
    tts=gTTS(text=speakData,lang='en')
    tts.save(mediaName+".mp3")
    #os.system("omxplayer "+mediaName+".mp3")
