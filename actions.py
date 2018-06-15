import pins as Controller
import music_player as play
import face_recognition as fr
import face_ids
import switch
import alarm
import threading
import os,time
import api

def act(dataReturn,data):
    flag = 0
    if dataReturn != 'None':
        if dataReturn == 'light on' or dataReturn == '1':
            print("aa ge")
            Controller.lightOn()
            flag=1
        elif dataReturn=='light off'or dataReturn=='2':
            print("bc")
            Controller.lightOff()
            flag=1    
        elif dataReturn=='fan on'or dataReturn=='3':
            Controller.fanOn()
            flag=1
        elif dataReturn=='fan off'or dataReturn=='4':
            Controller.fanOff()
            flag=1
        elif dataReturn=='door open'or dataReturn=='5':
            fr.detect_me()
            flag=1
        elif dataReturn=='door close'or dataReturn=='6':
            Controller.doorClose()
        elif dataReturn == 'addface' or dataReturn == '13':
            listx = data.split()
            face_ids.set_id(listx[1],listx[2])
            print("trained")
        elif dataReturn == 'play music' or dataReturn == '7':
            play.directorychooser()
        elif dataReturn == 'play next music' or dataReturn == '8':
            play.nextsong()
        elif dataReturn == 'play previous music' or dataReturn == '9':
            play.prevsong()
        elif dataReturn == 'stop music' or dataReturn == '10':
            play.stopsong()
        elif dataReturn == 'weather' or dataReturn == '11':
            os.system("omxplayer weather.mp3")
        elif dataReturn == 'news' or dataReturn == '12':
            os.system("omxplayer news.mp3")
        elif dataReturn=='switch'or dataReturn=='13':
            try:
                t=threading.Thread(target=switch.start,args=(data,))
                t.start()
                flag=1
                #switch.start(data)
            except:
                print("error thread")

        elif dataReturn=='alarm'or dataReturn=='14':
            try:
                t=threading.Thread(target=main,args=(data,))
                t.start()
                flag=1
                #switch.start(data)
            except:
                print("error thread")
        if flag==1:
            os.system("omxplayer sound/ok.mp3")
    else:
        print("Unknown String")
