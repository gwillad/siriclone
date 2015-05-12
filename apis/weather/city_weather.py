import pywapi
from sys import argv
import pprint

script, loc_id = argv
pp = pprint.PrettyPrinter(indent=1)

print loc_id
weather_com_result = pywapi.get_weather_from_weather_com(loc_id)
#weather_com_result = pywapi.get_weather_from_weather_com('USNY1209')
pp.pprint(weather_com_result)

print
print "More detailed information"
print "-------------------------"
print

print "Current conditions:" + weather_com_result['current_conditions']['text']
print "Temperature:" + weather_com_result['current_conditions']['temperature'] + "C"

