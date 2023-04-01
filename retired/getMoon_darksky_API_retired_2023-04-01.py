from __future__ import division
import time
from datetime import datetime
from urllib2 import Request, urlopen, URLError
import json
import auth as au


secret = au.secret
lat = str(au.lat)
lon = str(au.lon)


def accurateMoonCount(moonsSincePrimaveraCero, currentMoonPhase):
    intMoons=int(moonsSincePrimaveraCero)
    remainderMoons = moonsSincePrimaveraCero - float(intMoons)
    chooseMoon=[0,0]
    if(remainderMoons > 0.5):
        chooseMoon=[intMoons,intMoons+1]
    else:
        chooseMoon=[intMoons-1,intMoons]
    if(currentMoonPhase < 0.5):
        fullMoons=chooseMoon[0]
    else:
        fullMoons=chooseMoon[1]

    if(currentMoonPhase+0.5 > 1.):
        fullMoonsFraction=currentMoonPhase+0.5-1.
    else:
        fullMoonsFraction=currentMoonPhase+0.5

    fullMoonsFraction=int(fullMoonsFraction*10000.)

    return fullMoons+float(fullMoonsFraction)/10000.

def getCurrentMoon():

    request = Request('https://api.darksky.net/forecast/'+secret+'/'+lat+','+lon+'?exclude=[minutely,hourly,alerts,flags]')

    try:
        response = urlopen(request)
        currentweather = response.read()
        # print currentweather
    except URLError, e:
        print 'No Weather. Got an error code:', e



    weatherdata = json.loads(currentweather)

    currentTime = weatherdata['currently']['time']
    sunrise = weatherdata['daily']['data'][0]['sunriseTime']
    sunset = weatherdata['daily']['data'][0]['sunsetTime']

    if(currentTime > sunrise and currentTime < sunset):
        daylight=1
    else:
        daylight=0



    midnightToday = weatherdata['daily']['data'][0]['time']
    moonPhaseMidnightToday = weatherdata['daily']['data'][0]['moonPhase']

    currentTime = int(time.time())

    primaveraCero=1428120000.0
    synodicMonthInSeconds = 2551442.8

    moonsSincePrimaveraCero=(currentTime - primaveraCero)/synodicMonthInSeconds

    currentMoonPhase = moonPhaseMidnightToday + (currentTime - midnightToday)/synodicMonthInSeconds

    displayMoons = accurateMoonCount(moonsSincePrimaveraCero,currentMoonPhase)

    return displayMoons, daylight
