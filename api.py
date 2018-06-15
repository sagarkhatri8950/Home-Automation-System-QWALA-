import requests
import gspeak
import wikipedia
import time
import gspeak
from apis import *

def news():
    url='https://newsapi.org/v2/top-headlines?country=in&apiKey=d706ae3db4e7479abca4128cdad7250a'
    data=requests.get(url)
    read=data.json()

    a=format(read['articles'][0]['title'])
    b=str(format(read['articles'][1]['title']))
    c=format(read['articles'][2]['title'])
    d=format(read['articles'][3]['title'])
    e=format(read['articles'][4]['title'])
    f=format(read['articles'][5]['title'])
    g='Thank you'
    s=str(a + b + c + d + e + f)
    return s
    #print(b)
    #tts.speak(b)
    
    
def weather():
    city="sonipat"
    url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=39acb6922254b1a70d54454710ac118c'
    data=requests.get(url)
    read=data.json()

    n=format(read['name'])
    t=format(read['main']['temp'])
    h=format(read['main']['humidity'])
    p=format(read['main']['pressure'])
    w=format(read['wind']['speed'])
    d=format(read['weather'][0]['description'])
    t=str(float(t)-273.15)
    final=n+" Temperature is "+t
    final1=" Humidity is "+h+" and Pressure is "+p
    final2=" Speed is "+w+" and cloud is "+d
    #final="Sonipat Temperature is 34.0 Humidity is 28 and Pressure is 1008 Speed is 3.6 and cloud is haze"

    #tts.speak(final + final1 + final2)
    return (final+final1+final2)

def ask():    
    query="python"
    #a=wikipedia.summary(query, sentences=2)
    a="Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace."
    print(a)
    tts.speak(a)


def apiRefresh():
    newsReturn=''
    weatherReturn=''
    while True:
        newsReturn=news()
        weatherReturn=weather()
        print(weatherReturn)
        gspeak.speak(newsReturn,"news")
        gspeak.speak(weatherReturn,"weather")
        time.sleep(1000)


#apiRefresh()
