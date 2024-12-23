from __future__ import division
import time
from datetime import datetime
from urllib2 import Request, urlopen, URLError
import json
import ssl
import auth as au


secret = au.weatherbit_secret
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
    context = ssl._create_unverified_context()
    request = Request('https://api.weatherbit.io/v2.0/forecast/daily?lat='+lat+'&lon='+lon+'&days=1&key='+secret)

    try:
        response = urlopen(request, context=context)
        currentweather = response.read()
        # print currentweather
    except URLError, e:
        print 'No Weather. Got an error code:', e



    weatherdata = json.loads(currentweather)

    currentTime = int(time.time())
    sunrise = weatherdata['data'][0]['sunrise_ts']
    sunset = weatherdata['data'][0]['sunset_ts']

    if(currentTime > sunrise and currentTime < sunset):
        daylight=1
    else:
        daylight=0



    moonPhasePredictionTime = weatherdata['data'][0]['ts']
    moonPhaseAtPreditionTime = weatherdata['data'][0]['moon_phase_lunation']

    primaveraCero=1428120000.0
    synodicMonthInSeconds = 2551442.8

    moonsSincePrimaveraCero=(currentTime - primaveraCero)/synodicMonthInSeconds

    currentMoonPhase = moonPhaseAtPreditionTime + (currentTime - moonPhasePredictionTime)/synodicMonthInSeconds

    displayMoons = accurateMoonCount(moonsSincePrimaveraCero,currentMoonPhase)

    return displayMoons, daylight
