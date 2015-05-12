import pywapi
import pprint
from sys import argv


def getChanceOfPrecip(u_odds):
    odds = int(u_odds)
    if odds <= 10:
        return " with a low chance of precipitation" 
    if odds <= 40: 
        return " with a decent chance of precipitation"
    if odds <= 70: 
        return "with a good chance for precipitation"
    return ", and you can count on precipitation"

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

if len(argv) <= 2: #just wants current weather
    print "It's currently " + weather_com_result['current_conditions']['text'] + " in " + loc_name + " with a temperature of " \
        + weather_com_result['current_conditions']['temperature'] + "C.", 
    if (weather_com_result['current_conditions']['temperature'] != weather_com_result['current_conditions']['feels_like']):
        print "But it feels a little more like " + weather_com_result['current_conditions']['feels_like'] + "C. "
    

    forecast = raw_input("Do you want to see the forecast for today? ")
    if (forecast == "y" or forecast == "Y" or forecast == "Yes" or forecast == "yes"):
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


# else: #forecast
#     day = argv[2].lower()
#     if day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
#         for f in weather_com_result['forecasts']:
#             if weather_com_result['forecasts'][0]['day_of_week'].lower() == day:
#                 forecast = f
#         print forecast
    
    

