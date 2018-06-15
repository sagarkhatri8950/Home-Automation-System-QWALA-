import tts
##import requests
##import time

##city="sonipat"
##url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=39acb6922254b1a70d54454710ac118c'
##data=requests.get(url)
##read=data.json()
##
##n=format(read['name'])
##t=format(read['main']['temp'])
##h=format(read['main']['humidity'])
##p=format(read['main']['pressure'])
##w=format(read['wind']['speed'])
##d=format(read['weather'][0]['description'])
##t=str(float(t)-273.15)
##final=n+" Temperature is "+t
##final1=" Humidity is "+h+" and Pressure is "+p
##final2=" Speed is "+w+" and cloud is "+d
final="Sonipat Temperature is 34.0 Humidity is 28 and Pressure is 1008 Speed is 3.6 and cloud is haze"

tts.speak(final)


