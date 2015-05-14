import pywapi
import pprint
from sys import argv
import re


def getChanceOfPrecip(u_odds):
    odds = int(u_odds)
    if odds <= 10:
        return " with a low chance of precipitation" 
    if odds <= 40: 
        return " with a decent chance of precipitation"
    if odds <= 70: 
        return "with a good chance for precipitation"
    return ", and you can count on precipitation"

phrase = argv[1:]

locale = "CLINTON, NY"
day = "TODAY"

months = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']


for i in range(len(phrase)): 
    if phrase[i] == "IN":
        #next word[s] will be a location
        if (phrase[i+1] != "CLINTON" or phrase[i+2] != "NY"): # clinton ny special case
            locale = phrase[i+1]
    elif phrase[i] == "ON":
        if phrase[i+1] in months:
            day = " ".join(phrase[i+1:i+3])
        else: 
            day = phrase[i+1]
    elif phrase[i] in months:
        day = " ".join(phrase[i:i+2])
    elif re.match("\d?\d\/\d?\d", phrase[i]):
        day = phrase[i]
    elif phrase[i] in ['TODAY', 'TOMORROW', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']:
        day = phrase[i]

loc_id_list = pywapi.get_loc_id_from_weather_com(locale)

ans = 0

if locale != "CLINTON, NY" and loc_id_list['count'] > 1:
    for i in range(loc_id_list['count']):
        yn = raw_input("Did you mean, " + loc_id_list[i][1] + "? ")
        if re.match("[yY](es|)?", yn):
            ans = i
            break
    

loc_id = loc_id_list[ans][0]
loc_name = loc_id_list[ans][1]

weather_com_result = pywapi.get_weather_from_weather_com(loc_id)

if len(argv) <= 2 or day == "TODAY" or day == "TONIGHT" or day == "NOW": # just wants current weather
    print "It's currently " + weather_com_result['current_conditions']['text'] + " in " + loc_name + " with a temperature of " \
        + weather_com_result['current_conditions']['temperature'] + "C.", 
    if (weather_com_result['current_conditions']['temperature'] != weather_com_result['current_conditions']['feels_like']):
        print "But it feels a little more like " + weather_com_result['current_conditions']['feels_like'] + "C. "
    

    want_forecast = raw_input("Do you want to see the forecast for today? ")
    if re.match("[yY](es|)?", want_forecast):
        print "Okay! "
        if weather_com_result['forecasts'][0]['day']['text'] != "":
            print "Today it will be " \
                + weather_com_result['forecasts'][0]['day']['text'] \
                + getChanceOfPrecip(weather_com_result['forecasts'][0]['day']['chance_precip']) \
                + ". "
        if weather_com_result['forecasts'][0]['night']['text'] != "":
            print "Tonight it will be " \
                + weather_com_result['forecasts'][0]['night']['text'] \
                + getChanceOfPrecip(weather_com_result['forecasts'][0]['night']['chance_precip']) \
                + ". "


else: #forecast
    day = argv[2].lower()
    forecast = None
    day_or_date = None
    if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        for f in weather_com_result['forecasts']:
            if f['day_of_week'].lower() == day:
                forecast = f
        if forecast == None:
            print "Sorry I don't have data that far in advance. "
    elif day == "tomorrow":
        forecast = weather_com_results['forecasts'][1]
    else:
        month_name = re.compile("(january|february|march|april|may|june|july|august|september|october|november|december)\s+\d?\d")
        month_value = re.compile("\d?\d\/\d?\d")
        
        if month_name.match(day):
            day = " ".join(day.split()[0:2]).strip(",")
        if month_value.match(day):
            print day
            day = " ".join([months[int(day.split("/")[0])], day.split("/")[1]]).strip(",")
        for f in weather_com_result['forecasts']:
            if f['date'].lower() == day:
                forecast = f
        day = day[0:1].upper() + day[1:]
        if forecast == None: 
            print "Sorry I don't have that date. "
    
       
    if forecast != None:
        if forecast['day']['text'] != "":
            print "The weather on " + day + " during the day will be " \
                + forecast['day']['text'] \
                + getChanceOfPrecip(forecast['day']['chance_precip']) \
                + ". "
        if forecast['night']['text'] != "":
            print "The weather on " + day + " at night will be " \
                + forecast['night']['text'] \
                + getChanceOfPrecip(forecast['day']['chance_precip']) \
                + ". "
        print "There will be a high of " \
            + forecast['high'] + "C and a low of " \
            + forecast['low'] + ". "

