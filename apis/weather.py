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

months = { '1': "january",
           '2': "february",
           '3': "march",
           '4': "april",
           '5': "may",
           '6': "june",
           '7': "july",
           '8': "august",
           '9': "september",
           '10': "october",
           '11': "november",
           '12': "december" }

locale = argv[1]
pp = pprint.PrettyPrinter(indent=4)

loc_id_list = pywapi.get_loc_id_from_weather_com(locale)

#pp.pprint(loc_id)

ans = 0

if loc_id_list['count'] > 1:
    print "Which " + locale + " did you mean?" 
    for i in range(loc_id_list['count']):
        print "%d. " % (i + 1), loc_id_list[i][1]
    ans = int(raw_input("Enter the relevent number: ")) - 1
    

loc_id = loc_id_list[ans][0]
loc_name = loc_id_list[ans][1]

weather_com_result = pywapi.get_weather_from_weather_com(loc_id)
pp.pprint(weather_com_result)

if len(argv) <= 2 or argv[2].lower() == "today" or argv[2].lower() == "tonight" or argv[2].lower() == "now" or " ".join(argv[2:]).lower() == "right now" : #just wants current weather
    print "It's currently " + weather_com_result['current_conditions']['text'] + " in " + loc_name + " with a temperature of " \
        + weather_com_result['current_conditions']['temperature'] + "C.", 
    if (weather_com_result['current_conditions']['temperature'] != weather_com_result['current_conditions']['feels_like']):
        print "But it feels a little more like " + weather_com_result['current_conditions']['feels_like'] + "C. "
    

    want_forecast = raw_input("Do you want to see the forecast for today? ")
    if (want_forecast == "y" or want_forecast == "Y" or want_forecast == "Yes" or want_forecast == "yes"):
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
            day = " ".join([months[day.split("/")[0]], day.split("/")[1]]).strip(",")
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

