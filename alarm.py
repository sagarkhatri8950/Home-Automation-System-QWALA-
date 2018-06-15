import time
import os
import pygame


class Alarm():
    def __init__(self, hours, minutes,music_time):
        super(Alarm, self).__init__()
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.music_time=int(music_time)
        self.fadeout=2000

    def run(self):

            while True:
                now = time.localtime()
                if (now.tm_hour == self.hours and now.tm_min == self.minutes):       
                    pygame.mixer.init()
                    sound = pygame.mixer.Sound("alarm.wav")
                    sound.play()
                    time.sleep(self.music_time-(int(self.fadeout/1000)))
                    sound.fadeout(self.fadeout)
                    time.sleep(1)


def main(alarm):
    alarmData=alarm.split()
    if alarmData[2]!='cancel':
   # alarm = Alarm(alarm_HH, alarm_MM,60) 60= time for the sec the alarm will raise
        #alarm = Alarm('16','54',6)
        alarm = Alarm(alarmData[1],alarmData[2],6)
        alarm.run()



if __name__ == "__main__":
 main("alarm 9 44")
